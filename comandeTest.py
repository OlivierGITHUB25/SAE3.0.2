import psutil
import os
import subprocess
import sys
import platform


var="C:"
os.system(f"dir {var}")

#os.system(f"cpu")
os.system(f"python --version")
#os.system(f"ping 8.8.8.8")
os.system(f"powershell get-process")
print(psutil.virtual_memory().percent)
print(psutil.cpu_percent())
print(os.name)
print(platform.system())
