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

result = [word.strip(',.:!?;()[]{{}}=\'"`@_-+#~&$€*%§/\\')
          for word in string.split() if len(word) > n]
result = [word for word in result if word]
print(result)
