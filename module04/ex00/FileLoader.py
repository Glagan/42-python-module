import pandas as pd


class FileLoader:
    def __init__(self) -> None:
        pass

    def load(self, path: str):
        if not isinstance(path, str):
            return None
        try:
            df = pd.read_csv(path)
            print('Loading dataset of dimensions {}'.format(' x '.join(str(i) for i in df.shape)))
            return df
        except OSError as err:
            print('Failed to load dataset: {}'.format(err))
            return None

    def display(self, df: pd.DataFrame, n: int):
        if not isinstance(df, pd.DataFrame):
            return
        if not isinstance(n, int) or n == 0:
            return
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(-n))
