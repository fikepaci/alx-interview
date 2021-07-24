#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Description:
    Write a method that determines if all the boxes can be opened
    Arguments:
    boxes --> List of Lists, it contains the boxes with keys
    Return boolean
    Variables:
    myKeys --> List, Store the number keys to open boxes
    key --> integer, key of the myKeys
    boxKey --> integer, key inside of an specific box
    """
    myKeys = [0]
    for key in myKeys:
        for boxKey in boxes[key]:
            if boxKey not in myKeys and boxKey < len(boxes):
                myKeys.append(boxKey)
    if len(myKeys) == len(boxes):
        return True
    return False