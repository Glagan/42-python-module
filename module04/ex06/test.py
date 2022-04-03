import pandas as pd
from MyPlotLib import MyPlotLib

mpl = MyPlotLib()
data = pd.read_csv('../resources/athlete_events.csv')
hist = mpl.histogram(data, ['Weight'])
hist = mpl.histogram(data, ['Weight', 'Height'])
hist = mpl.histogram(data, ['Year', 'Weight', 'Height'])
density = mpl.density(data, ['Year', 'Weight', 'Height'])
pair_plot = mpl.pair_plot(data, ['Year', 'Weight', 'Height'])
box_plot = mpl.box_plot(data, ['Year', 'Weight', 'Height'])
