import json

with open ("lista.json","r") as arch:
    campers = json.load(arch)

print (json.dumps(campers, indent=4))