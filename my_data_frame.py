from errors import INVALID_COLUNM
from pandas import DataFrame
from sensitivities import Sensitivities
import numpy as np
epsilon = 0.1
def noise(colunm:str,method:str,epsilon:float)->float:
    """return the noise based on method, colunm, epsilon

    Args:
        colunm (str): a name of colunm
        method (str): a name of method (sum,mean)
        epsilon (float): value of epsilon

    Raises:
        Exception: INVALID COLUNM
        Exception: INVALID QUERY

    Returns:
        float: a noise value
    """    
    if (colunm not in Sensitivities.keys()):
        raise Exception(colunm+"\'s not support "+method+" method")
    
    if (method not in Sensitivities[colunm].keys()):
        raise Exception("Invalid query "+method)
    sensitivity= float(Sensitivities[colunm][method])
  
    return np.random.laplace(0,sensitivity*1.0/epsilon)
  

class myDataFrame(DataFrame):

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

    def get_statistic(self, colunm,query_type):
      
        if (query_type == "mean"):
            return self[colunm].mean()+noise(colunm, query_type, epsilon)
        if (query_type == "max"):
            return self[colunm].max()+noise(colunm, query_type, epsilon)
        if (query_type == "min"):
            return self[colunm].min()+noise(colunm, query_type, epsilon)
        if (query_type == "median"):
            return self[colunm].median()+noise(colunm, query_type, epsilon)
        if (query_type == "mode"):
            return self[colunm].mode()+noise(colunm, query_type, epsilon)
        if (query_type == "sum"):
            return self[colunm].sum()+noise(colunm, query_type, epsilon)
        if (query_type=="count"):
            return self[colunm].count()+noise(colunm, query_type, epsilon)
        else:
            raise Exception("Invalid query "+query_type)
