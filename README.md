# Morse tree

## Requirements

This project requires Python 3.5 or later, as well as the `asyncio` and `websockets` libraries.

To install these dependencies, run the following command:

```
pip install -r requirements
```


## Binary_tree

This module implements a Binary Tree data structure, and it provides several methods to operate with it, such as inserting new nodes, deleting nodes, and finding a path or an element in the tree.

### Usage

To use the `Binary_tree` class, you can import it into your Python code:

```
from binary_tree import Binary_tree

bt = Binary_tree()
```

- **Inserting nodes**

  To insert a node into the tree, you need to provide a string with the data you want to insert and an encoding string that specifies the path to the new node in the tree. The encoding string is a sequence of "." and "-" characters that represents the left and right branches of the tree, respectively.
  If the path is not correct 1 is returned, otherwise it will return 0 upon successful insertion.

  ```
  bt.insert("a", ".")
  bt.insert("b", "-")
  bt.insert("c", "--")
  bt.insert("d", ".-")

  bt.print()
  # 0 None
  #       1 a
  #               2 d
  #       1 b
  #               2 c
  ```

- **Deleting nodes**

  To delete a node from the tree, you need to provide the data of the node you want to delete.
  The function does a pre-order search, and keeps traversing until the element is found and deleted or reached the last node in the tree.

  If the element had children , all of them well be gone as well

  ```
  bt.delete("b")

  bt.print()
  # 0 None
  #       1 a
  #               2 d
  ```

- **Finding a path**

  To find the path to a node in the tree, you need to provide the data of the node you want to find.
  The function does a recursive pre-order search and builds up the path backwards once the element has been found, using the keys `.` and `-` that encode the path, the final answer will be in the correct order because the function is recursive. If the element was not found an empty string is returned

  ```
  path = bt.find_path("d")
  print(path)  # ".-"
  ```

  The following is a break down of how it functions:

  - The method starts by checking if the current node is the target element. If it is, it returns the traversal path that was passed in as a parameter.
  - If the current node is not the target element, it iterates over the two sides of the binary tree using the `__sides` dictionary, and for each side that is not empty, it recursively calls the `find_path` method on the next node in that side of the tree.
  - If the target element is found in the subtree rooted at one of the child nodes, the method returns the traversal path to the target element.

- **Finding an element**

  To find an element in the tree, you need to provide an encoding string that specifies the path to the node that contains the element.
  The function starts with the root node and keeps accessing the `.` and `-` children until theres one element left, then it returns it

  ```
  elem = bt.find_elem(".-")
  print(elem)  # "d"
  ```

  The following is a break down of how it works:

  - The method starts at the root node of the binary tree and iterates over the characters in the path string, one character at a time. For each character in the path string, it moves down to the next node in the binary tree, according to the direction indicated by the character.
  - Once it reaches the end of the path string, it returns the value of the node it has reached.
  - Specifically, for each character in the path string, it checks whether the character indicates that the next node is to the left or the right of the current node. It then sets the node variable to the next node in that direction.
  - When it reaches the end of the path string, it returns the value of the node it has reached as a string.

- **Converting to an array**

  To convert the tree to a binary heap array, you can use the `to_array` method.
  It traverses the tree using Breadth First Search (BFS), also called level order search.

  ```
  bt.insert("x", "-")
  bt.insert("y", "-.")
  arr = bt.to_array()
  print(arr)  # ["a", "x", "d", "y"]
  ```

  The method uses a queue to do the search, but rather than dequeueing items, it simply moves the index forward by one, and with each iteration it appends the children of the node at the current index, until we reach a node with node left child, because at that point we know we have reached the end of the list, since the trees we will be using are perfect binary trees.

- **Printing the tree**

  To print the tree, you can use the print method, which does it in a pre-order way and adds indentation automatically when moving down the levels. The function follows a recurssive pre-order approach.

  ```
  bt.print()
  ```

---

## Heap

This module implements a binary heap array that will be used to decode morse messages using the message as a path to traverse the array.
To traverse the heap array, 2 lambda functions are implemented to satisfy the following properties of a heap:

