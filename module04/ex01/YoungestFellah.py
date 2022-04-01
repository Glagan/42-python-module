from math import isnan
import pandas as pd


def youngestFellah(df: pd.DataFrame, year: int):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
        df: pandas.DataFrame object containing the dataset.
        year: integer corresponding to a year.
    Returns:
        dct: dictionary with 2 keys for female and male athlete.
    """
    if not isinstance(df, pd.DataFrame):
        return {'f': 'nan', 'm': 'nan'}
    if not isinstance(year, int):
        return {'f': 'nan', 'm': 'nan'}
    by_f = df[(df['Year'] == year) & (df['Sex'] == 'F')]
    by_m = df[(df['Year'] == year) & (df['Sex'] == 'M')]
    return {'f': by_f['Age'].min(), 'm': by_m['Age'].min()}
