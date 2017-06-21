import timeit
setup = '''
from novaclient import client
nova = client.Client(version='2.0', username='admin', password='secret', project_name='admin', auth_url='http://192.168.0.4/identity')
'''
task = '''
for i in range(1):
	nova.flavors.list()
'''
for i in range(20):
	print(timeit.timeit(task, setup, number=1))
