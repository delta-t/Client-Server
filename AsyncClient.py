"""
Python Version == 3.6.5
Create a simple chat with server using asyncio module.
If server is not responding - terminate the connection and report about error.
Otherwise, print the chat and then close the connection.
"""
import asyncio


@asyncio.coroutine
def tcp_echo_client(first_msg: str,
                    second_msg: str, buffer: int, loop):
    reader, writer = yield from asyncio.open_connection("127.0.0.1",
                                                        5005, loop=loop)

    print(f'Client: %r' % first_msg)
    writer.write(first_msg.encode())

    first_data = yield from reader.read(buffer)
    print(f'Server: %r' % first_data.decode("utf-8"))

    print(f'Client: %r' % second_msg)
    writer.write(second_msg.encode())

    second_data = yield from reader.read(buffer)
    print(f'Server: %r' % second_data.decode("utf-8"))

    print('Close the connection')
    writer.close()


first_message = "Hello, server! I am a client."
second_message = "I'm fine. Nice to connect to you!"
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(first_message, second_message, 1024, loop))
loop.close()
