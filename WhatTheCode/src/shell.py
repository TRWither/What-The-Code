from parser import parser
from lexer import lexer

def main():
    print("What The Code v1.0.0")
    print("Type 'help_me_!!!' or 'license' for more infos.")
    print()
    while True:
        s = input("-> ")
        if s == "run run run":
            print("COME HERE !!!")
            break
        else:
            result = parser.parse(s)
            if result != None:
                print(result)
            
if __name__ == "__main__":
    main()