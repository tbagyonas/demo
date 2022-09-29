import re
import json
from collections import Counter
from itertools import chain
import pandas as pd
def dsearch(lod, **kw):

    result=list(filter(lambda i: all((i[k] == v for (k, v) in kw.items())), lisRes))
    print(result)
    return result

lod=('[{"interface": "dp0ce1", "IPAddress": "-", "State": "u/D", "SpeedDuplex": '
 '"auto/auto", "Description": ["-"]}, {"interface": "dp0p7s0", "IPAddress": '
 '"10.156.43.100/24", "State": "u/u", "SpeedDuplex": "a-1g/a-full", '
 '"Description": ["Mgmt", "Network"]}, {"interface": "dp0xe0", "IPAddress": '
 '"-", "State": "u/u", "SpeedDuplex": "10g/full", "Description": ["-"]}, '
 '{"interface": "dp0xe1", "IPAddress": "-", "State": "u/u", "SpeedDuplex": '
 '"10g/full", "Description": ["-"]}, {"interface": "dp0xe11", "IPAddress": '
 '"10.156.21.2/20", "State": "u/u", "SpeedDuplex": "1g/full", "Description": '
 '["-"]}, {"interface": "dp0xe12", "IPAddress": "-", "State": "A/D", '
 '"SpeedDuplex": "auto/auto", "Description": '
 '["link-to-TimeProvider4100-eth4"]}, {"interface": "dp0xe13", "IPAddress": '
 '"-", "State": "u/D", "SpeedDuplex": "auto/auto", "Description": ["-"]}, '
 '{"interface": "lo1", "IPAddress": "1.1.1.1/32", "State": "u/u", '
 '"SpeedDuplex": "-/-", "Description": ["-"]}, {"interface": "sw0", '
 '"IPAddress": "-", "State": "u/u", "SpeedDuplex": "-/-", "Description": '
 '["-"]}, {"interface": "sw0.50", "IPAddress": "10.0.0.2/30", "State": "u/u", '
 '"SpeedDuplex": "-/-", "Description": ["-"]}, {"interface": "sw0.100", '
 '"IPAddress": "192.168.4.1/24", "State": "u/D", "SpeedDuplex": "-/-", '
 '"Description": ["-"]}, {"interface": "sw0.1001", "IPAddress": '
 '"100.100.0.1/24", "State": "u/u", "SpeedDuplex": "-/-", "Description": '
 '["-"]}, {"interface": "sw0.1001", "IPAddress": "100:100::1/64", "State": '
 '"-", "SpeedDuplex": "-", "Description": ["-"]}, {"interface": "sw0.1002", '
 '"IPAddress": "192.168.1.2/30", "State": "u/u", "SpeedDuplex": "-/-", '
 '"Description": ["-"]}, {"interface": "sw0.1002", "IPAddress": '
 '"192.168.2.2/30", "State": "-", "SpeedDuplex": "-", "Description": ["-"]}, '
 '{"interface": "sw0.1002", "IPAddress": "cef:0:4:3:2:1:0:4/128", "State": '
 '"-", "SpeedDuplex": "-", "Description": ["-"]}, {"interface": "sw0.1026", '
 '"IPAddress": "100.100.8.1/24", "State": "u/u", "SpeedDuplex": "-/-", '
 '"Description": ["-"]}, {"interface": "sw0.1026", "IPAddress": '
 '"100:100:8::1/64", "State": "-", "SpeedDuplex": "-", "Description": ["-"]}, '
 '{"interface": "sw0.4004", "IPAddress": "4.4.0.1/24", "State": "u/D", '
 '"SpeedDuplex": "-/-", "Description": ["-"]}]')
lisRes=json.loads(lod)

new_k = 'interface'

values={}
new_output = Counter(sub[new_k] for sub in lisRes)
for k,v in new_output.items():
 if new_output[k]>1:
  values[k]=v

#print(values)
dct={}

for k,v in new_output.items():
 if new_output[k]>1:
  multiples={k:v}
  #print(multiples)

for i in range(len(lisRes)):
 values={}
 if lisRes[i]['interface'] in multiples:
  values= {lisRes[i]['interface']:{lisRes[i]['State'],lisRes[i+1]['IPAddress']}}
print(values)


print('-----------------------------------------------')


def filtered(lisRes):
 #global item
 item = [item for item in lisRes if re.match(r"192\.168", item['IPAddress'])]
 for i in range(len(item)):
  print(item[i]['interface'], item[i]['IPAddress'])





filtered(lisRes)

# from collections import defaultdict
# a =[{'id': 1,'desc': 'smth'},
#     {'id': 2,'desc': 'smthelse'},
#     {'id': 1,'desc': 'smthelse2'},
#     {'id': 1,'desc': 'smthelse3'}]
# d = defaultdict(list)
# for x in lisRes:
#     d[x['interface']].append(x['IPAddress']) # group description by id
# #print(d)
# b = [dict(interface=interface, IPaddress=IPAddress if len(IPAddress) > 1 else IPAddress[0])
#      for interface, IPAddress in d.items()]
# print(b)

# b = []
# for id in (x['id'] for x in a):
#     desc = d[id]
#     if desc:
#        b.append(dict(id=id, desc=desc if len(desc) > 1 else desc[0]))
#        del d[id]
#        #print(b)
# txt=input()
# def spell(txt):
#     for i in range(len(txt)):
#         print(txt[-1-i])
#
# spell(txt)

for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(f"{n} equals {x}*{n//x}")
            break
    else:
        print(f"{n} is a prime number")
import netaddr
from netaddr import IPNetwork


def summarize():
 global ip, ip_list
 ip_list=[]
 #ip_list = [ip for ip in IPNetwork('fe80::/120')]
 for ip in IPNetwork('fe80::/120'):
  ip_list.append(ip)

 ip_list.append(IPNetwork('192.0.2.0/24'))
 ip_list.extend([str(ip) for ip in IPNetwork('192.0.3.0/24')])
 ip_list.append(IPNetwork('192.0.4.0/25'))
 ip_list.append(IPNetwork('192.0.4.128/25'))
 print(ip_list)
 return netaddr.cidr_merge(ip_list)


print(summarize())
#summary = netaddr.cidr_merge(ip_list)
#print(summary)

