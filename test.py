from mininet.node import Host, OVSSwitch(, Controller
from mininet.link import link

# A host is simply a Node.
h1 = Host( 'h1' ).setIP('10.0.0.1/24') # e1
h2 = Host( 'h2' ).setIP('10.0.0.2/24') # e1
h3 = Host( 'h3' ).setIP('10.0.0.3/24') # e2
h4 = Host( 'h4' ).setIP('10.0.0.4/24') # e2
h5 = Host( 'h5' ).setIP('10.0.0.5/24') # e3
h6 = Host( 'h6' ).setIP('10.0.0.6/24') # e3
h7 = Host( 'h7' ).setIP('10.0.0.7/24') # e4
h8 = Host( 'h8' ).setIP('10.0.0.8/24') # e4

# Edge switches
e1 = OVSSwitch( 'e1', inNamespace=False )
e2 = OVSSwitch( 'e2', inNamespace=False )
e3 = OVSSwitch( 'e3', inNamespace=False )
e4 = OVSSwitch( 'e4', inNamespace=False )

# Aggregation switches
a1 = OVSSwitch( 'e1', inNamespace=False )
a2 = OVSSwitch( 'e2', inNamespace=False )

# Core switch
c1 = OVSSwitch( 'c1', inNamespace=False )

# Links between hosts and edge switches
Link(h1,e1)
Link(h2,e1)
Link(h3,e2)
Link(h4,e2)
Link(h5,e3)
Link(h6,e3)
Link(h7,e4)
Link(h8,e8)

# Links between edge switches and
# aggregation switches
Link(e1,a1)
Link(e2,a1)
Link(e3,a2)
Link(e4,a2)

# Link between aggregation switches
# and core switch
Link(a1,c1)
Link(a2,c1)

# Start up a new OVS OpenFlow switches
e1.start()
e2.start()
e3.start()
e4.start()
a1.start()
a2.start()
c1.start()

# Test of reachability
print(h1.cmd('ping -h8'))

# Stop the OVS OpenFlow switches
e1.stop()
e2.stop()
e3.stop()
e4.stop()
a1.stop()
a2.stop()
c1.stop()
