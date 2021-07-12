# import subprocess
import numpy as np
from condition.create_condition import createCondition
import pandas as pd
from errors import *
from executor import Executor
import sys


def main():
    # path = input("Input the path of the dataset: ") if (
    #     len(argv) == 1) else argv[1]

    df = pd.read_csv("adult.csv")
    execute = Executor(df)
    while True:
        try:
            query = input("Write you query: \n")
            execute.execute(query)
        except QueryException as e:
            print(e)


try:
    main()
except KeyboardInterrupt:
    print("\nPress Ctrl-C to terminate while statement")
except Exception as e:
    print("Error:", e)
