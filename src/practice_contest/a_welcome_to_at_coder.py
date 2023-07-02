def main():
    num1 = int(input())
    num2, num3 = (int(x) for x in input().split())
    str1 = input()

    print(f'{num1 + num2 + num3} {str1}')

if __name__ == '__main__':
    main()
