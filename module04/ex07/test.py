import pandas as pd
from Komparator import Komparator

data = pd.read_csv('../resources/athlete_events.csv')
kp = Komparator(data)

print("# Scale")

kp.compare_box_plots('Medal', ['Age'])
kp.compare_histograms('Medal', 'Height')
kp.density('Medal', 'Weight')

print("# Tests")

kp.compare_box_plots('Sex', ['Height', 'Weight'])
kp.compare_box_plots('Sex', 'Height')
kp.density('Sex', 'Height')
kp.compare_histograms('Sex', 'Height')
