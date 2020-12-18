import unittest
from rgb_to_hex import converter
class testCases (unittest.TestCase):
    def test_rgb_to_hex_01(self):
        value = converter()
        result = "6f6f6f"
        self.assertEqual(result, value.rgb_to_hex((111, 111, 111)))
    
    def test_rgb_to_hex_02(self):
        value = converter()
        result = "de6fde"
        self.assertEqual(result, value.rgb_to_hex((222, 111, 222)))
    
    def test_rgb_to_hex_03(self):
        value = converter()
        result = "7a6f7a"
        self.assertEqual(result, value.rgb_to_hex((122, 111, 122)))