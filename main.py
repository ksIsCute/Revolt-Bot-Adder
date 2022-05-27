import os, requests, time
totalbots = 0
totalmembers = 0
start = input("[STARTUP] - Do you want to add multiple servers?\n")
starttime = time.time()
while(True):
  serverarray = []
  if start.lower() == "y":
    print("[STARTUP] - Alright, activating multiple server mode!")
    num = input("\n[STARTUP] - How many servers do you want to add?\n")
    for i in range(0, int(num)):
      server = input(f"\n[STARTUP] - Enter Server Id #{i + 1}:\n")
      if len(server) == len("01F80118K1F2EYD9XAMCPQ0BCT"):
        serverarray.append(server)
      else:
        print('Please enter a valid server ID!')
  else:
    print("\n[STARTUP] - Alright, lets stick to one shall we?")
    target = input("[STARTUP] - Enter Server Id:\n")
    if len(target) == 0:
      print('\033[31m' + "\nYou need to return a valid server id!")
      print('\033[39m')
      continue
    serverarray.append(target)
  bots = 0
  members = 0
  for i in serverarray:
    server = requests.get(
      f"https://api.revolt.chat/servers/{i}/members",
      headers = {"x-session-token": os.environ['token']}
    )
    for member in server.json()['users']:
      try:
        member['bot']
        try:
          requests.post(
            f"https://api.revolt.chat/bots/{member['_id']}/invite",
            headers={"x-session-token": os.environ['token']},
            json = {"server": "01G214R5HRG1Q21PYMGGXPQDVY"}
          )
          print(f"[VALID] - Added {member['username']}")
          bots += 1
          totalbots += 1
        except:
          print('\033[31m' + "[INVALID] - Bot is private or invalid!")
          print('\033[39m')
      except KeyError:
        members += 1
        totalmembers += 1
        try:
          fren = requests.put(f"https://api.revolt.chat/users/{member['username']}/friend", header={"x-session-token": os.environ['token']})
          if fren.json()['username']:
            print(f"[FRIENDING] - Added {fren.json()['username']}!")
          else:
            print('\033[31m' + f"[FRIENDING] - Couldn't send a friend request to {member['username']}!")
            print('\033[39m')
        except:
          print('\033[31m' + f"[FRIENDING] - Couldn't send a friend request to {member['username']}!")
          print('\033[39m')
    
        print('\033[31m' + f"[ERROR] - Didnt add {member['username']}.")
        print('\033[39m')
        pass
  print(f"[COMPLETED] - Completed in {round(time.time() - starttime, 2)}s")
  print(f"[COMPLETED] - Iterated through a total of {bots + members} accounts.")
  print(f"[COMPLETED] - Added {bots} bots.")
  print(f"[COMPLETED] - Ignored {members} users.")
  if bots + members < totalbots + totalmembers:
    print(f"[STATS] - You've searched through {totalbots + totalmembers} accounts this session!")
    print(f"[STATS] - Consisting of {totalbots} bots and {totalmembers} users!")
  input("[COMPLETED] - Press ENTER to continue / search another server.")
  os.system('cls' if os.name == 'nt' else 'clear')