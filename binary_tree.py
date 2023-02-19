class Binary_tree():
    def __init__(self, data: str = None) -> None:
        self.__data: str = data
        self.__sides: dict = {'.': None, '-': None}

    def __eq__(self, rhs: object) -> bool:
        return self.__data == rhs

    def __getitem__(self, key: str):
        return self.__sides[key]

    def __str__(self) -> str:
        return str(self.__data)

    def is_empty(self)->bool:
        for node in self.__sides.values():
            if node:
                return False
        return not self.__data

    def insert(self, data: str, encoding: str) -> int:
        if not encoding:  # make sure encoding is not NULL
            return 1

        if self[encoding[0]]:  # check if the upcoming side exists
            # move down the tree
            return self[encoding[0]].insert(data, encoding[1:])

        if len(encoding) != 1:  # make sure we havent reached the end of the list without reaching the end of encoding
            return 1

        self.__sides[encoding[0]] = Binary_tree(data)  # insert the new node
        return 0

    def delete(self, data) -> None:
        for s, node in self.__sides.items():
            if node == data:
                self.__sides[s] = None
                break
            elif not node:
                continue
            node.delete(data)

    def find_path(self, elem: str, side: str = '') -> str:
        if self == elem:
            return side

        for s, node in self.__sides.items():
            if not node:
                continue

            if x := node.find_path(elem, s):
                return side + x
        return ''

    def find_elem(self, path: str) -> str:
        node = self

        while len(path) > 1:
            node = node[path[0]]

            path = path[1:]

        return str(node[path])

    def print(self, indent: int = 0) -> None:  # print the tree in preorder form
        print("\t"*indent, indent, self.__data)

        for node in self.__sides.values():
            if node:
                node.print(indent+1)

    def __del__(self) -> None:
        print("item %s deleted", self)


x = Binary_tree()
x.insert('E', ".")
x.insert('T', "-")
x.insert('I', "..")
x.insert('A', "...")
x.print()
x.delete("I")
x.print()
# print(x.find_elem(x.find_path("A")))
