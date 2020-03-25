"""
Python Version == 3.6.5
Create a server for chatting with client
"""
import asyncio


@asyncio.coroutine
def handle_echo(reader, writer):
    buffer = 1024
    data = yield from reader.read(buffer)

    first_message = data.decode("utf-8")
    addr = writer.get_extra_info('peername')
    print(f"Received %r from %r" % (first_message, addr))

    first_answer = "Hello, client! I am a server. How are you?"
    print(f"Send: %r" % first_answer)
    writer.write(first_answer.encode())

    second_message = data.decode("utf-8")
    addr = writer.get_extra_info('peername')
    print(f"Received %r from %r" % (second_message, addr))

    second_answer = "Thanks! Good bye!"
    print(f"Send: %r" % second_answer)
    writer.write(second_answer.encode())
    yield from writer.drain()

    print("Close the connection")
    writer.close()
    raise KeyboardInterrupt


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_echo, '127.0.0.1', 5005, loop=loop)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
