"""
Python Version == 3.7.3
Create a simple chat with server using asyncio module.
If server is not responding - terminate the connection and report about error.
Otherwise, print the chat and then close the connection
"""
import asyncio


async def tcp_echo_client(first_message: str, second_message: str, loop):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888, loop=loop
    )

    print(f'Send {first_message!r}')
    writer.write(first_message.encode())

    first_data = await reader.read(100)
    print(f'Received {first_data.decode()!r}')

    print(f'Send {second_message!r}')
    writer.write(second_message.encode())

    second_data = await reader.read(100)
    print(f'Received {second_data.decode()!r}')

    print('Close the connection')
    writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tcp_echo_client("Hello, server! I am a client.",
                                            "I'm fine. Nice to connect to you!",
                                            loop))
    loop.close()
