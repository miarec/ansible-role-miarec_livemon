import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

miarec_livemon_version = os.environ.get('MIAREC_LIVEMON_VERSION')


def test_directories(host):

    dirs = [
        "/opt/miarec_livemon/releases/{}".format(miarec_livemon_version),
        "/opt/miarec_livemon/shared",
        "/var/log/miarec_livemon"
    ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists

def test_files(host):
    files = [
        "/opt/miarec_livemon/releases/{}/miarec_livemon.ini".format(miarec_livemon_version),
        "/opt/miarec_livemon/releases/{}/miarec_livemon".format(miarec_livemon_version),
        "/var/log/miarec_livemon/livemon.log"
    ]

    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file

def test_service(host):

    services = [
        "miarec_livemon"
    ]

    for service in services:
        s = host.service(service)
        assert s.is_enabled
        assert s.is_running

def test_socket(host):
    sockets = [
        "tcp://0.0.0.0:6087"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
