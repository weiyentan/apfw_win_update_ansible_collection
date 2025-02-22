# apfw_win_update

## Overview
APFW stands for Automated Patching Framework Windows.


The **apfw_win_update** Ansible collection is designed to speed up and simplify the process of managing Windows updates using the `PSWindowsUpdate` module and PowerShell automation. This collection provides a structured way to handle Windows updates and compliance through Ansible, making it easier for system administrators to manage updates across multiple Windows systems.



The install_winupdates role is designed to install Windows updates using the `PSWindowsUpdate` module.  The install_winupdates role is designed to install Windows updates using the `PSWindowsUpdate` module. It requires a Windows Update Server / Update Server. 

## How it Differs from Traditional `win_update` Task

The `apfw_win_update` collection differs from the native Ansible `win_update` module in its approach to managing updates. While the native `win_update` module directly installs updates, `apfw_install_winupdates` uses Ansible to configure the machine and deploy patching scripts, create a scheduled task to run these scripts.. These scripts handle the logic of installing updates and rebooting, providing more control and flexibility.

The `apfw_wait` role, which monitors the update process to ensure updates are applied successfully and pauses playbook execution if the update process is not completed. This collection is more scalable and can be used to manage multiple systems simultaneously. 

## Installation and Usage

Before using the **apfw_win_update** collection, you need to install it with the ansible-galaxy CLI:

```bash
ansible-galaxy collection install apfw.apfw_win_update
```

You can also include it in a `requirements.yml` file and install it via:

```yaml
collections:
  - name: apfw.apfw_win_update
```

```bash
ansible-galaxy collection install -r requirements.yml
```

## Communication
If you have any questions or need help, feel free to join our [Discord Channel](https://discord.gg/FQjREauPVt).



## Ansible Version Compatibility

This collection has been tested against the following Ansible versions: >=2.15. Plugins and modules within a collection may be tested with only specific Ansible versions.

## Changelog

- **2025-02-22**: Renamed `install_winupdates` role to `apfw_install_winupdates` to align with the naming convention of other roles in the collection.
See [CHANGELOG.rst](CHANGELOG.rst) for the release history and changes made to this collection.

## Collection Documentation

Browsing the [latest collection documentation](https://docs.ansible.com/ansible/latest/collections/community/windows) will show docs for the latest version released in the Ansible package. If you are looking to contribute, please refer to the latest commit documentation.

## Contributing to this collection

Currently, we welcome bug fixes or feature requests to plugins in this collection, but no new modules or plugins will be accepted. If you find problems, please open an issue or create a PR against the Community Windows collection repository. See [Contributing to Ansible-maintained collections](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html) for details.

## License

This collection is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## About

Ansible collection for APFW Windows Update. For more information about APFW's Windows integration, browse the resources in the [APFW Windows Update](https://github.com/apfw/apfw_win_update) collection documentation.
