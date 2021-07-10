
from datetime import date
from my_data_frame import myDataFrame as DataFrame
from condition.create_condition import createCondition
from typing import List
from errors import QueryException 
import sys
import pandas as pd
import numpy as np
from errors import *
epsilon = 0.1
epsilon_per_colunm = 5


class Executor:
    def __init__(self, df:DataFrame, epsilon:float=epsilon, epsilon_per_colunm:float=epsilon_per_colunm) -> None:
        self.df = df

        self.epsilon = epsilon

        self.colunm_epsilon_dict = {}
        for i in self.df.keys():
            self.colunm_epsilon_dict[i] = epsilon_per_colunm


    def execute(self, query: str):
        """Execute query

        Args:
            query (str): query string look like no sql

        Raises:
            Exception: Invalid syntax

        """
        colunm, query = query.split(".", 1)
        if colunm not in self.df.keys():
            raise QueryException(INVALID_COLUNM)
        query = query.replace(" ", "")
        if (query[-1] != ")"):
            raise QueryException(INVALID_SYNTAX)
        query = query[:-1]

        query_type, conditions_str = query.split("(", 1)

        data = self.df
        if (conditions_str!=""):
            condition = createCondition(conditions_str)
            final_data = DataFrame(condition.filter(data))
        final_data = DataFrame(data)
       
        if (self.colunm_epsilon_dict[colunm] <= 0):
            raise QueryException(LIMID_QUERY_PER_COLUNM, colunm)



        statistic, budget= final_data.get_statistic(colunm,query_type,self.epsilon)
        self.colunm_epsilon_dict[colunm] = self.colunm_epsilon_dict[colunm] -(final_data.shape[0]/df.shape[0])* budget
        print("Response: ", statistic)




