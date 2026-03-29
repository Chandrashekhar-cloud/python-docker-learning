#!/usr/bin/env python3
name = input('Your name: ')
city = input('Your city: ')
skills = ['linux','docker','git','python','AWS']
server = {'hostname':'web1','ip':'192.168.1.1','port':8080,'status':'running'}
print(f'\n ==== PROFILE ====')
print(f'Name : {name}')
print(f'city : {city}')
print(f'skills : {skills}')
print(f'\n=== server ====')
for k,v in server.items():
	print(f' {k}:{v}')	
