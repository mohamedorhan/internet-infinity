import unittest
from interconnect.greennet import GreenNet

class TestGreenNet(unittest.TestCase):

    def setUp(self):
        """Initialize GreenNet before each test."""
        self.gn = GreenNet()

    def test_add_route(self):
        """Adding a route should store it in routes dictionary."""
        self.gn.add_route("Node1", "192.168.1.1")
        self.assertIn("Node1", self.gn.get_routes())

    def test_send_packet_success(self):
        """Sending a packet to a known node should return True."""
        self.gn.add_route("Node2", "192.168.1.2")
        result = self.gn.send_packet("Node2", "Hello Internet ∞")
        self.assertTrue(result)

    def test_send_packet_failure(self):
        """Sending a packet to an unknown node should fail."""
        result = self.gn.send_packet("UnknownNode", "TestData")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
