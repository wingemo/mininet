from mininet.node import Host, OVSSwitch, Controller
from mininet.link import Link

# A host is simply a Node.
h1 = Host("h1")
h2 = Host("h2")
h3 = Host("h3")
h4 = Host("h4")
h5 = Host("h5")
h6 = Host("h6")
h7 = Host("h7")
h8 = Host("h8")

list_host = [h1, h2, h3, h4, h5, h6, h7, h8]

# Edge switches
e1 = OVSSwitch("e1", inNamespace=False)
e2 = OVSSwitch("e2", inNamespace=False)
e3 = OVSSwitch("e3", inNamespace=False)
e4 = OVSSwitch("e4", inNamespace=False)

# Aggregation switches
a1 = OVSSwitch("a1", inNamespace=False)
a2 = OVSSwitch("a2", inNamespace=False)

# Core switch
c1 = OVSSwitch("c1", inNamespace=False)

# Core switch
ct = Controller("ct", inNamespace=False)

# Links between edge switches and
# aggregation switches
Link(e1, a1)
Link(e2, a1)
Link(e3, a2)
Link(e4, a2)

# Link between aggregation switches
# and core switch
Link(a1, c1)
Link(a2, c1)

# Links between hosts and edge switches
Link(h1, e1)
Link(h2, e1)
Link(h3, e2)
Link(h4, e2)
Link(h5, e3)
Link(h6, e3)
Link(h7, e4)
Link(h8, e4)

# # Set the IP address for the interface
h1.setIP("10.0.0.1/24")
h2.setIP("10.0.0.2/24")
h3.setIP("10.0.0.3/24")
h4.setIP("10.0.0.4/24")
h5.setIP("10.0.0.5/24")
h6.setIP("10.0.0.6/24")
h7.setIP("10.0.0.7/24")
h8.setIP("10.0.0.8/24")

# Start up controller
ct.start()

# Start up a new OVS OpenFlow switches
e1.start([ct])
e2.start([ct])
e3.start([ct])
e4.start([ct])
a1.start([ct])
a2.start([ct])
c1.start([ct])

# Test of reachability
for host in list_host:
    for reciver in list_host:
        if host != reciver:
            print(host.cmd("ping -c3", reciver.IP()))

# Stop the OVS OpenFlow switches
e1.stop()
e2.stop()
e3.stop()
e4.stop()
a1.stop()
a2.stop()
c1.stop()
