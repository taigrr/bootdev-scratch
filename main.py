#!/usr/bin/env python3
with open("books/frankenstein.txt") as file:
    text = file.read()
    wc = len(text.split())
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document")
    print()
    charDict = {}
    for char in text:
        char = char.lower()
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    ldict = sorted(charDict.items(), key=lambda x: x[1], reverse=True)
    for x in ldict:
        if not x[0].isalpha():
            continue
        print(f"The '{x[0]}' character was found {x[1]} times")
    print("--- End report ---")

