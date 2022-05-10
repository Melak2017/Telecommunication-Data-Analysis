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

    def convert_to_mega_bytes(self, df):

        df = self.__convert_bytes_to_megabytes(df, 'social_media_dl_(bytes)')
        df = self.__convert_bytes_to_megabytes(df, 'social_media_ul_(bytes)')

        df = self.__convert_bytes_to_megabytes(df, "google_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "google_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "email_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "email_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "youtube_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "youtube_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "netflix_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "netflix_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "gaming_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "gaming_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "other_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "other_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "total_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "total_ul_(bytes)")

        converted_df = df.rename(columns={'social_media_dl_(bytes)': 'social_media_dl',
                                          'social_media_ul_(bytes)': 'social_media_ul',

                                          'google_dl_(bytes)': 'google_dl',
                                          'google_ul_(bytes)': 'google_ul',

                                          'email_dl_(bytes)': 'email_dl',
                                          'email_ul_(bytes)': 'email_ul',

                                          'youtube_dl_(bytes)': 'youtube_dl',
                                          'youtube_ul_(bytes)': 'youtube_ul',

                                          'netflix_dl_(bytes)': 'netflix_dl',
                                          'netflix_ul_(bytes)': 'netflix_ul',

                                          'gaming_dl_(bytes)': 'gaming_dl',
                                          'gaming_ul_(bytes)': 'gaming_ul',

                                          'other_dl_(bytes)': 'other_dl',
                                          'other_ul_(bytes)': 'other_ul',

                                          'total_dl_(bytes)': 'total_dl',
                                          'total_ul_(bytes)': 'total_ul',
                                          })
        return converted_df

    def __convert_bytes_to_megabytes(df, bytes_data):

        megabyte = 1*10e+5
        megabyte_col = df[bytes_data] / megabyte

        return megabyte_col

    def get_info(self) -> pd.DataFrame:

        return self.df.info()
