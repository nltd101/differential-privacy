from errors import INVALID_OPERATOR
from condition.condition import Condition, EQUAL_TO, GREATE_THAN, LESS_THAN

import numpy as np
from my_data_frame import myDataFrame as DataFrame


class ComparativeCondition(Condition):
    def __init__(self, code: int, parameters: str) -> None:
        """Contructor

        Args:
            code (int): a code represents the type of operator
            list_args (List): a list of arguments
        """
        super().__init__()

        self.code: int = code

        self.parameters.append(parameters)

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
        if type(data[0]) is np.int64:
            constant = np.int64(self.parameters[0])
        else:
            constant = self.parameters[0]
        if self.code == GREATE_THAN:
            return data[data > constant]
        elif self.code == LESS_THAN:
            return data[data < constant]
        elif self.code == EQUAL_TO:
            return data[data == constant]
        else:
            raise Exception(INVALID_OPERATOR)
