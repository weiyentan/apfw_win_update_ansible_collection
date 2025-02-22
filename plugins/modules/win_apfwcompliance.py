#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>, and others
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# this is a windows documentation stub.  actual code lives in the .ps1
# file of the same name

ANSIBLE_METADATA = {}

DOCUMENTATION = r'''
---
module: win_apfwcompliance
version_added: "0.1"
short_description: Checks the value of the patching status on a computer
description:
  - Checks the patching status of the computer using the APFW framework.
  - This module retrieves compliance information related to patching by checking the status of the job and the number of patches remaining.
  - If the job has not started or has failed, an appropriate message will be returned.
  - Outputs include:
    - `changed`: Indicates whether any changes were made.
    - `Patchstatus`: Current status of the patching process.
    - `Patchesremaining`: Number of patches remaining to be applied.
    - `daterun`: Date when the patches were last run.
options:
  data:
    description:
      - 
notes:
  - Requires the AutomatedPatching playbook to be run on the machine.
  - If the XML file does not exist, a message indicating the job status is undetermined will be returned.
author:
- Wei-Yen Tan (@weiyen)
'''

EXAMPLES = r'''
# Check Windows Patching status on machines that are being patched
# by the AutomatedPatching playbook.
# Example from an Ansible Playbook
- win_apfwcompliance:

RETURN = '''
win_apfwcompliance:
    description: default output from job
    
ok: [] => {
    "Patchesremaining": 0,
    "Patchstatus": "success",
    "changed": false

'''