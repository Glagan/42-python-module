import sys

if len(sys.argv) != 3:
    print('ERROR')
    exit()

string = str(sys.argv[1])
try:
    n = int(sys.argv[2])
    if n < 1:
        raise
except BaseException:
    print('ERROR')
    exit()

# Use the length *with* punctuation to count word length
result = [word.translate(dict.fromkeys(map(ord, ',.:;!?()[]{}|<>-=_\'"`@+#~&$£€*/\\'), None))
          for word in string.split() if len(word) > n]
result = [word for word in result if word]
print(result)
