
def callback_func(number):
    print(number)

def test(callback):
    callback('1')


if __name__ == "__main__":
    test(callback_func)