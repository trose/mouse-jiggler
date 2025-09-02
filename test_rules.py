#!/usr/bin/env python3
"""
Test script to validate the jigglypuff rules configuration.
"""

import json
import os
import sys

def test_rules_config():
    """Test that the rules configuration is valid JSON and has expected structure."""
    config_path = os.path.join(os.path.dirname(__file__), 'jigglypuff_rules.json')
    
    try:
        with open(config_path, 'r') as f:
            rules_config = json.load(f)
        
        # Check that rules exist
        assert 'rules' in rules_config, "Configuration must have 'rules' key"
        assert isinstance(rules_config['rules'], list), "'rules' must be a list"
        assert len(rules_config['rules']) == 2, "Expected exactly 2 rules"
        
        # Check rule structure
        enable_rule = rules_config['rules'][0]
        disable_rule = rules_config['rules'][1]
        
        # Validate enable rule
        assert enable_rule['name'] == 'enable_jiggling_before_tasks', "First rule must be 'enable_jiggling_before_tasks'"
        assert 'trigger' in enable_rule, "Rule must have 'trigger'"
        assert 'actions' in enable_rule, "Rule must have 'actions'"
        assert len(enable_rule['actions']) == 1, "Rule must have exactly one action"
        
        # Validate disable rule
        assert disable_rule['name'] == 'disable_jiggling_after_tasks', "Second rule must be 'disable_jiggling_after_tasks'"
        assert 'trigger' in disable_rule, "Rule must have 'trigger'"
        assert 'actions' in disable_rule, "Rule must have 'actions'"
        assert len(disable_rule['actions']) == 1, "Rule must have exactly one action"
        
        print("✅ All rule configuration tests passed!")
        return True
        
    except FileNotFoundError:
        print(f"❌ Configuration file not found at {config_path}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in configuration file: {e}")
        return False
    except AssertionError as e:
        print(f"❌ Configuration validation failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_rules_config()
    sys.exit(0 if success else 1)