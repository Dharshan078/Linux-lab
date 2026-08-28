import json
try:
   with open("servers.json","r") as file:
      data = json.load(file)
      total = 0
      run = 0
      stop_list = []
      for server in data:
         print(f"\nServer       :{server}")
         server_data = data[server]
         print(f"Hostname     :{server_data['hostname']}")
         print(f"Environment  :{server_data['environment']}")
         print(f"Status       :{server_data['status']}")
         print(f"CPU Usage    :{server_data['cpu']}%")
         print(f"Memory Usage :{server_data['memory']}%")
         total += 1
         status = server_data['status']
         if status == 'running':
            run += 1
         else:
            stop_list.append(server_data['hostname'])

      print(f"\nTotal Servers  :  {total}")
      print(f"Running Servers:  {run}")
      for stop_server in stop_list:
         print(f"\nStopped Servers: \n{stop_server}")
except FileNotFoundError:
   print("Error: servers.json could not be found.")
except json.JSONDecodeError:
   print("Error: Invalid JSON format.")
except:
    print("Something went wrong")
