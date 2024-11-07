def main():
    a = int(input())
    b = 200
    c = 100
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m


if __name__ == '__main__':
    print(main())
