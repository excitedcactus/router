from netmiko import Netmiko
from getpass import getpass

router = {
    "host": "router ip",
    "username": "admin",
    "password": getpass(),
    "device_type": "cisco_nxos",
}

commands = ["show access-lists"]

net_connect = Netmiko(**router)

print()
print(net_connect.find_promt())
output = net_connect.send_config_set(commands)
output += net_connect.send_command("copy run start")
print(output)
print()
