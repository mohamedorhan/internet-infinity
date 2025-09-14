import unittest
from internet_infinity import InternetInfinity

class TestSystem(unittest.TestCase):

    def setUp(self):
        """Initialize a fresh InternetInfinity system before each test."""
        self.system = InternetInfinity()

    def test_initialization(self):
        """System should initialize with at least one core layer (GreenNet)."""
        self.assertIn("GreenNet", self.system.layers)
        self.assertIsNotNone(self.system.greennet)

    def test_session_id_format(self):
        """Session ID must follow the expected format: YYYYMMDD_HHMMSS."""
        session_id = self.system.session_id
        self.assertRegex(session_id, r"^\d{8}_\d{6}$")

    def test_user_authentication_failure(self):
        """Login should fail with wrong credentials."""
        result = self.system.login("fake_user", "wrong_password")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
