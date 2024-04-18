#!/usr/bin/env python3

from lexer import lexer
from parser import parser
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: runfile.py <file.wtc>")
        return
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            code = file.read()
            tokens = lexer.input(code)
            parsed = parser.parse(tokens)
            print(parsed)
            print("Successfully executed !")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Huh, there is a little problem :", e)

if __name__ == "__main__":
    main()