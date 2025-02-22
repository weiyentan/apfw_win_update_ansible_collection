# APFW Wait Role

This Ansible role manages Windows patching workflows by monitoring completion status through file/endpoint checks, beginning with a 10-second initialization delay. It implements a robust retry system with exponential backoff - featuring separate retry counters for network issues (10 attempts max) and general failures (100 retries max), using progressively increasing delays from 300s for connections and 600s between operation checks. The role enforces strict timeout safeguards with a default 300-second threshold, preventing infinite loops through fail-safe mechanisms while providing clear timeout notifications.

Key features:
- Configurable timeout thresholds
- Automatic retries for transient failures
- Progressive delay increases between checks
- Connection attempt tracking


## Role Variables

### Main Parameters
- `apfw_wait_timeout` (default: 300) - Total timeout in seconds
- `apfw_wait_retry_delay` (default: 5) - Delay between retry attempts
- `apfw_wait_max_retries` (default: 100) - Maximum connection attempts
- `connection_delay` (default: 300) - Delay between connection retries

## Usage Example

```yaml
- name: Wait for patching completion
  include_role:
    name: apfw_wait
  vars:
    apfw_wait_timeout: 600  # 10 minutes
    connection_delay: 120   # 2 minutes between status checks
