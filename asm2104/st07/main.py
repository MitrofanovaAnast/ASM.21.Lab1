if __name__ == '__main__':
    from CardFile import CardFile
else:
    from .CardFile import CardFile

def closeApp():
    exit(0)

card = CardFile()
container = {
    1: ("Add some element", card.add),
    2: ("Print the element", card.print),
    3: ("Upload to file", card.file_write),
    4: ("Download from file", card.file_read),
    5: ("Clear", card.clear),
    6: ("Change info", card.change),
    7: ("Change Output", card.changeOutput),
    0: ("Exit menu", closeApp)
}

def main():
    try:
        while True:
            print("------------------------------")
            for i, item in container.items():
                print(i, ": ", item[0])
            print("------------------------------")
            container[int(input())][1]()
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()
