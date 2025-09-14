import unittest
from interconnect.quantum_internet import QuantumInternet

class TestQuantumInternet(unittest.TestCase):

    def setUp(self):
        """Initialize QuantumInternet before each test."""
        self.qi = QuantumInternet(firewall=None, persistence=None, crypto=None)

    def test_basic_initialization(self):
        """QuantumInternet must initialize with empty entanglement registry."""
        self.assertTrue(hasattr(self.qi, "entanglements"))
        self.assertEqual(self.qi.entanglements, {})

    def test_entangle_nodes(self):
        """Entangling two nodes should register them in entanglement registry."""
        self.qi.entangle("NodeA", "NodeB")
        self.assertIn("NodeA", self.qi.entanglements)
        self.assertEqual(self.qi.entanglements["NodeA"], "NodeB")

if __name__ == "__main__":
    unittest.main()
