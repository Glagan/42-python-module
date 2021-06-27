def youngestFellah(df, year):
    by_f = df[(df['Year'] == year) & (df['Sex'] == 'F')]
    by_m = df[(df['Year'] == year) & (df['Sex'] == 'M')]
    return {'f': by_f['Age'].min(), 'm': by_m['Age'].min()}