- to access the left child of the node: `2i + 1`
- to access the right child of the node: `2i + 2`

Where `i` is the index of the current node. The way it works is that we multiply by 2 to go down the tree by 1 level then add 1 because we start indexing at 0

### Usage

This class is mostly useless on its own and out of context. It is used in the `Morse` class to decode messages in a different way as will be discussed below. To use the module, you will have to import it and initialise it with an array.

```
h = Heap([[5, 3, 8, 1, 7, 6, 10]])
```

- **Finding an element**
  To find an element using a given path, you can use the `find_elem(path: str) -> str` method which takes in an encoded string that consists of `.` and `-` representing the path to the element from the root.

  When traversing the structure, the function uses the `__sides` dictionary which has 2 lambda functions that take in the current index and return the index of the left and write child by applying the method explained at the start.
  It starts at index `0` of the heap and then starts moving down the tree by calling the correct lambda function based on if the next node is a `.` or `-`.

  For example, if we want to find the element at path `.-` from the heap constructed earlier:

  - `h.find_elem(".-")`
  - We start at the root, index `0`.
  - `__sides['.']` will call `2i+1` so `2*0+1` is `1`
  - `__sides['-']` will call `2i+2` so `2*1+2` is `4`

  The final answer is the element at index 4 which is the number `7`

- **Decoding a message**

  To decode a full message, you can use the `decode` message which takes in a message of multiple paths, splits it by spaces ` ` and calls the `find_elem` on each path string, if the path was a `/` it appends a space ` ` which is a word breaker.

  ```
  msg = h.decode(".- / -.")

  print(msg) # 7 6
  ```

  It does the same exact job as the decode function of the `Morse` class, which will be explained in more details next.

---

## Morse

This module implements a Morse code encoder/decoder using a binary tree data structure.
Upon instantiation of a `Morse` object, it creates a `Binary_tree` and fills it up with the required elements, with the path being the morse encoding and the element at the end of the path is the value for it. Finally it prints the tree to the user

### Usage

To use the Morse class, you can import it into your Python code:

```
from morse import Morse

morse = Morse()
```

- **Encoding a message**

  To encode a message into Morse code, you can use the encode method.
  The function loops through the message to encode and calls the `find_path` method to find the character and appends it to a string one by one.

  ```
  encoded_message = morse.encode("Hello, World!")
  print(encoded_message)  # ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
  ```

  The following is a break down of how it works:

  - First, it converts the message to all uppercase letters using the `upper()` method. This is done to ensure that all characters in the message can be encoded.
  - Then, it initializes an empty string called `encoded_message` to hold the encoded message.
  - Next, it loops through each character in the message. If the character is a space, it appends `'/ '` to `encoded_message` and moves on to the next character. Otherwise, it calls the `find_path()` method on the binary tree object (which is stored as a private attribute called `__tree`) to find the encoded path for that character, and appends the path to `encoded_message`, followed by a space.
  - Finally, it returns `encoded_message`, with the last character (which is a space) removed using the slice notation `[:-1]`.

- **Decoding a message**

  To decode a Morse code message, you can use the decode method.
  The function first separates the message by spaces ` ` and then loops through these items, and calling the `find_elem` method appending the returned value to a string and returns it.
  If the character is a `/` it appends a ` ` which is a word breaker

  ```
  decoded_message = morse.decode(".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--")
  print(decoded_message)  # "HELLO, WORLD!"
  ```

  The following is a break down of how it works:

  - First, it initializes an empty string called `decoded_message` to hold the decoded message.
  - Next, it loops through each code (which is a space-separated string of characters or paths) in the encoded message obtained by calling the `split()` method on the message string.
  - If the code is an empty string (which can happen if there are multiple spaces in a row), it skips to the next code using the `continue` statement.
  - If the code is the special code `'/ '`, it appends a space to `decoded_message` and moves on to the next code.
  - Otherwise, it calls the `find_elem()` method on the binary tree object to find the character represented by the code, and appends the character to `decoded_message`.
  - Finally, it returns `decoded_message`.

