import os
import sys

if sys.argv[1]:
  ttl = sys.argv
else:
  ttl = 65

os.system('sudo iptables -t mangle -A POSTROUTING -j TTL --ttl-set {}'.format(ttl))
sys.exit()
