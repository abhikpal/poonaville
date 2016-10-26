import unittest
import biennale

class BasicRoutesTestCase(unittest.TestCase):
    """
    Checks basic routes in the web app.
    """
    def setUp(self):
        self.app = biennale.app.test_client()

    def test_returns_controller_ui(self):
        raise NotImplementedError

    def test_returns_projection(self):
        raise NotImplementedError
