import unittest
from rgb_to_hex import Converter

class TestRGBtoHex (unittest.TestCase):
    def test_rgb_to_hex_01(self):
        value = Converter()
        result = "e9e9e9"
        self.assertEqual(result, value.rgb_to_hex((233, 233, 233)))
    
    def test_rgb_to_hex_02(self):
        value = Converter()
        result = "eaf3f3"
        self.assertEqual(result, value.rgb_to_hex((234, 243, 243)))

    def test_rgb_to_hex_03(self):
        value = Converter()
        result = "d58585"
        self.assertEqual(result, value.rgb_to_hex((213, 133, 133)))