import os, requests, time
totalbots = 0
totalmembers = 0
start = input("[STARTUP] - Do you want to add multiple servers?\n")
starttime = time.time()
while(True):
  serverarray = []
  if start.lower() == "y":
    print("[STARTUP] - Alright, activating multiple server mode!")
    num = input("\n[STARTUP] - How many servers do you want to scrape?\n")
    for i in range(0, int(num)):
      server = input(f"\n[STARTUP] - Enter Server Id #{i + 1}:\n")
      if len(server) == len("01F80118K1F2EYD9XAMCPQ0BCT"):
        serverarray.append(server)
        serverinfo = requests.get(
          f"https://api.revolt.chat/servers/{server}",
          headers = {"x-session-token": os.environ['token']}
        )
        print(f"[STARTUP] - Added {serverinfo.json()['name']} to your serverlist.")
        time.sleep(2)
      else:
        print('[STARTUP] - Please enter a valid server ID!')
  else:
    print("\n[STARTUP] - Alright, lets stick to one shall we?")
    target = input("[STARTUP] - Enter Server Id:\n")
    if len(target) == 0:
      print('\033[31m' + "\nYou need to return a valid server id!")
      print('\033[39m')
      continue
    serverarray.append(target)
    serverinfo = requests.get(
      f"https://api.revolt.chat/servers/{target}",
      headers = {"x-session-token": os.environ['token']}
    )
    print(f"[STARTUP] - Scraping bots from {serverinfo.json()['name']}\n")
  bots = 0
  members = 0
  chosenserver = input("[STARTUP] - Please enter the server ID to add the found bots into:\n")
  serverinfo = requests.get(
      f"https://api.revolt.chat/servers/{chosenserver}",
      headers = {"x-session-token": os.environ['token']}
  )
  print(f"[STARTUP] - Adding bots to {serverinfo.json()['name']}\n")
  time.sleep(2)
  for i in serverarray:
    server = requests.get(
      f"https://api.revolt.chat/servers/{i}/members",
      headers = {"x-session-token": os.environ['token']}
    )
    for member in server.json()['users']:
      try:
        print(member['bot'])
        try:
          requests.post(
            f"https://api.revolt.chat/bots/{member['_id']}/invite",
            headers={"x-session-token": os.environ['token']},
            json = {"server": chosenserver}
          )
          print(f"[VALID] - Added {member['username']} to the server")
          bots += 1
          totalbots += 1
        except:
          print('\033[31m' + "[INVALID] - Bot is private or invalid!")
          print('\033[39m')
      except KeyError:
        members += 1
        totalmembers += 1
        
        print('\033[31m' + f"[ERROR] - Didnt add {member['username']} to the server.")
        print('\033[39m')
        pass
  print(f"[STATS] - Completed in {round(time.time() - starttime, 2)}s")
  print(f"[STATS] - Iterated through a total of {bots + members} accounts.")
  print(f"[STATS] - Added {bots} bots.")
  print(f"[STATS] - Ignored {members} users.")
  if bots + members < totalbots + totalmembers:
    print(f"[STATS] - You've searched through {totalbots + totalmembers} accounts this session!")
    print(f"[STATS] - Consisting of {totalbots} bots and {totalmembers} users!")
  input("[COMPLETED] - Press ENTER to continue / search another server.")
  os.system('cls' if os.name == 'nt' else 'clear')