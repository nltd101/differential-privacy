INVALID_CONDITION_NAME = 231
INVALID_OPERATOR = 31
INVALID_COLUNM = 323
INVALID_SYNTAX = 3132
LIMID_QUERY_PER_COLUNM = 3242
INVALID_QUERY = 4234
NOT_SUPPORT_METHOD = 21423


class QueryException(Exception):
    def __init__(self, code: int, *arr_params):
        self.arr_params = arr_params
        self.code = code

    def __str__(self):
        """return string when print(e)

        Returns:
            str: string when print(e)
        """

        if (self.code == INVALID_COLUNM):
            return ("Invalid colunm")
        elif (self.code == INVALID_OPERATOR):
            return ("Invalid operator")
        elif (self.code == INVALID_CONDITION_NAME):
            return ("Invalid codition name")
        elif (self.code == INVALID_SYNTAX):
            return ("Invalid syntax")
        elif (self.code == INVALID_QUERY):
            return ("Invalid query: "+str(self.arr_params[0]))
        elif (self.code == LIMID_QUERY_PER_COLUNM):
            return ("Limit query of "+str(self.arr_params[0])+" colunm")
        elif (self.code == NOT_SUPPORT_METHOD):
            return ("Colunm "+self.arr_params[0] + " doesn't support "+self.arr_params[1]+" method")
        else:
            return (str(self.arr_params))
