import pandas as pd


def howManyMedalsByCountry(df: pd.DataFrame, country: str):
    if not isinstance(df, pd.DataFrame):
        return {}
    if not isinstance(country, str):
        return {}
    try:
        by_country = df[df['Team'] == country]
        years = by_country['Year'].unique()
        medals = {}
        for year in years:
            for_year = by_country[by_country['Year'] == year]
            # Remove duplicates per Sport/Team and Year
            grouped = for_year.groupby(['Sport', 'Year', 'Team'])
            year_medals = grouped['Medal'].value_counts()
            if not year_medals.empty:
                medals[year] = {'G': 0, 'S': 0, 'B': 0}
                # Group by Medal for easy access in loop
                by_medals = year_medals.groupby('Medal').sum()
                for rank, count in by_medals.iteritems():
                    medals[year][rank[0]] = count
        return medals
    except BaseException:
        return {}
