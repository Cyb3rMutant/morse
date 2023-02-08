class Binary_tree():
    def __init__(self, data : str = None) -> None:
        self.__left : Binary_tree = None
        self.__data : str = data
        self.__right : Binary_tree = None

    def insert(self, data : str, encoding : str):
        print(encoding)
        if (encoding[0] == '.'):
            if self.__left:
                if not encoding:
                    return 1 
                return self.__left.insert(data, encoding[1:])

            if len(encoding) != 1:
                return 1 

            self.__left = Binary_tree(data)
            return 0

        elif (encoding[0] == '-'):
            if self.__right:
                if not encoding:
                    return 1 
                return self.__right.insert(data, encoding[1:])

            if len(encoding) != 1:
                return 1

            self.__right = Binary_tree(data)
            return 0

    def print(self, indent : int = 0) -> None:
        print("    "*indent, self.__data)

        if self.__left: self.__left.print(indent+1)

        if self.__right: self.__right.print(indent+1)

if __name__ == "__main__":
    x = Binary_tree("")
    print(x.insert('E', "."))
    print(x.insert('I', ".."))
    print(x.insert('S', "..."))
    print(x.insert('H', "...."))
    print(x.insert('A', ".-"))
    print(x.insert('R', ".-."))
    print(x.insert('L', ".-.."))
    print(x.insert('T', "-"))
    print(x.insert('M', "--"))
    print(x.insert('N', "-."))
    x.print()
