import numpy as np
import pandas as pd


class DataDescription:
    def __init__(self, df: pd.DataFrame):

        self.df = df

    def get_description(self):

        return self.df.describe()

    def show_datatypes(self) -> pd.DataFrame:
        return self.df.dtypes

    def get_matrix_correlation(self):
        return self.df.corr()

    def get_grouped_by(self, column_name: str):
        try:
            return self.df.groupby(column_name)
        except:
            print("Failed to get grouping column")
