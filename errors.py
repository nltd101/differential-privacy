from typing import Any


INVALID_CONDITION_NAME = 231
INVALID_OPERATOR = 31
INVALID_COLUNM = 323
INVALID_SYNTAX = 3132
def handle_errors(e:Any):
    """print text appropiate to err

    Args:
        e (Any): code err or text
    """    

    if (str(e) == str(INVALID_COLUNM)):
        print("INVALID_COLUNM")
    elif (str(e) ==str(INVALID_OPERATOR)):
        print("INVALID_OPERAOTR")
    elif (str(e) == str(INVALID_CONDITION_NAME)):
        print("INVALID_CONDITION_NAME")
    elif (str(e) == str(INVALID_SYNTAX)):
        print("INVALID_SYNTAX")
    else:
        print(e)
