from errors import INVALID_OPERATOR
from condition.condition import Condition, EQUAL_TO, GREATE_THAN, LESS_THAN

import numpy as np
from my_data_frame import myDataFrame as DataFrame
from errors import *


class ComparativeCondition(Condition):
    def __init__(self, code: int, parameters: str) -> None:
        """Contructor

        Args:
            code (int): a code represents the type of operator
            list_args (List): a list of arguments
        """
        super().__init__()

        self.code: int = code
        if parameters[0] != "(" or parameters[-1] != ")":
            raise Exception(INVALID_SYNTAX)
        parameters = parameters[1:-1]
        if (parameters.find(":") != -1):
            self.parameters.extend(parameters.split(":", 1))
        else:
            raise(INVALID_SYNTAX)

    def filter(self, data: DataFrame) -> DataFrame:
        """filter data base on the condition

        Args:
            data (DataFrame): previous data

        Raises:
            Exception: Invalid operator when operator in unknow

        Returns:
            DataFrame: filtered data
        """
        if (len(data) == 0):
            return data
        if type(data[self.parameters[0]][0]) is np.int64:
            constant = np.int64(self.parameters[1])
        else:
            constant = self.parameters[1]
        if self.code == GREATE_THAN:
            return data[data[self.parameters[0]] > constant]
        elif self.code == LESS_THAN:
            return data[data[self.parameters[0]] < constant]
        elif self.code == EQUAL_TO:
            return data[data[self.parameters[0]] == constant]
        else:
            raise Exception(INVALID_OPERATOR)
