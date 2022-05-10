import numpy as np
import pandas as pd


class CleanTelecomData:
    def __init__(self, df: pd.DataFrame):
        self.df = df

        print('Automation in Action...!!!')

    def convert_to_datetime(self, df: pd.DataFrame) -> pd.DataFrame:

        df['start'] = pd.to_datetime(
            df['start'])
        df['end'] = pd.to_datetime(
            df['end'])

        return df

    def bytes_to_megabytes(self, columns: list) -> pd.DataFrame:

        try:
            megabyte = 1*10e+5
            for x in columns:
                self.df[x] = self.df[x] / megabyte
                self.df.rename(
                    columns={x: f'{x[:-7]}(MegaBytes)'}, inplace=True)

        except:
            print('failed to convert to MB')

        return self.df

    def __convert_bytes_to_megabytes(df, bytes_data):

        megabyte = 1*10e+5
        megabyte_col = df[bytes_data] / megabyte

        return megabyte_col

    def get_info(self) -> pd.DataFrame:

        return self.df.info()
