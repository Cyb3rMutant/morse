class Binary_tree():
    def __init__(self, data : str = None) -> None:
        self.__data : str = data
        self.__sides : dict = {'.' : None, '-' : None}

    def insert(self, data : str, encoding : str):
        if not encoding:
            return 1 

        if self.__sides[encoding[0]]:
            return self.__sides[encoding[0]].insert(data, encoding[1:])

        if len(encoding) != 1:
            return 1 

        self.__sides[encoding[0]] = Binary_tree(data)
        return 0

    def print(self, indent : int = 0) -> None:
        print("    "*indent, self.__data)

        if self.__sides['.']: self.__sides['.'].print(indent+1)

        if self.__sides['-']: self.__sides['-'].print(indent+1)

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
