date = (3, 30, 2019, 9, 25)

print(
    '{:0>2}/{:0>2}/{} {:0>2}:{:0>2}'.format(
        date[3],
        date[4],
        date[2],
        date[0],
        date[1],
    )
)
