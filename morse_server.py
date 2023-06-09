import asyncio
import websockets
import json
from morse import morse


async def send_message(websocket, message, client_id):
    outwar_message = {
        "type": "morse_evt",
        "client_id": client_id,
        "payload": message
    }

    await websocket.send(json.dumps(outwar_message))


async def recv_message(websocket):
    message = json.loads(await websocket.recv())
    return message['payload']


async def echo(websocket, user, message, client_id):
    message = morse.encode_ham(user, "echo", message)
    await send_message(websocket, message, client_id)

    response = morse.decode_ham(await recv_message(websocket))

    return response


async def time(websocket, user, message,  client_id):
    message = morse.encode_ham(user, "time", message)
    await send_message(websocket, message, client_id)

    response = morse.decode_ham(await recv_message(websocket))

    return response


async def read_message():
    message = input("message: ")
    return message


async def main():
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        message = json.loads(await websocket.recv())

        if message["type"] != "join_evt":
            print("Did not receive a correct join message")
            return

        client_id = message["client_id"]

        user_message = await read_message()
        while (user_message != "end"):
            print(await echo(websocket, "user", user_message, client_id))
            print(await time(websocket, "user", user_message, client_id))
            user_message = await read_message()

if __name__ == "__main__":
    print("Echo client")
    asyncio.run(main())
