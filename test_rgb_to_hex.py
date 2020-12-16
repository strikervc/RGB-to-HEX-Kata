import unittest
from rgb_to_hex import converter
class testRGBtoHEX (unittest.TestCase):
    def test_rgb_to_hex_01(self):
        value = converter()
        result = "7bff8e"
        self.assertEqual(result, value.rgb_to_hex((123, 255, 142)))

    def test_rgb_to_hex_02(self):
        value = converter()
        result = "86f584"
        self.assertEqual(result, value.rgb_to_hex((134, 245, 132)))    