import sys

if len(sys.argv) != 3:
    print('ERROR')
    exit()

string = sys.argv[1]
try:
    n = int(sys.argv[2])
    if n < 1:
        raise
except:
    print('ERROR')
    exit()

result = list(word.strip(',.:!?;()[]{{}}=\'"`@_-+#~&$€*%§/\\')
              for word in string.split() if len(word) > n)
result = list(word for word in result if word)
if not result:
    print('ERROR')
    exit()
print(result)
