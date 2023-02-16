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
        print("    "*indent, indent, self.__data)

        if self['.']:
            self['.'].print(indent+1)

        if self['-']:
            self['-'].print(indent+1)


class Morse():
    def __init__(self, tree) -> None:
        self.__tree = tree

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
            print(code, self.__tree)

            node = node[code[0]]

            code = code[1:]

        return str(node[code])

    def decode(self, message: str) -> str:
        decoded_message: str = ''
        for code in message.split(" "):
            decoded_message += self.__get_decoded_char(code)
        return decoded_message


if __name__ == "__main__":
    x = Binary_tree("")

    print(x.insert('E', "."))
    print(x.insert('T', "-"))

    print(x.insert('I', ".."))
    print(x.insert('A', ".-"))
    print(x.insert('N', "-."))
    print(x.insert('M', "--"))

    print(x.insert('S', "..."))
    print(x.insert('U', "..-"))
    print(x.insert('R', ".-."))
    print(x.insert('W', ".--"))
    print(x.insert('D', "-.."))
    print(x.insert('K', "-.-"))
    print(x.insert('G', "--."))
    print(x.insert('O', "---"))

    print(x.insert('H', "...."))
    print(x.insert('V', "...-"))
    print(x.insert('F', "..-."))
    print(x.insert('L', ".-.."))
    print(x.insert('P', ".--."))
    print(x.insert('J', ".---"))
    print(x.insert('B', "-..."))
    print(x.insert('X', "-..-"))
    print(x.insert('C', "-.-."))
    print(x.insert('Y', "-.--"))
    print(x.insert('Z', "--.."))
    print(x.insert('Q', "--.-"))

    x.print()
    print("\n\n\n")
    y = Morse(x)
    print(y.decode("... --- -- . - .... .. -. --."))
