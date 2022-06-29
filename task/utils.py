import random
import string
import pandas as pd


class Utils:

    @staticmethod
    def get_random_string(length):
        # With combination of lower and upper case
        result_str = ''.join(
            random.choice(string.ascii_letters)
            for i in range(length)
        )
        return

    @staticmethod
    def data_from_csv_table(file_name):
        dt = pd.read_csv(f"task3//Resources/{file_name}.csv")
        # return pandas core and not tuple [1]
        rows = [t[1] for t in dt.iterrows()]
        return rows
