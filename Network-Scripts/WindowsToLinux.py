import paramiko
import time
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname':'192.168.43.179','port':'22','username':'yohannes','password':'Yohan1304'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux,look_for_keys=False,allow_agent=False)
shell=ssh_client.invoke_shell()
shell.send('cat /etc/passwd\n')
time.sleep(5)

output=shell.recv(1000)
output=output.decode('utf-8')
print(output)