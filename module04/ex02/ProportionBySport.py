import pandas as pd


def proportionBySport(df: pd.DataFrame, year: int, sport: str, gender: str):
    if not isinstance(df, pd.DataFrame):
        return 0
    if not isinstance(year, int):
        return 0
    if not isinstance(sport, str) or not isinstance(gender, str):
        return 0
    by_year = df[(df['Sex'] == gender) & (df['Year'] == year)]
    by_gender_sport = df[(df['Sport'] == sport) & (df['Sex'] == gender) & (df['Year'] == year)]
    if by_year.shape[0] == 0:
        return 0
    return by_gender_sport.shape[0] / by_year.shape[0]
