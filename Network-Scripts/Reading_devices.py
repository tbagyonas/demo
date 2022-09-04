from pprint import pprint
import json
with open('devices.txt') as f:
    devices = f.read().splitlines()
    print(devices)
    print(len(devices))
interfaces_list = list()
for interfaces in devices:
    devices_interface = {
        'interface':interfaces.split()[0],
        'IP-Address':interfaces.split()[1],
        'S/L':interfaces.split()[2],
        'Speed/Duplex':interfaces.split()[3],
        'Description':interfaces.split()[4:]


    }
    interfaces_list.append(devices_interface)


for i in range(len(interfaces_list)):
    if interfaces_list[i]['interface']=='-':
        interfaces_list[i]['interface']=interfaces_list[i-1]['interface']

#print(interfaces_list)
pprint(json.dumps(interfaces_list))
print(interfaces_list[17])
print(len(interfaces_list))
