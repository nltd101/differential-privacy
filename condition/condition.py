
from my_data_frame import myDataFrame as DataFrame
from typing import List
from abc import ABC, abstractmethod
from errors import *
GREATE_THAN = 1
LESS_THAN = 2
EQUAL_TO = 3
AND = 4
OR = 5
NOT = 6
comparative_condition = {"$gt": GREATE_THAN, "$lt": LESS_THAN, "$eq": EQUAL_TO}
logic_gate_condition = {"$and": AND, "$or": OR, "$not": NOT}


class Condition(ABC):
    parameters = []

    def __init__(self) -> None:
        """Contructor

        Args:
            parameter (List): list of the parameters
        """
        self.parameters: List[Condition] = []
        # self.parameters = parameter
        # pass

    @abstractmethod
    def filter(self, data: DataFrame) -> DataFrame:
        raise Exception("Not implemented")
