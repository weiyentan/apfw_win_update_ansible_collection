# APFW Windows Compliance Role

This role reports compliance policies on Windows systems.

## Purpose

The `apfw_win_compliance` role is designed to report compliance policies on Windows systems. It includes tasks for pausing playbook execution and checking patching status.

## Tasks

### Pause

Pauses playbook execution for a specified number of minutes, controlled by the `apfw_minwait` variable.

### Patching Status

Checks the patching status on Windows systems using the `win_apfwcompliance` module.

## Variables

Below are the key variables you can configure:

- `apfw_minwait`: Number of minutes to pause playbook execution (default: `0`).

## Example Playbook

```yaml
- hosts: windows
  roles:
    - role: apfw_win_compliance
      vars:
        apfw_minwait: 5