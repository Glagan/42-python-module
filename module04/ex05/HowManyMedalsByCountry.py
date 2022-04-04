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
        medals = {}
        for year in by_country.sort_values('Year')['Year'].unique():
            for_year = by_country[by_country['Year'] == year]
            by_unique_sports = pd.concat(
                (for_year.query("Sport not in @team_sports"),
                 for_year.query("Sport in @team_sports").drop_duplicates(subset=['Sex', 'Season', 'City', 'Sport', 'Event', 'Medal'], keep='first'))
            )
            year_medals = by_unique_sports.value_counts('Medal')
            if not year_medals.empty:
                medals[year] = {'G': 0, 'S': 0, 'B': 0}
                # Group by Medal for easy access in loop
                by_medals = year_medals.groupby('Medal').sum()
                for rank, count in by_medals.iteritems():
                    medals[year][rank[0]] = count
        return medals
    except BaseException:
        return {}
