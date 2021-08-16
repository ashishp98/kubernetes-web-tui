#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
y = mydata.getvalue("cmd").lower()

# Get Pods
if ('list' in y or 'show' in y or 'get' in y) and ('pod' in y or 'pods' in y):    
    cmd = "sudo kubectl get pods"
    print("COMMAND IS : " +cmd)
    print()
    print("OUTPUT >>> ")
    output = subprocess.getoutput(cmd)
    print(output)

# Get all resourses
elif ('list' in y or 'show' in y or 'get' in y) and ('every' in y or 'all' in y) and ('resources' in y or 'resource' in y):    
    cmd = "sudo kubectl get all"
    print("COMMAND IS : " +cmd)
    print()
    print("OUTPUT >>> ")
    output = subprocess.getoutput(cmd)
    print(output)

# Launch Pod
elif ('run' in y or 'create' in y or 'launch' in y) and ('pod' in y or 'pods' in y) and ('image' in y):
    str = y.split()
    if 'pod' in str:
        i = str.index(('pod')) + 1
    elif 'pods' in str:
        i = str.index('pods') + 1
    j = str.index('image') + 1
    cmd = "sudo kubectl run {0} --image={1}".format(str[i], str[j])
    print("COMMAND IS : " +cmd)
    print()
    print("OUTPUT >>> ")
    output = subprocess.getoutput(cmd)
    print(output)

# Launch Deployment
elif ('deployment' in y or 'deploy' in y) and ('create' in y or 'launch' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    j = str.index('image') + 1
    cmd = "sudo kubectl create deployment {0} --image={1}".format(str[i], str[j])
    print("COMMAND IS : " +cmd)
    print()
    print("OUTPUT >>> ")

    output = subprocess.getoutput(cmd)
    print(output)

# Expose deployment
elif ('deployment' in y or 'deploy' in y) and ('expose' in y or 'service' in y or 'services' in y) and ('port' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    port = str.index('port') + 1
    cmd = "sudo kubectl expose deployment {0} --port={1} --type=NodePort".format(str[i], str[port])
    print("COMMAND IS : " +cmd)
    print()
    print("OUTPUT >>> ")

    output = subprocess.getoutput(cmd)
    print(output)

# Scale deployment
elif ('deployment' in y or 'deploy' in y) and ('scale' in y or 'replica' in y or 'replicas' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index('deployment') + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    j = str.index('to') + 1
    cmd = "sudo kubectl scale deployment {0} --replicas={1}".format(str[i], str[j])
    print("COMMAND IS : " +cmd)
    print()
    print("OUTPUT >>> ")

    output = subprocess.getoutput(cmd)
    print(output)

# Delete deployment
elif ('deployment' in y or 'deploy' in y) and ('delete' in y or 'remove' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    cmd = "sudo kubectl delete deployment {}".format(str[i])
    print("COMMAND IS : " +cmd)
    print()
    print("OUTPUT >>> ")

    output = subprocess.getoutput(cmd)
    print(output)

# Get all deployment
elif ('list' in y or 'show' in y or 'get' in y) and ('every' in y or 'all' in y) and ('deploy' in y or 'deployment' in y):    
    cmd = "sudo kubectl get deployment"
    output = subprocess.getoutput(cmd)
    print(output)

# List Services
elif ('list' in y or 'show' in y or 'get' in y) and ('svc' in y or 'services' in y or 'service' in y):    
    cmd = "sudo kubectl get svc"
    print("COMMAND IS : " +cmd)
    print()
    print("OUTPUT >>> ")

    output = subprocess.getoutput(cmd)
    print(output)

# Delete Service
elif ('deployment' in y or 'deploy' in y) and ('expose' in y or 'service' in y or 'services' in y) and ('delete' in y or 'remove' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    cmd = "sudo kubectl delete svc {}".format(str[i])
    print("COMMAND IS : " +cmd)
    print()
    print("OUTPUT >>> ")

    output = subprocess.getoutput(cmd)
    print(output)

# delete all resourses
elif ('delete' in y or 'terminate' in y) and ('every' in y or 'all' in y) and ('resources' in y or 'resource' in y):    
    cmd = "sudo kubectl delete all --all"
    print("COMMAND IS : " +cmd)
    print()
    print("OUTPUT >>> ")

    output = subprocess.getoutput(cmd)
    print(output)

else:
    print("Please enter right requirement !!")
