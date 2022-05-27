import os, requests
while(True):
  target = input("[STARTUP] - Enter Server Id:\n")
  server = requests.get(
    f"https://api.revolt.chat/servers/{target}/members",
    headers = {"x-session-token": os.environ['token']}
  )
  bots = 0
  members = 0
  for member in server.json()['users']:
    try:
      member['bot']
      try:
        requests.post(
          f"https://api.revolt.chat/bots/{member['_id']}/invite",
          headers={"x-session-token": os.environ['token']},
          json = {"server": "01G214R5HRG1Q21PYMGGXPQDVY"}
        )
        print(f"[VALID] - Added {member['username']}!")
        bots += 1
      except:
        print("[INVALID] - Bot is private or invalid!")
    except KeyError:
      members += 1
      print(f"[ERROR] - Didnt add {member['username']}.")
      pass
  print(f"[COMPLETED] - Iterated through a total of {bots + members} accounts.")
  print(f"[COMPLETED] - Added {bots} bots.")
  print(f"[COMPLETED] - Ignored {members} users.")
  input("[COMPLETED] - Press ENTER to continue / search another server.")
  os.system('cls' if os.name == 'nt' else 'clear')
  