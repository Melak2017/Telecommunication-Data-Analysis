import numpy as np
import pandas as pd
import streamlit as st
import numpy as np

import sys
import os
sys.path.append(os.path.abspath(os.path.join('Data')))
sys.path.insert(0, '../scripts')

cleaned_data_csv = "../Data/clean_telecom_data_source.csv"
user_engagement_csv = "../Data/user_engagement.csv"


def top_handset_type(df, top=5):

    return df['handset_type'].value_counts().head(top)


def top_manufacturer(df, top=5):

    return df['handset_manufacturer'].value_counts().head(top)


def top_handset_by_manufacturer(df, manufacturer, top=5):

    return df.groupby('handset_manufacturer')['handset_type'].value_counts()[manufacturer].head(top)


def get_top_app_df(df, top=6):
    app_cols = ['social_media', 'google',
                'email', 'youtube', 'netflix', 'gaming']
    app_metrics = df[app_cols]

    app_total_df = pd.DataFrame(columns=['app', 'total'])

    app_total_df['app'] = app_cols
    app_totals = []
    for app in app_cols:
        app_totals.append(app_metrics.sum()[app])
    app_total_df['total'] = app_totals

    return app_total_df.sort_values(by=['total'], ascending=False).head(top)


def read_csv(csv_path):
    try:
        df = pd.read_csv(csv_path)
        print("file read as csv")
        return df
    except FileNotFoundError:
        print("file not found")


class Dashboard:

    def __init__(self, title: str) -> None:
        self.title = title
        self.page = None
        self.df: pd.DataFrame = self.load_data(
            cleaned_data_csv)  # .copy(deep=True)

        self.df = self.df.rename(columns={'msisdn/number': 'msisdn'})
        self.df = self.df.rename(columns={'dur._(ms)': 'duration'})

        self.df['msisdn'] = self.df['msisdn'].astype(
            "int")
        self.df['msisdn'] = self.df['msisdn'].astype(
            "str")

    @st.cache()
    def load_data(self, path):
        print("Data loaded")
        return read_csv(path)

    def render_siderbar(self, pages, select_label):
        st.sidebar.markdown("# Pages")
        self.page = st.sidebar.selectbox(f'{select_label}', pages)

    def render_data_page(self):

        st.write(self.df.sample(100))

    def top_handset_type(self):
        st.markdown("#### Top Handset type")
        top = st.number_input(label="Top", step=1, value=5, key="top_type")

        res = top_handset_type(self.df, top)
        st.bar_chart(data=res, width=0, height=400,
                     use_container_width=True)

    def top_manufacturer(self):
        st.markdown("#### Top handset manufactruer")

        top = st.number_input(label="Top", step=1, value=5, key="top_man")

        res = top_manufacturer(self.df, top)

        st.bar_chart(data=res, width=0, height=400,
                     use_container_width=True)

    def render(self):
        st.title(f"Welcome To {self.title}")
        self.render_siderbar([
            'Data overview', "User Overview Analysis",
            'User Engagement Analysis', 'User Experience Analysis',
        ], "select page: ")

        if (self.page == "Data overview"):
            sample = st.number_input(label="Sample", step=1,
                                     value=1000, key="sample")

            st.markdown(f"### Sample {sample} Data Over View")
            st.write(self.df.sample(sample))

        elif (self.page == "User Overview Analysis"):
            st.markdown("### User Overview Analysis")
            self.render_overview()

    def render_overview(self):

        self.top_handset_type()
        self.top_manufacturer()


if __name__ == "__main__":
    dashboard = Dashboard("TellCom Data Analytics")
    dashboard.render()
