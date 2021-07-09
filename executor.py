
from datetime import date
from my_data_frame import myDataFrame as DataFrame
from condition.create_condition import createCondition
from typing import List

import sys
import pandas as pd
import numpy as np
from errors import *


class Executor:
    def __init__(self, df) -> None:
        self.df = df

    def execute(self, query: str):
        """Execute query

        Args:
            query (str): query string look like no sql

        Raises:
            Exception: Invalid syntax

        """
        colunm, query = query.split(".", 1)
        if colunm not in self.df.keys():
            raise Exception(INVALID_COLUNM)
        query = query.replace(" ", "")
        if (query[-1] != ")"):
            raise Exception(INVALID_SYNTAX)
        query = query[:-1]

        query_type, conditions_str = query.split("(", 1)

        # data = self.df[colunm]
        data = self.df
        condition = createCondition(conditions_str)
        final_data = condition.filter(data)
        final_data = DataFrame(final_data[colunm])
        # print(final_data)

        print("Response: ", final_data.get_statistic(query_type))