- **Encoding a message with Ham radio format**

  To encode a message in the Ham radio format, you can use the `encode_ham` method.
  This function takes in the sender, receiver and message and then formats it in the following string:
  `<receiver>DE<sender>=<message>=(`
  where \<receiver>, \<sender> and \<message> are replaced by their corresponding values.
  Once done, it passes the formatted string to the `encode` function to get the final values in morse code.

  ```
  encoded_message = morse.encode_ham("KI7ABC", "W6XYZ", "Hello, World!")
  print(encoded_message)  # W6XYZDEKI7ABC=HELLO,WORLD!=(
  ```

- **Decoding a message with Ham radio format**

  To decode a Ham radio format message, you can use the `decode_ham` method.
  First it decodes the message using the `decode` method and then parses the returned string to extract the sender, receiver and the message and returns them

  ```
  decoded_message = morse.decode_ham("W6XYZDEKI7
  ```

  The following is a break down of how it works:

  - First, it calls the `decode_heap()` method on the class instance to obtain the decoded message.
  - Then, it finds the indices of the "DE" and "=" characters in the decoded message using the `find()` method.
  - It then extracts the receiver's name, sender's name, and message from the decoded message using slice notation and returns them as a tuple of strings.
  - Specifically, it finds the substring of the decoded message from the beginning up to the index of "DE" to get the receiver's name. It then finds the substring between the "DE" and "=" characters to get the sender's name, and the substring between "=" and the second-to-last character (which is the opening parenthesis) to get the message.
  - Finally, it returns these three values as a tuple in the form `(sender, receiver, msg)`.

---

## morse_server

This module implements a client that takes input from user and converts it to morse ham signal then sends it to a morse server and receives an echo and the time.

### Usage

To use this script, you just need to run the following command:

```
python morse_server.py
```

- **Encoding a message**

### Functions

- **main()**

  This is the main function of the script, which sets up the WebSocket connection, receives a join message from the server, prompts the user to input a message, and then sends and receives messages to and from the server using the `echo()` and `time()` functions. The function loops until the user inputs "end".

  The function first creates a WebSocket connection to the server using the `websockets.connect()` function. It then receives a message from the server using the `websocket.recv()` method and checks that the message is a "join" message with a valid client ID.

  The function then enters a loop, prompting the user to input a message and then sending the message to the server using the `echo()` and `time()` functions. The functions wait for a response from the server and then decode the response before printing it to the console.

  Finally, the function exits the loop when the user inputs "end" and closes the WebSocket connection.

- **recv_message(websocket)**

  This function takes a single argument, `websocket`, which is the WebSocket connection object. The function waits for a message to be received from the server using the `websocket.recv()` method, and then parses the message as a JSON object. The `payload` field of the message object is returned.

- **read_message()**

This function prompts the user to input a message using the `input()` function and returns the user's input as a string.

- **echo(websocket, user, message, client_id)**

  This function takes four arguments: `websocket`, which is the WebSocket connection object, `user`, which is the name of the user, `message`, which is the message to send to the server, and `client_id`, which is the unique identifier for the client. The function encodes the `user` as sender, `"echo"` as receiver and `message` as the paylod as a Morse code ham message using the `morse.encode_ham()` function, and then sends the message to the server using the `send_message()` function. The function then waits for a response from the server using the `recv_message()` function, decodes the response using the `morse.decode_ham()` function, and returns the decoded response.

- **time(websocket, user, message, client_id)**

  This function is similar to the `echo()` function, but it sends a different type of message to the server. The message payload is still encoded as Morse code using the `morse.encode_ham()` function, but the message receiver is `"time"` instead of "echo".

- **send_message(websocket, message, client_id)**

This function takes three arguments: `websocket`, which is the WebSocket connection object, `message`, which is the message to send to the server, and `client_id`, which is the unique identifier for the client. The function creates an outbound message object with the `message` payload and `client_id` and sends it to the server using the `websocket.send()` method.
