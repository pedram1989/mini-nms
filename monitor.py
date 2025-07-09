# MiniNMS -  مانیتورینگ سبک و ساده برای شبکه‌های کوچک

# فایل اصلی شروع پروژه - monitor.py

import time
import os
import json
import subprocess
from pysnmp.hlapi import *

def ping_device(ip):
    try:
        output = subprocess.check_output(['ping', '-c', '1', '-W', '1', ip])
        return True
    except subprocess.CalledProcessError:
        return False

def get_snmp_data(ip, community, oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        return None
    elif errorStatus:
        return None
    else:
        for varBind in varBinds:
            return str(varBind[1])

def monitor():
    with open('config/devices.json') as f:
        devices = json.load(f)

    results = []
    for device in devices:
        status = ping_device(device['ip'])
        uptime = get_snmp_data(device['ip'], device['community'], '1.3.6.1.2.1.1.3.0')  # sysUpTime
        results.append({
            'name': device['name'],
            'ip': device['ip'],
            'status': status,
            'uptime': uptime
        })

    with open('monitoring_output.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == '__main__':
    while True:
        monitor()
        time.sleep(60)  # هر 60 ثانیه یک‌بار بررسی کن
