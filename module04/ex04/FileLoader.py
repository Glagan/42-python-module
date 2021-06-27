import pandas as pd


class FileLoader:
    def load(self, path):
        try:
            df = pd.read_csv(path)
            print('Loading dataset of dimensions {} x {}'.format(*df.shape))
            return df
        except IOError as err:
            print('Failed to load {}: {}'.format(path, err))

    def display(self, df, n):
        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(-n))
