import unittest


class Binary_tree():
    def __init__(self, data: str = None) -> None:
        self.__data: str = data
        self.__sides: dict = {'.': None, '-': None}

    def __eq__(self, rhs: object) -> bool:
        return self.__data == rhs

    def __getitem__(self, key: str):
        return self.__sides[key]

    def insert(self, data: str, encoding: str):
        if not encoding:
            return 1

        if self[encoding[0]]:
            return self[encoding[0]].insert(data, encoding[1:])

        if len(encoding) != 1:
            return 1

        self.__sides[encoding[0]] = Binary_tree(data)
        return 0

    def __str__(self) -> str:
        return (self.__data)

    def print(self, indent: int = 0) -> None:

        if self['.']:
            self['.'].print(indent+1)

        print("    "*indent, indent, self.__data)
        if self['-']:
            self['-'].print(indent+1)


class Morse():
    def __init__(self) -> None:
        self.__tree = Binary_tree("")

        self.__tree.insert('E', ".")
        self.__tree.insert('T', "-")

        self.__tree.insert('I', "..")
        self.__tree.insert('A', ".-")
        self.__tree.insert('N', "-.")
        self.__tree.insert('M', "--")

        self.__tree.insert('S', "...")
        self.__tree.insert('U', "..-")
        self.__tree.insert('R', ".-.")
        self.__tree.insert('W', ".--")
        self.__tree.insert('D', "-..")
        self.__tree.insert('K', "-.-")
        self.__tree.insert('G', "--.")
        self.__tree.insert('O', "---")

        self.__tree.insert('H', "....")
        self.__tree.insert('V', "...-")
        self.__tree.insert('F', "..-.")
        self.__tree.insert(' ', "..--")
        self.__tree.insert('L', ".-..")
        self.__tree.insert(' ', ".-.-")
        self.__tree.insert('P', ".--.")
        self.__tree.insert('J', ".---")
        self.__tree.insert('B', "-...")
        self.__tree.insert('X', "-..-")
        self.__tree.insert('C', "-.-.")
        self.__tree.insert('Y', "-.--")
        self.__tree.insert('Z', "--..")
        self.__tree.insert('Q', "--.-")
        self.__tree.insert(' ', "---.")
        self.__tree.insert(' ', "----")
                
        self.__tree.insert('5', ".....")
        self.__tree.insert('4', "....-")
        self.__tree.insert(' ', "...-.")
        self.__tree.insert('3', "...--")
        self.__tree.insert(' ', "..-..")
        self.__tree.insert('¿', "..-.-")
        self.__tree.insert('?', "..--.")
        self.__tree.insert('2', "..---")
        self.__tree.insert('&', ".-...")
        self.__tree.insert(' ', ".-..-")
        self.__tree.insert('+', ".-.-.")
        self.__tree.insert(' ', ".-.--")
        self.__tree.insert(' ', ".--..")
        self.__tree.insert(' ', ".--.-")
        self.__tree.insert(' ', ".---.")
        self.__tree.insert('1', ".----")
        self.__tree.insert('6', "-....")
        self.__tree.insert(' ', "-...-")
        self.__tree.insert(' ', "-..-.")
        self.__tree.insert(' ', "-..--")
        self.__tree.insert(' ', "-.-..")
        self.__tree.insert(' ', "-.-.-")
        self.__tree.insert('(', "-.--.")
        self.__tree.insert(' ', "-.---")
        self.__tree.insert('7', "--...")
        self.__tree.insert(' ', "--..-")
        self.__tree.insert(' ', "--.-.")
        self.__tree.insert(' ', "--.--")
        self.__tree.insert('8', "---..")
        self.__tree.insert(' ', "---.-")
        self.__tree.insert('9', "----.")
        self.__tree.insert('0', "-----")

        self.__tree.insert(' ', "......")
        self.__tree.insert(' ', ".....-")
        self.__tree.insert(' ', "....-.")
        self.__tree.insert(' ', "....--")
        self.__tree.insert(' ', "...-..")
        self.__tree.insert(' ', "...-.-")
        self.__tree.insert(' ', "...--.")
        self.__tree.insert(' ', "...---")
        self.__tree.insert(' ', "..-...")
        self.__tree.insert(' ', "..-..-")
        self.__tree.insert(' ', "..-.-.")
        self.__tree.insert(' ', "..-.--")
        self.__tree.insert(' ', "..--..")
        self.__tree.insert('_', "..--.-")
        self.__tree.insert(' ', "..---.")
        self.__tree.insert(' ', "..----")
        self.__tree.insert(' ', ".-....")
        self.__tree.insert(' ', ".-...-")
        self.__tree.insert('"', ".-..-.")
        self.__tree.insert(' ', ".-..--")
        self.__tree.insert(' ', ".-.-..")
        self.__tree.insert('.', ".-.-.-")
        self.__tree.insert(' ', ".-.--.")
        self.__tree.insert(' ', ".-.---")
        self.__tree.insert(' ', ".--...")
        self.__tree.insert(' ', ".--..-")
        self.__tree.insert(' ', ".--.-.")
        self.__tree.insert(' ', ".--.--")
        self.__tree.insert(' ', ".---..")
        self.__tree.insert(' ', ".---.-")
        self.__tree.insert("'", ".----.")
        self.__tree.insert(' ', ".-----")
        self.__tree.insert(' ', "-.....")
        self.__tree.insert('-', "-....-")
        self.__tree.insert(' ', "-...-.")
        self.__tree.insert(' ', "-...--")
        self.__tree.insert(' ', "-..-..")
        self.__tree.insert(' ', "-..-.-")
        self.__tree.insert(' ', "-..--.")
        self.__tree.insert(' ', "-..---")
        self.__tree.insert(' ', "-.-...")
        self.__tree.insert(' ', "-.-..-")
        self.__tree.insert(';', "-.-.-.")
        self.__tree.insert('!', "-.-.--")
        self.__tree.insert(' ', "-.--..")
        self.__tree.insert(')', "-.--.-")
        self.__tree.insert(' ', "-.---.")
        self.__tree.insert(' ', "-.----")
        self.__tree.insert(' ', "--....")
        self.__tree.insert('¡', "--...-")
        self.__tree.insert(' ', "--..-.")
        self.__tree.insert(' ', "--..--")
        self.__tree.insert(' ', "--.-..")
        self.__tree.insert(' ', "--.-.-")
        self.__tree.insert(' ', "--.--.")
        self.__tree.insert(' ', "--.---")
        self.__tree.insert(' ', "---...")
        self.__tree.insert(' ', "---..-")
        self.__tree.insert(' ', "---.-.")
        self.__tree.insert(' ', "---.--")
        self.__tree.insert(' ', "----..")
        self.__tree.insert(' ', "----.-")
        self.__tree.insert(' ', "-----.")
        self.__tree.insert(' ', "------")
        self.__tree.insert('$', "...-..-")


        self.__tree.print()

    def __get_morse_encoding(self, node, char, code) -> str:
        if not node:
            return ''
        elif node == char:
            return code

        for side in ['.', '-']:
            if x := self.__get_morse_encoding(node[side], char, side):
                code += x
                return code

    def encode(self, message: str) -> str:
        encoded_message: str = ''
        for char in message:
            encoded_message += self.__get_morse_encoding(
                self.__tree, char, '') + ' '
        return encoded_message[:-1]

    def __get_decoded_char(self, code: str) -> str:
        node = self.__tree

        while len(code) > 1:
            node = node[code[0]]

            code = code[1:]

        return str(node[code])

    def decode(self, message: str) -> str:
        decoded_message: str = ''
        for code in message.split(" "):
            decoded_message += self.__get_decoded_char(code)
        return decoded_message


class TestSum(unittest.TestCase):
    def test_encode_us(self):
        self.assertEqual(morse.encode("US"), "..- ...")

    def test_decode_us(self):
        self.assertEqual(morse.decode("..- ..."), "US")


morse = Morse()
unittest.main()
