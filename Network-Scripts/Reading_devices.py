from pprint import pprint
import json
import re

# devices_interface=[]
show_interfaces = 'devices.txt'


def parse_interfaces(output):
    interfaces_pattern = "^[dls]\S+[0-9]\/?[0-9]*|^-"
    regex = re.compile(interfaces_pattern)
    with open('devices.txt') as f:
        devices = f.read().splitlines()
        print(devices)
        print(len(devices))
    interfaces_list = list()
    for interfaces in devices:
        if regex.search(interfaces):
            interfaces_list.append({
                'interface': interfaces.split()[0],
                'IPAddress': interfaces.split()[1],
                'State': interfaces.split()[2],
                'SpeedDuplex': interfaces.split()[3],
                'Description': interfaces.split()[4:]

            })

        for i in range(len(interfaces_list)):
            if interfaces_list[i]['interface'] == '-':
                interfaces_list[i]['interface'] = interfaces_list[i - 1]['interface']

    #print(dict(interfaces_list[0]))
    pprint(json.dumps(interfaces_list[1:]))
    #print(type(interfaces_list))
    print(len(interfaces_list))


parse_interfaces('devices.txt')
