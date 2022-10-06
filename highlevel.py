from mininet.topo import Topo
from mininet.net import Mininet

class Network(Topo):
    "Single network topology"

    def __init__(self):
        Topo.__init__(self)

        # Hosts to add
        h1 = self.addHost("h1")
        h2 = self.addHost("h2")
        h3 = self.addHost("h3")
        h4 = self.addHost("h4")
        h5 = self.addHost("h5")
        h6 = self.addHost("h6")
        h7 = self.addHost("h7")
        h8 = self.addHost("h8")

        # Switchs to add
        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")
        s3 = self.addSwitch("s3")
        s4 = self.addSwitch("s4")

        # Links to add
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(h7, s3)
        self.addLink(h8, s3)
        self.addLink(s1, s3)
        self.addLink(s2, s3)
        self.addLink(s3, s4)

def testNetwork():
    net = Mininet(topo=Network())
    net.start()
    net.pingAll()
    net.stop()
    
if __name__ == '__main__':
    testNetwork()
