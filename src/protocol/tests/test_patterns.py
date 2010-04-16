import unittest

class ParseTest(unittest.TestCase):
    def setUp(self):
        from ..patterns import parser
        self.parser = parser

    def test_empty(self):
        from ..messages import Empty
        message = self.parser("")
        self.assertTrue(isinstance(message, Empty))

    def test_registration(self):
        from ..messages import Registration
        message = self.parser("+register bob user")
        self.assertTrue(isinstance(message, Registration))

    def test_vht_signup(self):
        from ..messages import HealthWorkerSignup
        message = self.parser("+vht 123")
        self.assertTrue(isinstance(message, HealthWorkerSignup))
        from ..models import GROUPS
        self.assertEqual(message.group, GROUPS['VHT'])

    def test_hcw_signup(self):
        from ..messages import HealthWorkerSignup
        message = self.parser("+hcw 123")
        self.assertTrue(isinstance(message, HealthWorkerSignup))
        from ..models import GROUPS
        self.assertEqual(message.group, GROUPS['HCW'])
