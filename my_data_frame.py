from pandas import DataFrame
from pandas import Series


class myDataFrame(DataFrame):

    def mean(self):
        return super().mean()+5

    def max(self):
        return super().max()-1

    def min(self):
        return super().min()-2

    def median(self):
        return super().median()+2

    def get_statistic(self, query_type):
        if (query_type == "mean"):
            return self.mean()
        if (query_type == "max"):
            return self.max()
        if (query_type == "min"):
            return self.min()
        if (query_type == "median"):
            return self.median()
