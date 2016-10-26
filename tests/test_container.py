import unittest
from biennale.container import Container

class ContainerSetUpTestCase(unittest.TestCase):
    def test_timeout_setting(self):
        c = Container(timeout=120)
        assertEqual(c.get_timeout(), 120)

    def test_timeout_defaut(self):
        c = Container()
        assert(c.get_timeout(), 60)

class ContainerModifyTestCase(unittest.TestCase):
    def setUp(self):
        pass
