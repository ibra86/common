from asyncio import get_event_loop


async def print_hello_world():
    print('hello_world')


if __name__ == "__main__":
    # asyncio.run(print_hello_world())

    loop = get_event_loop()

    loop.run_until_complete(print_hello_world())
