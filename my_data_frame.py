
from typing import Dict, Tuple
from errors import INVALID_COLUNM, NOT_SUPPORT_METHOD, INVALID_QUERY, QueryException
from pandas import DataFrame
from sensitivities import Sensitivities
import numpy as np


class myDataFrame(DataFrame):

    def noise(self, colunm: str, method: str, epsilon: float) -> float:
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
        if method not in ["count"]:
            if (colunm not in Sensitivities.keys()):
                raise QueryException(INVALID_COLUNM, colunm)
            if (method not in Sensitivities[colunm].keys()):
                raise QueryException(NOT_SUPPORT_METHOD, colunm, method)
            sensitivity = float(Sensitivities[colunm][method])
        else:
            sensitivity = 1

        return np.random.laplace(0, sensitivity*1.0/epsilon)

    def get_statistic(self, colunm: str, query_type: str, epsilon: float) -> Tuple:
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
            partial_epsilon = epsilon/2
            noisy_sum = self[colunm].sum()+self.noise(colunm, "sum", partial_epsilon)
            noisy_count = self[colunm].count()+self.noise(colunm, "count", partial_epsilon)
            noisy_mean = noisy_sum/noisy_count
            return noisy_mean, epsilon
        if (query_type == "max"):
            return self[colunm].max()+self.noise(colunm, "sum", epsilon), epsilon
        if (query_type == "min"):
            return self[colunm].min()+self.noise(colunm, "sum", epsilon), epsilon
        if (query_type == "median"):
            return self[colunm].median()+self.noise(colunm, "sum", epsilon), epsilon
        if (query_type == "mode"):
            return self[colunm].mode()+self.noise(colunm, "sum", epsilon), epsilon
        if (query_type == "sum"):
            return self[colunm].sum()+self.noise(colunm, "sum", epsilon), epsilon
        if (query_type == "count"):
            return self[colunm].count()+self.noise(colunm, "count", epsilon), epsilon
        if query_type != "variance":
            raise QueryException(INVALID_QUERY, query_type)

        # calculate variance
        partial_epsilon = epsilon/3

        square_sum = sum((self[colunm][i])**2 for i in range(self[colunm].count()))
        noisy_square_sum = square_sum + self.noise(colunm, "sum_square", partial_epsilon)
        noisy_sum = self[colunm].sum()+self.noise(colunm, "sum", partial_epsilon)
        noisy_count = self[colunm].count()+self.noise(colunm, "count", partial_epsilon)
        noisy_mean = noisy_sum/noisy_count
        noisy_var = (1/noisy_count)*(noisy_square_sum - 2*noisy_mean*noisy_sum) + noisy_mean*noisy_mean

        return noisy_var, epsilon
