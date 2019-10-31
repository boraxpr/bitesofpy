def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    if start == 1:
        print(start)
        print('time is up')
        return 1
    else:
        print(start)
        return countdown_recursive(start-1)

# countdown_recursive(13)