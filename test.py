class TestNetwork( Topo ):
  "Single network topology"
  def _init_( self ):
      Topo._init_( self )
      #
      h1 = self.addHost( 'h1' )
      h2 = self.addHost( 'h2' )
      h3 = self.addHost( 'h3' )
      h4 = self.addHost( 'h4' )
      h5 = self.addHost( 'h5' )
      h6 = self.addHost( 'h6' )
      h7 = self.addHost( 'h7' )
      h8 = self.addHost( 'h8' )
      
      #
      s1 = self.addSwitch( 's1' )
      s2 = self.addSwitch( 's2' )
      s3 = self.addSwitch( 's3' )
      s4 = self.addSwitch( 's4' )
      
net = Mininet( topo=SingleSwitchTopo( 3 ) )
net.start()
CLI( net )
net.stop()
