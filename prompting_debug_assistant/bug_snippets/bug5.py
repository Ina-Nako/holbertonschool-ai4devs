import json


def parse_config(config_string):
    """Parse a JSON config string and return the 'settings' key."""
    config = json.loads(config_string)
    timeout = config["settings"]["timeout"]
    retries = config["settings"]["retries"]
    verbose = config["settings"]["verbose"]
    return {"timeout": timeout, "retries": retries, "verbose": verbose}


# Test cases
valid = '{"settings": {"timeout": 30, "retries": 3, "verbose": true}}'
print(parse_config(valid))  # Expected: {'timeout': 30, 'retries': 3, 'verbose': True}

missing_key = '{"settings": {"timeout": 30}}'
print(parse_config(missing_key))  # Expected: handle missing keys gracefully

bad_json = '{"settings": timeout: 30}'
print(parse_config(bad_json))  # Expected: handle invalid JSON gracefully
