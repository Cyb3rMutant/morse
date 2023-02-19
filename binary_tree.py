class Binary_tree():
    def __init__(self, data: str = None) -> None:
        self.__data: str = data
        self.__sides: dict = {'.': None, '-': None}

    def __eq__(self, rhs: object) -> bool:
        return self.__data == rhs

    def __getitem__(self, key: str):
        return self.__sides[key]

    def insert(self, data: str, encoding: str):
        if not encoding:  # make sure encoding is not NULL
            return 1

        if self[encoding[0]]:  # check if the upcoming side exists
            # move down the tree
            return self[encoding[0]].insert(data, encoding[1:])

        if len(encoding) != 1:  # make sure we havent reached the end of the list without reaching the end of encoding
            return 1

        self.__sides[encoding[0]] = Binary_tree(data)  # insert the new node
        return 0

    def __str__(self) -> str:
        return (self.__data)

    def print(self, indent: int = 0) -> None:  # print the tree in preorder form
        print("\t"*indent, indent, self.__data)

        if self['.']:
            self['.'].print(indent+1)

        if self['-']:
            self['-'].print(indent+1)
