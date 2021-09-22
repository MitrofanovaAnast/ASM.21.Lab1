from .Spisok import Spisok

def main():
    obj = Spisok()
    while True:
        try:
            print(r"""
        1 - Add element
        2 - Change Element
        3 - Delete Element
        4 - Output Elements
        5 - Write in File
        6 - Read from File
        7 - Clear List""")
            obj.functions[int(input())]()
        except:
            print('Error!!!')
            break

if __name__ == '__main__':
    main()


