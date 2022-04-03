from FileLoader import FileLoader
from ProportionBySport import proportionBySport

print("# Tests")

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
print(proportionBySport(data, 2004, 'Tennis', 'F'))

print("\n# Scale")

print(proportionBySport(data, 2004, 'Tennis', 'F'), end="\n")
# output is "0.02307"
print(proportionBySport(data, 2008, 'Hockey', 'F'), end="\n")
# output is  "0.03284"
print(proportionBySport(data, 1964, 'Biathlon', 'M'), end="\n")
# output is "0.00659"
