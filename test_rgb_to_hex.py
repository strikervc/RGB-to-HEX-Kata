import unittest
from rgb_to_hex import converter
class testRGBtoHEX (unittest.TestCase):
    def test_rgb_to_hex(self):
        value = converter()
        result = "7bff8e"
        self.assertEqual(result, value.rgb_to_hex((123, 255, 142)))