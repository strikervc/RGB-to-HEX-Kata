import unittest
from rgb_to_hex import converter
class testCases (unittest.TestCase):
    def test_rgb_to_hex_01(self):
        value = converter()
        result = "6f6f6f"
        self.assertEqual(result, value.rgb_to_hex((111, 111, 111)))