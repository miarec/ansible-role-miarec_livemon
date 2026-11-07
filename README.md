# ansible-role-miarec-livemon
![CI](https://github.com/miarec/ansible-role-miarec_livemon/actions/workflows/ci.yml/badge.svg?event=push)

Ansible role for installing of MiaRec Live Monitoring server application.


Role Variables
--------------

- `miarec_livemon_version`: The version of miarec livemon files to install
- `miarec_livemon_install_dir`: The installation directory (default: /opt/miarec_livemon)
- `miarec_livemon_log_dir`: The location of log files (default: /var/log/miarec_livemon)
- `miarec_livemon_rest_api_port`: The REST API port (default: 6087)

Example Playbook
----------------

eg:

``` yaml
    - name: Install miarec live monitoring server
      hosts: localhost
      become: yes
      roles:
        - role: ansible-role-miarec_livemon
          miarec_livemon_version: 1.1.0.11
```

The above playbook will install miarec_livemon version 1.1.0.11.

## Testing

This role uses [Molecule](https://molecule.readthedocs.io/) with Docker for testing.
[uv](https://docs.astral.sh/uv/) is used for dependency management.

### Prerequisites

- Docker
- uv (install via `curl -LsSf https://astral.sh/uv/install.sh | sh`)

### Running Tests

```bash
# Run full test suite
uv run molecule test

# Test against specific distro
MOLECULE_DISTRO=ubuntu2404 uv run molecule test
MOLECULE_DISTRO=rockylinux9 uv run molecule test
```

### Available Distros

| Distribution   | Variable Value  |
|----------------|-----------------|
| Ubuntu 22.04   | `ubuntu2204`    |
| Ubuntu 24.04   | `ubuntu2404`    |
| Rocky Linux 9  | `rockylinux9`   |
| RHEL 9         | `rhel9`         |

### Linting

```bash
uv run ansible-lint
```
