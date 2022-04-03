import pandas as pd

team_sports = [
    'Basketball', 'Football',  'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo',
    'Hockey', 'Rowing', 'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball',
    'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo'
]


def howManyMedalsByCountry(df: pd.DataFrame, country: str):
    if not isinstance(df, pd.DataFrame):
        return {}
    if not isinstance(country, str):
        return {}
    try:
        by_country = df[df['Team'] == country]
        by_unique_sports = pd.concat(
            (by_country.query("Sport not in @team_sports"),
             by_country.query("Sport in @team_sports").drop_duplicates(subset=['Sex', 'Games', 'Year', 'Season', 'Sport', 'City', 'Event'], keep='first'))
        )
        years = by_unique_sports.sort_values('Year')['Year'].unique()
        medals = {}
        for year in years:
            for_year = by_unique_sports[by_unique_sports['Year'] == year]
            year_medals = for_year.value_counts()
            if not year_medals.empty:
                medals[year] = {'G': 0, 'S': 0, 'B': 0}
                # Group by Medal for easy access in loop
                by_medals = year_medals.groupby('Medal').sum()
                for rank, count in by_medals.iteritems():
                    medals[year][rank[0]] = count
        return medals
    except BaseException:
        return {}
