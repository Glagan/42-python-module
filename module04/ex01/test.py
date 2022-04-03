from FileLoader import FileLoader
from YoungestFellah import youngestFellah

print("# Tests")

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
print(youngestFellah(data, 2004))
print(youngestFellah(data, 1991))

print("\n# Scale")

print(youngestFellah(data, 1992))
# output is: "{'f': 12.0, 'm': 11.0}"
print(youngestFellah(data, 2004))
# output is: "{'f': 13.0, 'm': 14.0}"
print(youngestFellah(data, 2010))
# output is: "{'f': 15.0, 'm': 15.0}"
print(youngestFellah(data, 2003))
# output is: "{'f': nan, 'm': nan}"
