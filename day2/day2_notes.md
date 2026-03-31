# Day 17 - Python: Conditions, Loops, Functions

## Theory
- Control flow is the core of all scripts
- These are the building blocks of every DevOps automation tool

## Conditions

### If/Elif/Else
```python
cpu = 85
if cpu > 90:
    print('CRITICAL')
elif cpu > 70:
    print('WARNING')
else:
    print('OK')
```

### Logical Operators
```python
# and, or, not, in
if cpu > 70 and cpu < 100:
    print('High but alive')

tools = ['docker', 'linux']
if 'docker' in tools:
    print('Docker found')
```

## Loops

### For Loop
```python
services = ['nginx', 'mysql', 'redis']
for svc in services:
    print(f'Checking {svc}...')

# Range
for i in range(1, 6):  # 1 to 5
    print(f'Attempt {i}')
```

### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control
```python
# break = stop loop entirely
# continue = skip current iteration
for i in range(10):
    if i == 5: break      # stops at 5
    if i == 3: continue   # skips 3
    print(i)
```

## Functions

### Basic Function
```python
def greet(name):
    print(f'Hello {name}!')

greet('DevOps')
```

### With Return Value + Default Parameter
```python
def check_cpu(usage, threshold=80):  # default param
    if usage > threshold:
        return 'HIGH'
    return 'NORMAL'

print(check_cpu(85))      # HIGH
print(check_cpu(50))      # NORMAL
print(check_cpu(85, 90))  # NORMAL (threshold=90)
```

### Multiple Return Values
```python
def get_server():
    return 'web01', '10.0.0.1', 'running'

name, ip, status = get_server()
print(name, ip, status)
```

## Key Takeaways
- `elif` = else if — chain as many as you need
- `in` operator checks if item exists in list — very useful
- `range(1, 6)` gives 1,2,3,4,5 — end number is excluded
- Default parameters make functions flexible: `def fn(x, threshold=80)`
- Functions can return multiple values — unpack them directly
- `break` exits loop, `continue` skips to next iteration

## Script Written Today

**`day17/service_checker.py`**
```python
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
```

## Git Commit
```bash
git add .
git commit -m "Day 17: Python conditions loops functions service checker"
git push
```# Day 17 - Python: Conditions, Loops, Functions

## Theory
- Control flow is the core of all scripts
- These are the building blocks of every DevOps automation tool

## Conditions

### If/Elif/Else
```python
cpu = 85
if cpu > 90:
    print('CRITICAL')
elif cpu > 70:
    print('WARNING')
else:
    print('OK')
```

### Logical Operators
```python
# and, or, not, in
if cpu > 70 and cpu < 100:
    print('High but alive')

tools = ['docker', 'linux']
if 'docker' in tools:
    print('Docker found')
```

## Loops

### For Loop
```python
services = ['nginx', 'mysql', 'redis']
for svc in services:
    print(f'Checking {svc}...')

# Range
for i in range(1, 6):  # 1 to 5
    print(f'Attempt {i}')
```

### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control
```python
# break = stop loop entirely
# continue = skip current iteration
for i in range(10):
    if i == 5: break      # stops at 5
    if i == 3: continue   # skips 3
    print(i)
```

## Functions

### Basic Function
```python
def greet(name):
    print(f'Hello {name}!')

greet('DevOps')
```

### With Return Value + Default Parameter
```python
def check_cpu(usage, threshold=80):  # default param
    if usage > threshold:
        return 'HIGH'
    return 'NORMAL'

print(check_cpu(85))      # HIGH
print(check_cpu(50))      # NORMAL
print(check_cpu(85, 90))  # NORMAL (threshold=90)
```

### Multiple Return Values
```python
def get_server():
    return 'web01', '10.0.0.1', 'running'

name, ip, status = get_server()
print(name, ip, status)
```

## Key Takeaways
- `elif` = else if — chain as many as you need
- `in` operator checks if item exists in list — very useful
- `range(1, 6)` gives 1,2,3,4,5 — end number is excluded
- Default parameters make functions flexible: `def fn(x, threshold=80)`
- Functions can return multiple values — unpack them directly
- `break` exits loop, `continue` skips to next iteration

## Script Written Today

**`day17/service_checker.py`**
```python
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
```

## Git Commit
```bash
git add .
git commit -m "Day 17: Python conditions loops functions service checker"
git push
```
