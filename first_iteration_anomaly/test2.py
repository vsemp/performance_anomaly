from novaclient import client
nova = client.Client(version='2.0', username='admin', password='secret', project_name='admin', auth_url='http://192.168.0.4/identity')

from time import time
for i in range(1):
        start=time()
        nova.flavors.list()
        print(time()-start)
