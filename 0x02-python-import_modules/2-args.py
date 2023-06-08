#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    n = 1
    argc = len(sys.argv) - n
    print('{} argument{}{}'.format(
        argc, 's' * (argc != 1),
        ':' if argc > 0 else '.'
        ))
    for arg in sys.argv[n:]:
        print('{}: {}'.format(n, arg))
        n += 1
