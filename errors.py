


INVALID_CONDITION_NAME = 231
INVALID_OPERATOR = 31
INVALID_COLUNM = 323
INVALID_SYNTAX = 3132
LIMID_QUERY_PER_COLUNM = 3242
INVALID_QUERY = 4234
NOT_SUPPORT_METHOD = 21423

class QueryException(Exception):
    def __init__(self, code:int, *arr_params):
        self.arr_params = arr_params
        self.code = code
    def __str__(self):
        """return string when print(e)

        Returns:
            str: string when print(e)
        """       
       
        if (self.code == INVALID_COLUNM):
            return ("INVALID COLUNM")
        elif (self.code == INVALID_OPERATOR):
            return ("INVALID OPERAOTR")
        elif (self.code == INVALID_CONDITION_NAME):
            return ("INVALID CONDITION NAME")
        elif (self.code == INVALID_SYNTAX):
            return ("INVALID SYNTAX")
        elif (self.code==INVALID_QUERY):
            return ("INVALID QUERY "+str(self.arr_params[0]))
        elif (self.code==LIMID_QUERY_PER_COLUNM):
            return ("LIMIT QUERY OF "+str(self.arr_params[0])+" COLUNM")
        elif (self.code==NOT_SUPPORT_METHOD):
            return ("COLUNM "+self.arr_params[0]+ " DOESN'T SUPORT "+self.arr_params[1]+" METHOD")
        else:
            return (str(self.arr_params))
       
