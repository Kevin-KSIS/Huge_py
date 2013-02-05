import os
import md5
import re

if "Wow6432Node" in os.popen('REG QUERY HKEY_LOCAL_MACHINE\\SOFTWARE\\').read():
    os.popen('REG QUERY HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Cryptography\Protect\Providers /v Preferred').read().split(" ")[-1: ][0].split("\n")[0]
else:
    WID = re.findall('MachineGuid\\.*(.*)\n' , os.popen('REG QUERY HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography /v MachineGuid').read())[0].split('\t')[-1:][0]
print HWID
