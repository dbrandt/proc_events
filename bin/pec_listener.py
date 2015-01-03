import os
import errno
import struct
import socket
from select import select


from PEC import pec
from PEC import netlink
from PEC import connector
from PEC.pec import pec_control, pec_unpack

def hex_dump(data):
    """
    Print struct packed data in a way similar to 'x /Nbx <address>'
    in GDB.
    """
    for i in xrange(len(data)):
        print "0x%02x" % ord(data[i]),
        if i != 0 and not (i+1) % 8:
            print
        else:
            print "  ",
    print

s = socket.socket(socket.AF_NETLINK,
                  socket.SOCK_DGRAM,
                  netlink.NETLINK_CONNECTOR)

#  Netlink sockets are connected with pid and message group mask,
#  message groups are for multicast protocols (like our process event
#  connector).

try:
    s.bind((os.getpid(), connector.CN_IDX_PROC))
except socket.error, (_errno, errmsg):
    if _errno == errno.EPERM:
        print ("You don't have permission to bind to the "
               "process event connector. Try sudo.")
        raise SystemExit(1)
    raise

pec_control(s, listen=True)

while True:
    (readable, w, e) = select([s],[],[])
    buf = readable[0].recv(256)
    event = pec_unpack(buf)
    event["what"] = pec.pec_events_rev.get(event.what)
    print event

pec_control(s, listen=False)

s.close()

# todo:
# cn_msg parsing
# proc_event parsing
# explaining docs
# function separation
