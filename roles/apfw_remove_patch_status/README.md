# apfw_remove_patch_status

## Overview

The **apfw_remove_patch_status** role is designed to manage the status of installed patches on Windows systems. It performs cleanup of patch status files and scheduled tasks related to patching.

## Role Tasks
- **Remove Patch Status file**: Cleans up any existing patch status files to ensure a clean state.
- **Remove scheduled task Install_Patch**: Deletes the scheduled task named `Install_Patch` to prevent it from running.
- **Remove scheduled task Monitor_Patch**: Deletes the scheduled task named `Monitor_Patch` to prevent it from running.

## Variables
This role uses the following variables:
- `apfw_patch_status_file`: Path to the patch status file that needs to be removed.

## Example Usage
To use this role in your playbook, you can include it as follows:
```yaml
- name: Remove Patch Status
  hosts: windows
  roles:
    - apfw_remove_patch_status
```

## Dependencies
This role may require the `win_updates` role to be present in your playbook for overall patch management.