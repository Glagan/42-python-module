import pandas as pd


def howManyMedals(df: pd.DataFrame, player: str):
    if not isinstance(df, pd.DataFrame):
        return {}
    if not isinstance(player, str):
        return {}
    by_player = df[df['Name'] == player]
    years = by_player['Year'].unique()
    medals = {}
    for year in years:
        medals[year] = {'G': 0, 'S': 0, 'B': 0}
        for_year = by_player[by_player['Year'] == year]
        for rank, count in for_year['Medal'].value_counts().iteritems():
            medals[year][rank[0]] = count
    return medals
