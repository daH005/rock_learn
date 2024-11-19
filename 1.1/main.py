def main(b, c):
    a = int(input())
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m


if __name__ == '__main__':
    print(main(200, 100))
