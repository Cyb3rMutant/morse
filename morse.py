from binary_tree import Binary_tree


class Morse(Binary_tree):
    def __init__(self, data: str = None) -> None:
        super().__init__(data)

        self.insert('E', ".")
        self.insert('T', "-")

        self.insert('I', "..")
        self.insert('A', ".-")
        self.insert('N', "-.")
        self.insert('M', "--")

        self.insert('S', "...")
        self.insert('U', "..-")
        self.insert('R', ".-.")
        self.insert('W', ".--")
        self.insert('D', "-..")
        self.insert('K', "-.-")
        self.insert('G', "--.")
        self.insert('O', "---")

        self.insert('H', "....")
        self.insert('V', "...-")
        self.insert('F', "..-.")
        self.insert(' ', "..--")
        self.insert('L', ".-..")
        self.insert(' ', ".-.-")
        self.insert('P', ".--.")
        self.insert('J', ".---")
        self.insert('B', "-...")
        self.insert('X', "-..-")
        self.insert('C', "-.-.")
        self.insert('Y', "-.--")
        self.insert('Z', "--..")
        self.insert('Q', "--.-")
        self.insert(' ', "---.")
        self.insert(' ', "----")

        self.insert('5', ".....")
        self.insert('4', "....-")
        self.insert(' ', "...-.")
        self.insert('3', "...--")
        self.insert('¿', "..-.-")
        self.insert('?', "..--.")
        self.insert('2', "..---")
        self.insert('&', ".-...")
        self.insert(' ', ".-..-")
        self.insert('+', ".-.-.")
        self.insert('1', ".----")
        self.insert('6', "-....")
        self.insert('(', "-.--.")
        self.insert('7', "--...")
        self.insert('8', "---..")
        self.insert('9', "----.")
        self.insert('0', "-----")

        self.insert(' ', "...-..")
        self.insert('_', "..--.-")
        self.insert('"', ".-..-.")
        self.insert("'", ".----.")
        self.insert('-', "-....-")
        self.insert(';', "-.-.-.")
        self.insert('!', "-.-.--")
        self.insert(')', "-.--.-")
        self.insert('¡', "--...-")

        self.insert('$', "...-..-")

        self.print()

    def encode(self, message: str) -> str:
        encoded_message: str = ''
        for char in message:
            encoded_message += self.find_path(char) + ' '
        return encoded_message[:-1]

    def decode(self, message: str) -> str:
        decoded_message: str = ''
        for code in message.split(" "):
            decoded_message += self.find_elem(code)
        return decoded_message


morse = Morse()
