#!/usr/bin/env python3
import subprocess

def check_service(name):
    r = subprocess.run(
        ['systemctl', 'is-active', name],
        capture_output=True,
        text=True
    )
    return r.stdout.strip()

services = ['nginx', 'ssh', 'cron']

print('=== SERVICE STATUS ===')
for svc in services:
    status = check_service(svc)
    icon = 'OK' if status == 'active' else 'DOWN'
    print(f'  [{icon}] {svc}: {status}')

