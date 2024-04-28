alphabet = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/'
} # dictionary containing international morse code alphabet and corresponding morse code

def decode(code):
    morseCode = {value: key for key, value in alphabet.items()} # key-value dictionary swap to get morse code before corresponding character
    chars = code.split(' ')

    for char in chars:
        print(morseCode.get(char, f"Invalid Morse code: {char}"), end='')

def encode(text):
    text = text.upper() # capitalize since morse code standard

    for char in text:
        print(alphabet.get(char, f"Invalid Character: {char}"), end=' ')

mode = input("Type d to decode, type e for encode: ")

if mode == "d" or mode == "D":
    decode(input("What is your input? "))
elif mode == 'e' or mode == 'E':
    encode(input("What is your input? "))
else:
    print("Invalid character!")
