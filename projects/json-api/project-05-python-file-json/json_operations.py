import json
with open("server.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(f"Hostname   :{data['hostname']}")
    print(f"Memory     :{data['ram']}")
    print(f"CPU        :{data['cpu']}")
    print(f"Status     :{data['status']}")
    print(f"OS         :{data['os']}")
    print(f"Environment:{data['environment']}")