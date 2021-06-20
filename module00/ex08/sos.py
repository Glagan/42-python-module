import sys

translation = {
    'a': '.-',      'b': '-...',    'c': '-.-.',   'd': '-..',
    'e': '.',       'f': '..-.',    'g': '--.',    'h': '....',
    'i': '..',      'j': '.---',    'k': '-.-',    'l': '.-..',
    'm': '--',      'n': '-.',      'o': '---',    'p': '.--.',
    'q': '--.-',    'r': '.-.',     's': '...',    't': '-',
    'u': '..-',     'v': '...-',    'w': '.--',    'x': '-..-',
    'y': '-.--',    'z': '--.',     '0': '-----',  '1': '.----',
    '2': '..---',   '3': '...--',   '4': '....-',  '5': '.....',
    '6': '-....',   '7': '--...',   '8': '---..',  '9': '----.',
}

if len(sys.argv) == 1:
    exit()

result = []
for phrase in sys.argv[1:]:
    words = phrase.split(' ')
    for word in words:
        morse = []
        for char in word.lower():
            if not char in translation:
                print('ERROR')
                exit()
            morse.append(translation[char])
        result.append(' '.join(morse))
if result:
    print(' / '.join(result))
