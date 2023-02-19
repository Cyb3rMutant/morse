import unittest
from morse import morse


class TestSum(unittest.TestCase):
    def test_encode_us(self):
        self.assertEqual(morse.encode("US"), "..- ...")

    def test_encode_us(self):
        self.assertEqual(morse.encode("HELLO"), ".... . .-.. .-.. ---")

    def test_encode_us(self):
        self.assertEqual(morse.encode(""), "")

    def test_encode_us(self):
        self.assertEqual(morse.encode("US"), "..-")

    def test_encode_us(self):
        self.assertEqual(morse.encode("U"), "..- ...")

    def test_decode_us(self):
        self.assertEqual(morse.decode(".... . .-.. .-.. ---"), "HELLO")

    def test_decode_us(self):
        self.assertEqual(morse.decode(""), "")

    def test_decode_us(self):
        self.assertEqual(morse.decode("..- ..."), "US")

    def test_decode_us(self):
        self.assertEqual(morse.decode("..-"), "US")

    def test_decode_us(self):
        self.assertEqual(morse.decode("..- ..."), "U")


unittest.main()
