# import subprocess
import numpy as np
from condition.create_condition import createCondition
import pandas as pd
from errors import *
from executor import Executor
import sys


def main(argv):
    # path = input("Input the path of the dataset: ") if (
    #     len(argv) == 1) else argv[1]


    df = pd.read_csv("adult.csv")
    execute = Executor(df)
    while True:
        try:
            query = input("Write you query: \n")
            execute.execute(query)
        except Exception as e:
            handle_errors(e)


try:
    main(sys.argv)
except KeyboardInterrupt:
    print("\nPress Ctrl-C to terminate while statement")
except Exception as e:
    print("Error:", e)
# execute = Executor(df)

# query = "fnlwgta.mean({$and:[{$gt:(age:20)},{$lt:(age:30)}]})"
# execute.execute(query)



