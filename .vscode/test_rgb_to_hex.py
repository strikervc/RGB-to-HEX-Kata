import unittest
from rgb_to_hex import converter
class testCases (unittest.TestCase):
    def test_rgb_to_hex_01(self):
        value = converter()
        result = "e9e9e9"
        self.assertEqual(result, value.rgb_to_hex((233, 233, 233)))