import unittest
from rgb_to_hex import Converter

class TestRGBtoHex (unittest.TestCase):
    def test_rgb_to_hex(self):
        value = Converter()
        result = "e9e9e9"
        self.assertEqual(result, value.rgb_to_hex((233, 233, 233)))