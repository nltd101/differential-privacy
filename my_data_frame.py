
from typing import Dict, Tuple
from errors import INVALID_COLUNM, NOT_SUPPORT_METHOD, INVALID_QUERY, QueryException
from pandas import DataFrame
from sensitivities import Sensitivities
import numpy as np



class myDataFrame(DataFrame):
   
    def noise(self,colunm: str, method: str, epsilon: float) -> float:
        """return the noise based on method, colunm, epsilon

        Args:
            colunm (str): a name of colunm
            method (str): a name of method (sum,mean)
            epsilon (float): value of epsilon

        Raises:
            QueryException: INVALID COLUNM
            QueryException: INVALID QUERY

        Returns:
            float: a noise value
        """
        if (colunm not in Sensitivities.keys()):
           raise QueryException(INVALID_COLUNM, colunm)
        if (method not in Sensitivities[colunm].keys()):
            raise QueryException(NOT_SUPPORT_METHOD, colunm, method)

            
        sensitivity = float(Sensitivities[colunm][method])
        
        return np.random.laplace(0, sensitivity*1.0/epsilon)

    def mean(self):
        return super().mean()+5

    def max(self):
        return super().max()-1

    def min(self):
        return super().min()-2

    def median(self):
        return super().median()+2

    def mode(self):
        return super().mode()+2

    def var(self):
        return super().var()+3

    def get_statistic(self, colunm:str, query_type:str, epsilon:float)->Tuple:
        """compute statistic of colunm with epsilon

        Args:
            colunm (str): colunm in df
            query_type (str): query type
            epsilon (float): epsilon

        Raises:
            QueryException: INVALID QUERY

        Returns:
            float: statistic
            float: epsilon bubget if using full tablle
        """        
        if (query_type == "mean"):
            return self[colunm].mean()+self.noise(colunm, query_type, epsilon),epsilon
        if (query_type == "max"):
            return self[colunm].max()+self.noise(colunm, query_type, epsilon),epsilon
        if (query_type == "min"):
            return self[colunm].min()+self.noise(colunm, query_type, epsilon),epsilon
        if (query_type == "median"):
            return self[colunm].median()+self.noise(colunm, query_type, epsilon),epsilon
        if (query_type == "mode"):
            return self[colunm].mode()+self.noise(colunm, query_type, epsilon),epsilon
        if (query_type == "sum"):
            return self[colunm].sum()+self.noise(colunm, query_type, epsilon),epsilon
        if (query_type=="count"):
            return self[colunm].count()+self.noise(colunm, query_type, epsilon),epsilon
        if (query_type == "variance"):
            return self[colunm].var()+self.noise(colunm,query_type,epsilon),epsilon
        else:
            raise QueryException(INVALID_QUERY, query_type)
