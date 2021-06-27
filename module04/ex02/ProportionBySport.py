def proportionBySport(df, year, sport, gender):
    by_year_gender = df[(df['Year'] == year) & (df['Sex'] == gender)]
    by_sport = by_year_gender[by_year_gender['Sport'] == sport]
    return by_sport.shape[0] / by_year_gender.shape[0]
