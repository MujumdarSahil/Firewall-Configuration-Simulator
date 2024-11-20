import unittest
from app.firewall import Firewall

class TestFirewall(unittest.TestCase):
    def setUp(self):
        self.firewall = Firewall()

    def test_add_rule(self):
        self.firewall.add_rule("ALLOW ALL")
        self.assertEqual(self.firewall.get_rules(), ["ALLOW ALL"])

    def test_delete_rule(self):
        self.firewall.add_rule("ALLOW ALL")
        self.firewall.delete_rule(0)
        self.assertEqual(self.firewall.get_rules(), [])
