
from netaddr import *
import pings
from collections import namedtuple

def test_peer(ip,host,broad):
    pos=0
    #r=namedtuple(pos,'IP Name Status')
    p=pings.Ping()
    p=p.ping(str(ip),times=1)
    if p.is_reached() == True and ip != host and ip != broad:
        r = namedtuple('num','IP Name Status')
        new = r(IP=str(ip),Name=IPAddress(str(ip)).reverse_dns,Status='Online')
        print('{0.IP:<20s} {0.Name:^30s} {0.Status:>10s}'.format(new))
        pos += 1

if __name__=="__main__":

    p = input('Enter a network IP with CDR notation: ')
    p=IPNetwork(str(p))
    net = p.network
    broad=p.broadcast
    ip = IPSet([IPNetwork(str(p))])
    for i in ip:
        test_peer(i,net,broad)







