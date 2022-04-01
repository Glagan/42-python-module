import pandas as pd


class SpatioTemporalData:
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("dataset should be a DataFrame")
        self.data = df

    def when(self, location: str):
        if not isinstance(self.data, pd.DataFrame):
            return []
        try:
            return self.data[self.data['City'] == location]['Year'].unique().tolist()
        except BaseException:
            return []

    def where(self, date: str):
        if not isinstance(self.data, pd.DataFrame):
            return []
        try:
            return self.data[self.data['Year'] == date]['City'].unique().tolist()
        except BaseException:
            return []
