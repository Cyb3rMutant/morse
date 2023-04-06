import unittest
from morse import morse
from binary_tree import bt
from datetime import datetime
import websockets
import json
import morse_server


class TestSum(unittest.TestCase):
    def test_001_bt_empty(self):
        self.assertTrue(bt.is_empty())

    def test_002_bt_insert_fail(self):
        self.assertNotEqual(bt.insert('A', ".-"), 1)

    def test_003_bt_insert_fail_empty(self):
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

    def test_016_morse_encode_empty(self):
        self.assertEqual(morse.encode(""), "")

    def test_017_morse_encode_fail_1(self):
        self.assertEqual(morse.encode("US"), "..-")

    def test_018_morse_encode_fail_2(self):
        self.assertEqual(morse.encode("U"), "..- ...")

    def test_019_morse_encode_lowercase(self):
        self.assertEqual(morse.encode("hello"), ".... . .-.. .-.. ---")

    def test_020_morse_encode_numbers(self):
        self.assertEqual(morse.encode("122"), ".---- ..--- ..---")

    def test_021_morse_encode_special_chars(self):
        self.assertEqual(morse.encode('.,?\'!()&:;+-_\"$¿¡'),
                         ".-.-.- --..-- ..--. .----. -.-.-- -.--. -.--.- .-... ---... -.-.-. .-.-. -....- ..--.- .-..-. ...-..- ..-.- --...-")

    def test_022_morse_encode_mixed(self):
        self.assertEqual(morse.encode("HeLLo123!"),
                         ".... . .-.. .-.. --- .---- ..--- ...-- -.-.--")

    def test_023_morse_encode_long_sentence(self):
        self.assertEqual(morse.encode("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"),
                         "- .... . / --.- ..- .. -.-. -.- / -... .-. --- .-- -. / ..-. --- -..- / .--- ..- -- .--. ... / --- ...- . .-. / - .... . / .-.. .- --.. -.-- / -.. --- --.")

    def test_024_morse_decode_us(self):
        self.assertEqual(morse.decode("..- ..."), "US")

    def test_025_morse_decode_hello(self):
        self.assertEqual(morse.decode(".... . .-.. .-.. ---"), "HELLO")

    def test_026_morse_decode_empty(self):
        self.assertEqual(morse.decode(""), "")

    def test_027_morse_decode_fail_1(self):
        self.assertEqual(morse.decode("..-"), "US")

    def test_028_morse_decode_fail_2(self):
        self.assertEqual(morse.decode("..- ..."), "U")

    def test_029_morse_decode_lowercase(self):
        self.assertEqual(morse.decode(".... . .-.. .-.. ---"), "HELLO")

    def test_030_morse_decode_numbers(self):
        self.assertEqual(morse.decode(".---- ..--- ...--"), "123")

    def test_031_morse_decode_special_chars(self):
        self.assertEqual(morse.decode(
            ".-.-.- --..-- ..--. .----. -.-.-- -.--. -.--.- .-... ---... -.-.-. .-.-. -....- ..--.- .-..-. ...-..- ..-.- --...-"), '.,?\'!()&:;+-_\"$¿¡')

    def test_032_morse_decode_long_sentence(self):
        self.assertEqual(morse.decode(
            "- .... . / --.- ..- .. -.-. -.- / -... .-. --- .-- -. / ..-. --- -..- / .--- ..- -- .--. ... / --- ...- . .-. / - .... . / .-.. .- --.. -.-- / -.. --- --."), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")

    def test_033_morse_heap_decode_us(self):
        self.assertEqual(morse.decode_heap("..- ..."), "US")

    def test_034_morse_heap_decode_hello(self):
        self.assertEqual(morse.decode_heap(".... . .-.. .-.. ---"), "HELLO")

    def test_035_morse_heap_decode_empty(self):
        self.assertEqual(morse.decode_heap(""), "")

    def test_036_morse_heap_decode_fail_1(self):
        self.assertEqual(morse.decode_heap("..-"), "US")

    def test_037_morse_heap_decode_fail_2(self):
        self.assertEqual(morse.decode_heap("..- ..."), "U")

    def test_038_morse_heap_decode_lowercase(self):
        self.assertEqual(morse.decode_heap(".... . .-.. .-.. ---"), "HELLO")

    def test_039_morse_heap_decode_numbers(self):
        self.assertEqual(morse.decode_heap(".---- ..--- ...--"), "123")

    def test_040_morse_heap_decode_special_chars(self):
        self.assertEqual(morse.decode_heap(
            ".-.-.- --..-- ..--. .----. -.-.-- -.--. -.--.- .-... ---... -.-.-. .-.-. -....- ..--.- .-..-. ...-..- ..-.- --...-"), '.,?\'!()&:;+-_\"$¿¡')

    def test_041_morse_heap_decode_long_sentence(self):
        self.assertEqual(morse.decode_heap(
            "- .... . / --.- ..- .. -.-. -.- / -... .-. --- .-- -. / ..-. --- -..- / .--- ..- -- .--. ... / --- ...- . .-. / - .... . / .-.. .- --.. -.-- / -.. --- --."), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")

    def test_042_morse_encode_ham_us(self):
        self.assertEqual(morse.encode_ham('S', 'R', "US"),
                         ".-. -.. . ... -...- ..- ... -...- -.--.")

    def test_043_morse_encode_ham_no_sendER(self):
        self.assertEqual(morse.encode_ham('', 'R', "HELLO"),
                         ".-. -.. . -...- .... . .-.. .-.. --- -...- -.--.")

    def test_044_morse_encode_ham_no_receIVER(self):
        self.assertEqual(morse.encode_ham('S', '', "HELLO"),
                         "-.. . ... -...- .... . .-.. .-.. --- -...- -.--.")

    def test_045_morse_encode_ham_numbers_AND_SPECIAL_CHAracters(self):
        self.assertEqual(morse.encode_ham('S1!', 'R7&', "1234567890.,?\'!()&:;+-_\"$¿¡"),
                         ".-. --... .-... -.. . ... .---- -.-.-- -...- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- .-.-.- --..-- ..--. .----. -.-.-- -.--. -.--.- .-... ---... -.-.-. .-.-. -....- ..--.- .-..-. ...-..- ..-.- --...- -...- -.--.")

    def test_046_morse_decode_ham_us(self):
        self.assertEqual(morse.decode_ham(
            ".-. -.. . ... -...- ..- ... -...- -.--."), ('S', 'R', "US"))

    def test_047_morse_decode_ham_no_sender(self):
        self.assertEqual(morse.decode_ham(
            ".-. -.. . -...- .... . .-.. .-.. --- -...- -.--."), ('', 'R', "HELLO"))

    def test_048_morse_decode_ham_no_receiver(self):
        self.assertEqual(morse.decode_ham(
            "-.. . ... -...- .... . .-.. .-.. --- -...- -.--."), ('S', '', "HELLO"))

    def test_049_morse_decode_ham_numbers_and_special_characters(self):
        self.assertEqual(morse.decode_ham(".-. --... .-... -.. . ... .---- -.-.-- -...- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- .-.-.- --..-- ..--. .----. -.-.-- -.--. -.--.- .-... ---... -.-.-. .-.-. -....- ..--.- .-..-. ...-..- ..-.- --...- -...- -.--."),
                         ('S1!', 'R7&', "1234567890.,?\'!()&:;+-_\"$¿¡"))


class TestAsync(unittest.IsolatedAsyncioTestCase):
    async def test_050_morse_server_echo(self):
        async with websockets.connect("ws://localhost:10102") as websocket:

            echo = await morse_server.echo(websocket, "test", "hi", json.loads(await websocket.recv())["client_id"])

            self.assertEqual(echo, ("ECHO", "TEST", "HI"))

    async def test_051_morse_server_time(self):
        async with websockets.connect("ws://localhost:10102") as websocket:

            time = await morse_server.time(websocket, "test", "hi", json.loads(await websocket.recv())["client_id"])

            self.assertEqual(
                time, ("TIME", "TEST", datetime.now().strftime("%H:%M:%S")))


unittest.main()
