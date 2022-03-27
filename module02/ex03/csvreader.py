import os


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        self.file = None
        if self.filename is None:
            return None
        if self.skip_bottom < 0 or self.skip_top < 0:
            return None
        try:
            self.file = open(self.filename, 'r')
        except OSError as err:
            return None

        header = []
        data = []
        columns = 0
        for line in self.file:
            line_data = list(column.strip('\n')
                             for column in line.split(self.sep))
            if not header:
                header = line_data
                columns = len(header)
            else:
                if len(line_data) != columns:
                    return None
                data.append(line_data)
        if not self.header:
            data.insert(0, header)
            header = None

        class CsvFile:
            def __init__(self, header, data):
                self.header = header
                self.data = data

            def __iter__(self):
                return data.__iter__()

            def getdata(self):
                return self.data

            def getheader(self):
                return self.header

        if self.skip_bottom == 0:
            self.skip_bottom = -len(data)
        return CsvFile(header, data[self.skip_top:-self.skip_bottom])

    def __exit__(self, exc_type, exc_value, exc_trace):
        if self.file:
            self.file.close()