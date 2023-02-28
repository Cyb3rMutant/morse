import unittest
from morse import morse
from binary_tree import bt


class TestSum(unittest.TestCase):
    def test_001_bt_empty(self):
        self.assertTrue(bt.is_empty())

    def test_002_bt_insert_fail(self):
        self.assertNotEqual(bt.insert('A', ".-"), 1)

    def test_003_bt_insert_fail_emptu(self):
        self.assertNotEqual(bt.insert('E', ""), 1)

    def test_004_bt_insert(self):
        self.assertEqual(bt.insert('E', "."), 0)

    def test_005_bt_insert_level_2(self):
        self.assertEqual(bt.insert('A', ".-"), 0)

    def test_006_bt_find_elem(self):
        self.assertEqual(bt.find_elem("."), "E")

    def test_007_bt_find_elem_no_elem(self):
        self.assertEqual(bt.find_elem(".-."), "None")

    def test_008_bt_find_path(self):
        self.assertEqual(bt.find_path("A"), ".-")

    def test_009_bt_find_path_not_path(self):
        self.assertEqual(bt.find_path("I"), "")

    def test_010_bt_empty_fail(self):
        self.assertTrue(bt.is_empty())

    def test_011_bt_delete(self):
        self.assertEqual(bt.delete("E"), None)

    def test_012_bt_empty(self):
        self.assertTrue(bt.is_empty())

    def test_013_bt_delete_empty(self):
        self.assertEqual(bt.delete("E"), None)

    def test_014_morse_encode_us(self):
        self.assertEqual(morse.encode("US"), "..- ...")

    def test_015_morse_encode_hello(self):
        self.assertEqual(morse.encode("HELLO"), ".... . .-.. .-.. ---")

    def test_016_morse_encode_(self):
        self.assertEqual(morse.encode(""), "")

    def test_017_morse_encode_fail_1(self):
        self.assertEqual(morse.encode("US"), "..-")

    def test_018_morse_encode_fail_2(self):
        self.assertEqual(morse.encode("U"), "..- ...")

    def test_019_morse_decode_us(self):
        self.assertEqual(morse.decode("..- ..."), "US")

    def test_020_morse_decode_hello(self):
        self.assertEqual(morse.decode(".... . .-.. .-.. ---"), "HELLO")

    def test_021_morse_decode_(self):
        self.assertEqual(morse.decode(""), "")

    def test_022_morse_decode_fail_1(self):
        self.assertEqual(morse.decode("..-"), "US")

    def test_023_morse_decode_fail_2(self):
        self.assertEqual(morse.decode("..- ..."), "U")


unittest.main()