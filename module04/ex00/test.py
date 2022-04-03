from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")
if data is not None:
    loader.display(data, 12)
    loader.display(data, -12)

try:
    data = loader.load("../resources/athlete_events.csv2")
except BaseException:
    pass

try:
    data = loader.load("../resources/empty_file.csv")
except BaseException:
    pass
