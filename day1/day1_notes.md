# Day 16 - Python Basics: Variables, Data Types, I/O

## Theory
- Python reads like English — easiest language to start with
- Run Python: `python3 filename.py`
- Interactive mode: just type `python3`

## Core Concepts

### 1. Variables & Data Types
```python
name = 'Chandrashekhar'  # string
age = 21                  # integer
gpa = 9.1                 # float
placed = False            # boolean

# Print with f-strings (best way)
print(f'My name is {name}, age {age}')
```

### 2. Input from User
```python
name = input('Enter name: ')
print(f'Hello {name}!')

# Read with prompt
read -p 'Enter age: '  # bash style
# Python style:
age = input('Enter age: ')
print(f'You are {age} years old')
```

### 3. Lists — Ordered, Changeable
```python
skills = ['Linux', 'Docker', 'Python', 'AWS']
skills.append('Kubernetes')  # add item
skills.remove('Linux')       # remove item
print(skills[0])             # first item
print(skills[-1])            # last item
print(len(skills))           # count

# Loop through list
for skill in skills:
    print(skill)
```

### 4. Dict — Key-Value Pairs
```python
server = {'name':'web01', 'ip':'192.168.1.1', 'port':80}
print(server['name'])        # access value
server['status'] = 'running' # add key

# Loop through dict
for k, v in server.items():
    print(f'{k}: {v}')
```

### 5. Type Conversion
```python
int("42")      # string to int
str(100)       # int to string
float("3.14")  # string to float
```

## Script Written Today

**`day16/basics.py`**
```python
#!/usr/bin/env python3
name = input('Your name: ')
city = input('Your city: ')

skills = ['Linux', 'Git', 'Python', 'Docker', 'AWS']

server = {
    'hostname': 'web01',
    'ip': '192.168.1.1',
    'port': 8080,
    'status': 'running'
}

print(f'\n=== PROFILE ===')
print(f'Name  : {name}')
print(f'City  : {city}')
print(f'Skills: {skills}')

print(f'\n=== SERVER ===')
for k, v in server.items():
    print(f'  {k}: {v}')
```

## Key Takeaways
- f-strings are the best way to print variables: `f'Hello {name}'`
- Lists use `[]`, Dicts use `{}`
- `append()` adds to list, `remove()` deletes from list
- Dict `.items()` lets you loop through key-value pairs
- Always use `input()` for user input — it returns a string
- Convert types when needed: `int()`, `str()`, `float()`

## Git Commit
```bash
git add .
git commit -m "Day 16: Python basics variables lists dicts"
git push
```
