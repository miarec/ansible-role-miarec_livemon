# ansible-role-miarec-livemon

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




