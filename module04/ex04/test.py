from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

print("# Tests")

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
sp = SpatioTemporalData(data)
print(sp.where(1896))
print(sp.where(2016))
print(sp.when('Athina'))
print(sp.when('Paris'))

print("\n# Scale")

print(sp.where(2000))
# output is: ['Sydney']
print(sp.where(1980))
# output is: ['Lake Placid', 'Moskva'] If a single of these locations is returned it's ok.
print(sp.when('London'))
# output is: [2012, 1948, 1908]
