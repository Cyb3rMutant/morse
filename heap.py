class Heap():
    def __init__(self, array) -> None:
        self.__array = array
        self.__sides: dict = {'.': (lambda i: 2*i+1),
                              '-': (lambda i: 2*i+2)}

    def find_elem(self, path) -> str:
        idx: int = 0
        while len(path):
            idx = self.__sides[path[0]](idx)
            path = path[1:]

        return str(self.__array[idx])

    def decode(self, message: str) -> str:
        decoded_message: str = ''
        for code in message.split(' '):
            if not code:
                continue
            if code == '/':
                decoded_message += ' '
                continue
            decoded_message += self.find_elem(code)
        return decoded_message
