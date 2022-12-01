import psutil
import os
import socket
import subprocess
import sys
import platform
#import netifacespip


var="C:"
os.system(f"dir {var}")

#os.system(f"cpu")
os.system(f"python --version")
#os.system(f"ping 8.8.8.8")
#os.system(f"powershell get-process")
print(psutil.virtual_memory().percent)
print(psutil.cpu_percent())
print(psutil.disk_usage("c:"))
print(os.name)
print(platform.system())
#os.system(("ipconfig").encode('utf-8'))
rep = os.popen("ipconfig ")
print(f"{rep.read()}")
print(socket.gethostname())
#print(socket.getsockname())
print(socket.gethostbyname(socket.gethostname()))
#process = subprocess.Popen("ipconfig")
#output =process.communicate()
#print (output)
#for ifaceName in interfaces():
 #   addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
  #  print(' '.join(addresses))
p = subprocess.Popen('ping 8.8.8.8' , shell=True, stdout=subprocess.PIPE)
print (subprocess.Popen('ping 8.8.8.8' , shell=True, stdout=subprocess.PIPE))