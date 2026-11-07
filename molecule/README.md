# Molecule test this role

## Scenario - `default`
This will test the role installing miarec_livemon.

Run Molecule test
```
uv run molecule test
```

Run test with variable example
```
MOLECULE_DISTRO=rockylinux9 uv run molecule test
```

### Molecule variables
 - `MOLECULE_DISTRO` OS of docker container to test, default `ubuntu2404`
   - Tested distros;
    - `ubuntu2204`
    - `ubuntu2404`
    - `rockylinux9`
    - `rhel9`
 - `MOLECULE_MIAREC_LIVEMON_VERSION` defines variable miarec_livemon_version, default `0.1.0.183`
 - `MOLECULE_ANSIBLE_VERBOSITY` `0-3`, sets ansible verbosity for debugging, default `0`
