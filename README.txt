BEWARE: This is not produciton software yet.
        I originally wrote this in 2011 and suddenly had use for
        it again and started to polish it. Look around and reuse
        if you'd like to experiment before I'm done.

proc_events
-----------

This package makes it possible to create event driven code around
process events such as new forks, process start and exit and ID
changes (UID, GID etc) on modern Linux systems.

How?
----
Linux kernels since 2.6.15 contains a userspace <-> kernelspace 
connector built on netlink sockets. This can be used by the kernel
to broadcast internal information to userspace, like process events
in our case. This exposes a possibility to know in near-realtime 
when a process starts, dies, forks, etc.

This package creates a netlink socket and tells the kernel to start
broadcasting process events. Either you use this socket manually,
or use the simple supplied callback loop.

What do I need?
---------------
You will need a Linux kernel of version 2.6.15 or higher to make use
of this package. To enable the process events connector, enable this
in the kernel:

 Device Drivers --->
   [*] Connector - unified userspace <-> kernelspace linker
     [*]   Report process events to userspace
		    

