# Ansible - APFW Patching

This role is to configure the machine to be ready for patching. It uses the underlying PowerShell module PSWindowsUpdate to do the underlying work for Windows Patching. With this framework, you can provide an end time and end date to when the patching will finish.

This role will create registry values that the patching logic will refer to when determining the end date and end time of the patching period.

It will also create scheduled tasks that will perform the patching tasks Install_Patch and Monitor_Patch. The Monitor_Patch scheduled task provides the logic to restart the computer and restart the Install_Patch scheduled task. This could involve multiple restarts within the time period.

Once the Patching process has completed, the monitor_patch script will clean up the scheduled tasks and the monitor_patch ps1 file itself. It will clean up whether it successfully patched within the operating hours being set.

The wait time of the patching has been set as the default as 10 minutes in default settings.

## Variables
- `apfw_enddate`: The end date for the patching process.
- `apfw_endtime`: The end time for the patching process.
- `duration`: The duration for which the patching should run before it stops.

## Tags
There are different tags in the Ansible Patching role. The following tags exist:
* enddateregistry (End date registry entry) 
* endtimeregistry (End time registry entry)
* duration (Duration registry entry)
* copyipm (Copy Patch Monitoring file) 
* copypswin (Copy PSWindowsUpdate)
* schtsk_ip (Sets up scheduled task for Install_Patch)
* schtsks_mp (Sets up scheduled task for Monitor_Patch)
* runschtask_ip (Runs Install_Patch)
* runschtask_mp (Runs Monitor_Patch)

## Process
1. Creates registry entries for end date and end time when the Windows computers will stop the patching logic.
2. Creates a registry entry for the duration of the patching process.
3. Copy across the file called PatchMonitoring.ps1 that will contain the logic to handle reboots and installation of the patching using PSWindowsUpdate as the underlying module.
4. Copy across the installpatch.ps1 that generates the first patching status file on the computer being patched.
5. Copy across the PSWindowsUpdate module to the modules directory.
6. Create a scheduled task Install_Patch that is configured to respond to a dummy event that will never execute so it will be set to run once (this is done so the install_patch can only respond to an instruction not a time trigger).
7. Create a scheduled task called Monitor_Patch that will run the script Patchmonitoring.ps1 script at boot. This is to accommodate for a reboot and have the logic continue the patching cycle when the computer reboots.
8. Run the Install_Patch scheduled task.
9. Run the Patch_Monitoring scheduled task.
10. The Patching cycle begins at this point. It will use its logic to start the patching if there are remaining patches left (and Windows installer not started) and reboot the server if it needs it. During the patching cycle, the script logs its activities in a log prefixed with apfw_patching_dd_mm_yy.log. It also produces a patching status file that can be referred to in Ansible through another playbook called AnsibleAutomatedPatchingCompliance. This file has certain information in it, including the total number of patches and reboot status.
11. If patching completes, it goes through the clean-up stage and will log that there is a success in patching. The helper function will:
    * stop the install_patch scheduled task 
    * stop the monitor_patch scheduled task
    * remove the install_patch scheduled task
    * remove the patch monitoring file 
    * remove the folder apfwpatching in the registry that is used.
12. If patching fails (because it went outside the patch window), the system will go through the same process of cleaning up but will log a failure message in the log.
