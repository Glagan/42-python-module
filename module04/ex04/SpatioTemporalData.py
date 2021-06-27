import pandas as pd


class SpatioTemporalData:
    def __init__(self, df):
        self.data = df

    def when(self, location):
        return self.data[self.data['City'] == location]['Year'].unique()

    def where(self, date):
        return self.data[self.data['Year'] == date]['City'].unique()
