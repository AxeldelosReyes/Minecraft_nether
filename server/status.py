import minestat
import threading
import os
import datetime
# Below is an example using the MineStat class.
# If server is offline, other instance members will be None.
ms = minestat.MineStat('play.zonecraft.es', 25565)

def print_status(ms):
  ms.check_status()
  cst = datetime.datetime.now()
  print('Minecraft server status of %s on port %d:' % (ms.address, ms.port))
  if ms.online:
    if ms.current_players == 0 and cst.hour <= 12:
      os.system("sudo stop.sh")
  else:
    if cst.hour >= 12:
      os.system("sudo open.sh")
  threading.Timer(10 , print_status ,args = (ms,)).start()

print_status(ms)

