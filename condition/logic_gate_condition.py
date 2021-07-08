
from typing import List
from condition.condition import *
# from condition.create_condition import createCondition
from condition import create_condition
from errors import *


class LogicGateCondition(Condition):

    def __init__(self, code: int, parameters: str) -> None:
        """Contructor

        Args:
            code (int): code of operator
            list_args (List): list of arguments

        Raises:
            Exception: Invalid syntax
        """
        super().__init__()
        self.code: int = code
        # in the logic conditon container, sub condition in [ ]
        if (parameters[0] != "[" or parameters[-1] != "]"):
            raise Exception(INVALID_SYNTAX)
        parameters = parameters[1:-1]
        if code == NOT:
            # 1 condition
            self.parameters.append(
                create_condition.createCondition(parameters))
        elif code in [AND, OR]:
            # 2 conditions
            condition1, condition2 = parameters.split(",", 1)
            self.parameters.append(
                create_condition.createCondition(condition1))
            self.parameters.append(
                create_condition.createCondition(condition2))

    def filter(self, data: DataFrame) -> DataFrame:
        """filter data base on self

        Args:
            data (DataFrame): previous data

        Returns:
            DataFrame: filtered data
        """
        if self.code == NOT:
            indexes = self.parameters[0].filter(data).index
            indexes = indexes.tolist()
            # get indexes of the data when the condition is true
            # return records not being in that indexes
            return data[~data.index.isin(indexes)]
        elif self.code == AND:
            # call filter 2 times
            return self.parameters[1].filter(self.parameters[0].filter(data))
        elif self.code == OR:
            # call 2 filters and merge 2 results
            indexes = self.parameters[0].filter(data).index.tolist()
            indexes.extend(
                self.parameters[1].filter(data).index.tolist())
            # remove indexes being equal
            indexes = list(set(indexes))
            return data[data.index.isin(indexes)]
        return
