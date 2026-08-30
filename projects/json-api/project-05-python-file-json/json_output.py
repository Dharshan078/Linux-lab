import json
server = {
    "hostname": "web-server-01",
    "environment": "production",
    "status": "running",
    "cpu": 45,
    "memory": 62
}
with open ("output.json","w") as file:
    json.dump(server, file, indent=4)