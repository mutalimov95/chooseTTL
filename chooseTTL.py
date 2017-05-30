import os
import sys

ttl = 65

if sys.argv[1]:
    ttl = sys.argv

os.system('iptables -t mangle -A POSTROUTING -j TTL --ttl-set {}'.format(ttl))
sys.exit()
