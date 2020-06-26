import minestat
import threading
import os
import datetime
# Below is an example using the MineStat class.
# If server is offline, other instance members will be None.
ms = minestat.MineStat('34.70.21.148', 25565)

def print_status(ms):
  ms.check_status()
  cst = datetime.datetime.now()
  print('Minecraft server status of %s on port %d:' % (ms.address, ms.port))
  print('Minecraft server status is %s' % (ms.online))
  if ms.online:
    if ms.current_players == 0 and cst.hour <= 12:
      print('Minecraft server is closing')
      os.system("sudo ./stop.sh")
  else:
    if cst.hour >= 12:
      print('Minecraft server is starting')
      os.system("sudo ./open.sh")
  threading.Timer(30 , print_status ,args = (ms,)).start()

print_status(ms)

