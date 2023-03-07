from binary_tree import Binary_tree


class Morse():
    def __init__(self) -> None:
        self.__tree = Binary_tree()
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
        self.__tree.insert('\0', "..--")
        self.__tree.insert('L', ".-..")
        self.__tree.insert('\0', ".-.-")
        self.__tree.insert('P', ".--.")
        self.__tree.insert('J', ".---")
        self.__tree.insert('B', "-...")
        self.__tree.insert('X', "-..-")
        self.__tree.insert('C', "-.-.")
        self.__tree.insert('Y', "-.--")
        self.__tree.insert('Z', "--..")
        self.__tree.insert('Q', "--.-")
        self.__tree.insert('\0', "---.")
        self.__tree.insert('\0', "----")

        self.__tree.insert('5', ".....")
        self.__tree.insert('4', "....-")
        self.__tree.insert('\0', "...-.")
        self.__tree.insert('3', "...--")
        self.__tree.insert('\0', "..-..")
        self.__tree.insert('¿', "..-.-")
        self.__tree.insert('?', "..--.")
        self.__tree.insert('2', "..---")
        self.__tree.insert('&', ".-...")
        self.__tree.insert('\0', ".-..-")
        self.__tree.insert('+', ".-.-.")
        self.__tree.insert('\0', ".-.--")
        self.__tree.insert('\0', ".--..")
        self.__tree.insert('\0', ".--.-")
        self.__tree.insert('\0', ".---.")
        self.__tree.insert('1', ".----")
        self.__tree.insert('6', "-....")
        self.__tree.insert('=', "-...-")
        self.__tree.insert('\0', "-..-.")
        self.__tree.insert('\0', "-..--")
        self.__tree.insert('\0', "-.-..")
        self.__tree.insert('\0', "-.-.-")
        self.__tree.insert('(', "-.--.")
        self.__tree.insert('\0', "-.---")
        self.__tree.insert('7', "--...")
        self.__tree.insert('\0', "--..-")
        self.__tree.insert('\0', "--.-.")
        self.__tree.insert('\0', "--.--")
        self.__tree.insert('8', "---..")
        self.__tree.insert('\0', "---.-")
        self.__tree.insert('9', "----.")
        self.__tree.insert('0', "-----")

        self.__tree.insert('\0', "......")
        self.__tree.insert('\0', ".....-")
        self.__tree.insert('\0', "....-.")
        self.__tree.insert('\0', "....--")
        self.__tree.insert('\0', "...-..")
        self.__tree.insert('\0', "...-.-")
        self.__tree.insert('\0', "...--.")
        self.__tree.insert('\0', "...---")
        self.__tree.insert('\0', "..-...")
        self.__tree.insert('\0', "..-..-")
        self.__tree.insert('\0', "..-.-.")
        self.__tree.insert('\0', "..-.--")
        self.__tree.insert('\0', "..--..")
        self.__tree.insert('_', "..--.-")
        self.__tree.insert('\0', "..---.")
        self.__tree.insert('\0', "..----")
        self.__tree.insert('\0', ".-....")
        self.__tree.insert('\0', ".-...-")
        self.__tree.insert('"', ".-..-.")
        self.__tree.insert('\0', ".-..--")
        self.__tree.insert('\0', ".-.-..")
        self.__tree.insert('.', ".-.-.-")
        self.__tree.insert('\0', ".-.--.")
        self.__tree.insert('\0', ".-.---")
        self.__tree.insert('\0', ".--...")
        self.__tree.insert('\0', ".--..-")
        self.__tree.insert('\0', ".--.-.")
        self.__tree.insert('\0', ".--.--")
        self.__tree.insert('\0', ".---..")
        self.__tree.insert('\0', ".---.-")
        self.__tree.insert("'", ".----.")
        self.__tree.insert('\0', ".-----")
        self.__tree.insert('\0', "-.....")
        self.__tree.insert('-', "-....-")
        self.__tree.insert('\0', "-...-.")
        self.__tree.insert('\0', "-...--")
        self.__tree.insert('\0', "-..-..")
        self.__tree.insert('\0', "-..-.-")
        self.__tree.insert('\0', "-..--.")
        self.__tree.insert('\0', "-..---")
        self.__tree.insert('\0', "-.-...")
        self.__tree.insert('\0', "-.-..-")
        self.__tree.insert(';', "-.-.-.")
        self.__tree.insert('!', "-.-.--")
        self.__tree.insert('\0', "-.--..")
        self.__tree.insert(')', "-.--.-")
        self.__tree.insert('\0', "-.---.")
        self.__tree.insert('\0', "-.----")
        self.__tree.insert('\0', "--....")
        self.__tree.insert('¡', "--...-")
        self.__tree.insert('\0', "--..-.")
        self.__tree.insert('\0', "--..--")
        self.__tree.insert('\0', "--.-..")
        self.__tree.insert('\0', "--.-.-")
        self.__tree.insert('\0', "--.--.")
        self.__tree.insert('\0', "--.---")
        self.__tree.insert('\0', "---...")
        self.__tree.insert('\0', "---..-")
        self.__tree.insert('\0', "---.-.")
        self.__tree.insert('\0', "---.--")
        self.__tree.insert('\0', "----..")
        self.__tree.insert('\0', "----.-")
        self.__tree.insert('\0', "-----.")
        self.__tree.insert('\0', "------")

        self.__tree.insert('\0', ".......")
        self.__tree.insert('\0', "......-")
        self.__tree.insert('\0', ".....-.")
        self.__tree.insert('\0', ".....--")
        self.__tree.insert('\0', "....-..")
        self.__tree.insert('\0', "....-.-")
        self.__tree.insert('\0', "....--.")
        self.__tree.insert('\0', "....---")
        self.__tree.insert('\0', "...-...")
        self.__tree.insert('$', "...-..-")
        self.__tree.insert('\0', "...-.-.")
        self.__tree.insert('\0', "...-.--")
        self.__tree.insert('\0', "...--..")
        self.__tree.insert('\0', "...--.-")
        self.__tree.insert('\0', "...---.")
        self.__tree.insert('\0', "...----")
        self.__tree.insert('\0', "..-....")
        self.__tree.insert('\0', "..-...-")
        self.__tree.insert('\0', "..-..-.")
        self.__tree.insert('\0', "..-..--")
        self.__tree.insert('\0', "..-.-..")
        self.__tree.insert('\0', "..-.-.-")
        self.__tree.insert('\0', "..-.--.")
        self.__tree.insert('\0', "..-.---")
        self.__tree.insert('\0', "..--...")
        self.__tree.insert('\0', "..--..-")
        self.__tree.insert('\0', "..--.-.")
        self.__tree.insert('\0', "..--.--")
        self.__tree.insert('\0', "..---..")
        self.__tree.insert('\0', "..---.-")
        self.__tree.insert('\0', "..----.")
        self.__tree.insert('\0', "..-----")
        self.__tree.insert('\0', ".-.....")
        self.__tree.insert('\0', ".-....-")
        self.__tree.insert('\0', ".-...-.")
        self.__tree.insert('\0', ".-...--")
        self.__tree.insert('\0', ".-..-..")
        self.__tree.insert('\0', ".-..-.-")
        self.__tree.insert('\0', ".-..--.")
        self.__tree.insert('\0', ".-..---")
        self.__tree.insert('\0', ".-.-...")
        self.__tree.insert('\0', ".-.-..-")
        self.__tree.insert('\0', ".-.-.-.")
        self.__tree.insert('\0', ".-.-.--")
        self.__tree.insert('\0', ".-.--..")
        self.__tree.insert('\0', ".-.--.-")
        self.__tree.insert('\0', ".-.---.")
        self.__tree.insert('\0', ".-.----")
        self.__tree.insert('\0', ".--....")
        self.__tree.insert('\0', ".--...-")
        self.__tree.insert('\0', ".--..-.")
        self.__tree.insert('\0', ".--..--")
        self.__tree.insert('\0', ".--.-..")
        self.__tree.insert('\0', ".--.-.-")
        self.__tree.insert('\0', ".--.--.")
        self.__tree.insert('\0', ".--.---")
        self.__tree.insert('\0', ".---...")
        self.__tree.insert('\0', ".---..-")
        self.__tree.insert('\0', ".---.-.")
        self.__tree.insert('\0', ".---.--")
        self.__tree.insert('\0', ".----..")
        self.__tree.insert('\0', ".----.-")
        self.__tree.insert('\0', ".-----.")
        self.__tree.insert('\0', ".------")
        self.__tree.insert('\0', "-......")
        self.__tree.insert('\0', "-.....-")
        self.__tree.insert('\0', "-....-.")
        self.__tree.insert('\0', "-....--")
        self.__tree.insert('\0', "-...-..")
        self.__tree.insert('\0', "-...-.-")
        self.__tree.insert('\0', "-...--.")
        self.__tree.insert('\0', "-...---")
        self.__tree.insert('\0', "-..-...")
        self.__tree.insert('\0', "-..-..-")
        self.__tree.insert('\0', "-..-.-.")
        self.__tree.insert('\0', "-..-.--")
        self.__tree.insert('\0', "-..--..")
        self.__tree.insert('\0', "-..--.-")
        self.__tree.insert('\0', "-..---.")
        self.__tree.insert('\0', "-..----")
        self.__tree.insert('\0', "-.-....")
        self.__tree.insert('\0', "-.-...-")
        self.__tree.insert('\0', "-.-..-.")
        self.__tree.insert('\0', "-.-..--")
        self.__tree.insert('\0', "-.-.-..")
        self.__tree.insert('\0', "-.-.-.-")
        self.__tree.insert('\0', "-.-.--.")
        self.__tree.insert('\0', "-.-.---")
        self.__tree.insert('\0', "-.--...")
        self.__tree.insert('\0', "-.--..-")
        self.__tree.insert('\0', "-.--.-.")
        self.__tree.insert('\0', "-.--.--")
        self.__tree.insert('\0', "-.---..")
        self.__tree.insert('\0', "-.---.-")
        self.__tree.insert('\0', "-.----.")
        self.__tree.insert('\0', "-.-----")
        self.__tree.insert('\0', "--.....")
        self.__tree.insert('\0', "--....-")
        self.__tree.insert('\0', "--...-.")
        self.__tree.insert('\0', "--...--")
        self.__tree.insert('\0', "--..-..")
        self.__tree.insert('\0', "--..-.-")
        self.__tree.insert('\0', "--..--.")
        self.__tree.insert('\0', "--..---")
        self.__tree.insert('\0', "--.-...")
        self.__tree.insert('\0', "--.-..-")
        self.__tree.insert('\0', "--.-.-.")
        self.__tree.insert('\0', "--.-.--")
        self.__tree.insert('\0', "--.--..")
        self.__tree.insert('\0', "--.--.-")
        self.__tree.insert('\0', "--.---.")
        self.__tree.insert('\0', "--.----")
        self.__tree.insert('\0', "---....")
        self.__tree.insert('\0', "---...-")
        self.__tree.insert('\0', "---..-.")
        self.__tree.insert('\0', "---..--")
        self.__tree.insert('\0', "---.-..")
        self.__tree.insert('\0', "---.-.-")
        self.__tree.insert('\0', "---.--.")
        self.__tree.insert('\0', "---.---")
        self.__tree.insert('\0', "----...")
        self.__tree.insert('\0', "----..-")
        self.__tree.insert('\0', "----.-.")
        self.__tree.insert('\0', "----.--")
        self.__tree.insert('\0', "-----..")
        self.__tree.insert('\0', "-----.-")
        self.__tree.insert('\0', "------.")
        self.__tree.insert('\0', "-------")
        self.__tree.print()

    def encode(self, message: str) -> str:
        message = message.upper()
        encoded_message: str = ''
        for char in message:
            encoded_message += self.__tree.find_path(char) + ' '
        return encoded_message[:-1]

    def decode(self, message: str) -> str:
        decoded_message: str = ''
        for code in message.split(" "):
            if not code:
                continue
            decoded_message += self.__tree.find_elem(code)
        return decoded_message

    def encode_ham(self, sender: str, receiver: str, msg: str) -> str:
        return self.encode(f"{receiver}DE{sender}={msg}=(")

    def decode_ham(self, msg: str):
        msg = self.decode(msg)
        print(msg)
        de = msg.find("DE")
        eq = msg.find("=")
        print(de)
        print(eq)
        receiver = msg[:de]
        sender = msg[de+2:eq]
        msg = msg[eq+1:-2]
        return sender, receiver, msg

    def to_array(self):
        return self.__tree.to_array()


morse = Morse()
print(morse.encode_ham("s1", "r1", "hi"))
print(morse.decode_ham(".-. .---- -.. . ... .---- -...- .... .. -...- -.--."))
