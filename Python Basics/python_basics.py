import math
import string
import pygame
import time
pygame.init()

# Waypoint 1: Say Greeting
print()


def hello(name):
    return (('Hello ' + name.strip() + '!'))


print(hello('World'))

# Waypoint 2: Pythagorean Theorem
print()


def calculate_hypotenuse(a, b):
    c = math.sqrt(pow(a, 2)+pow(b, 2))
    return(c)


print('Length of the hypotenuse:', calculate_hypotenuse(3, 4))

# Waypoint 3: Test whether all Conditions are True
print()
lst1 = []


def are_all_conditions_true(lst1):
    if len(lst1) == 0:
        return None
    for elem in lst1:
        if elem is True:
            pass
        elif elem is False:
            return False
    return True


print(are_all_conditions_true([True, True, False, True, False, False, True]))

# Waypoint4:Test whether at least one Condition is True
print()
lst2 = []


def is_a_condition_true(lst2):
    if len(lst2) == 0:
        return None
    for elem in lst2:
        if elem is True:
            return True
    return False


print(is_a_condition_true([True, True, False, True, False, False, True]))    

# Waypoint 5: Filter List of Integers
print()


def filter_integers_greater_than(l, n):
    for i in l:
        if i > n:
            L.append(i)
    return(L)


l = [0, 3, 5, -2, 9, 8]
L = []
print(filter_integers_greater_than(l, 4))

# Waypoint 6: Find Cheapest Hotels
print()


def find_cheapest_hotels(hotel_daily_rates, n):
    for hotel in hotel_daily_rates:
        if hotel[1] <= n:
            hotels.append(hotel[0])
    return(hotels)


hotel_daily_rates = [
    ('Majestic Saigon Hotel', 93),
    ('Hotel Grand Saigon', 120),
    ('Sofitel Saigon Plaza', 123),
    ('Hotel Continental', 62),
    ('Caravelle Hotel', 180),
    ('Sheraton Saigon Hotel', 216),
    ('Park Hyatt Saigon', 209)
]
hotels = []
print(find_cheapest_hotels(hotel_daily_rates, 150))

# Waypoint 7: Calculate Distance between two 2D Points
print()


def calculate_euclidean_distance_between_2_points(p1, p2):
    x1, x2 = p1[0], p2[0]
    y1, y2 = p1[1], p2[1]
    distance = math.sqrt(pow((x2-x1), 2)+pow((y2-y1), 2))
    return distance


print(calculate_euclidean_distance_between_2_points((1, 1), (2, 2)))

# Waypoint 8: Calculate Distance between several 2D Points
print()
edis = []


def calculate_euclidean_distance_between_points(points):
    if len(points) < 2:
        raise ValueError('The list MUST contain at least 2 points')
    for i in range(len(points)-1):
        dis = calculate_euclidean_distance_between_2_points(points[i], points[i + 1])
        edis.append(dis)
    edistance = sum(edis)
    return edistance


print(calculate_euclidean_distance_between_points([(0, 0), (3, 4), (0, 0)]))

# Waypoint 9: Capitalize the Words of a String
print()


def capitalize_word(s):
    if isinstance(s, int):
        raise TypeError('Not a string')
    elif isinstance(s, type(None)):
        return None
    s = s.strip().title()
    return(' '.join(s.split()))


print(capitalize_word('Không  có gì    quý hơn  độc lập      tự do'))

# Waypoint 10: Uppercase and Lowercase Words
print()


def uppercase_lowercase_words(s2):
    if isinstance(s2, int) is True:
        raise TypeError('Not a string')
    if s2 is None:
        return None
    if s2.isspace() is True:
        print('')
    lst3 = []
    lst3 = s2.split()
    lst4 = []
    for i in range(len(lst3)):
        if i % 2 == 0:
            lst4.append(lst3[i].upper())
        elif i % 2 == 1:
            lst4.append(lst3[i].lower())
    lst4 = " ".join(lst4)
    return lst4


print(uppercase_lowercase_words('1 one two 2 3 three four 4 five six'))

# Waypoint 11: Factorial
print()


def factorial(n):
    factorial = 1
    if isinstance(n, int) is False:
        raise TypeError('Not an integer')
    if isinstance(n, int) is True:
        if n < 0:
            raise ValueError('Not a positive integer')
    for i in range(1, n+1):
        factorial = factorial*i
    return factorial


print([(n, factorial(n)) for n in range(6)])

# Waypoint 12: Convert a Digit Character to an Integer
print()


def char_to_int(s):
    lst = [(d, ord(d)) for d in string.digits]
    if isinstance(s, str) is not True:
        raise TypeError('Not a string')
    if len(s) != 1:
        raise ValueError('Not a single digit')
    for elem in lst:
        for i in s:
            if elem[0] == i:
                if elem[1] == 48: return 0                    
                if elem[1] == 49: return 1                    
                if elem[1] == 50: return 2                   
                if elem[1] == 51: return 3                 
                if elem[1] == 52: return 4
                if elem[1] == 53: return 5                   
                if elem[1] == 54: return 6                   
                if elem[1] == 55: return 7                  
                if elem[1] == 56: return 8             
                if elem[1] == 57: return 9

print(char_to_int('9'))

# Waypoint 13: Convert a String of Digit Characters to an Integer
print()


def string_to_int(s):
    lst4 = []
    try:
        if isinstance(s, str) is not True:
            raise TypeError('Not a string')
        for i in s:
            lst4.append(char_to_int(i))
        lst4 = [str(x) for x in lst4]

        lst4 = int("".join(lst4))
        return(lst4)
    except ValueError:
        raise ValueError('Not a positive integer string expression')


print(string_to_int('1234'))

# Waypoint 14: Test Palindrome String
print()


def is_palindrome(value):
    rvs = 0
    if isinstance(value, int) is True:
        num = value
        while num > 0:
            rvs = (10*rvs) + num % 10
            num //= 10
        if rvs == value:
            return True
        else:
            return False
    if isinstance(value, float) is True:
        value = int(str(value).replace('.', ''))
        num = value
        while num > 0:
            rvs = (10*rvs) + num % 10
            num //= 10
        if rvs == value:
            return True
        else:
            return False
    sen = len(value.split())
    lst = string.ascii_lowercase
    if sen > 1:
        value = ''.join([v for v in value.lower() if v in lst])
        vl = ''.join([s for s in value.lower() if s in lst])
        if vl == value[::-1].lower():
            return True
        elif vl != value[::-1].lower():
            return False
    if isinstance(value, str) is True:
        if value.lower() == value[::-1].lower():
            return True
        else:
            return False


print(is_palindrome("No 'x' in Nixon"))

# Waypoint 15: Convert Roman Numerals to Integer
print()


def roman_numeral_to_int(roman_numeral):
    value = 0
    i = 0
    backlist = [5,50,500,1000]
    frontlist = [1,10,100,1000]
    nope = ['IIII', 'VVVV', 'XXXX', 'LLLL', 'CCCC', 'DDDD', 'MMMM']
    roman_symbols = {'N': 0,
                     'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
    if isinstance(roman_numeral, str) is False:
        raise TypeError('Not a string')
    for s in roman_numeral:
        if s.upper() not in roman_symbols:
            raise ValueError('Not a Roman numeral')
    while i < len(roman_numeral):
        for char in nope:
            if char in roman_numeral.upper():
                raise ValueError('Not a Roman numeral')
        if i+1 < len(roman_numeral):
            front = roman_symbols[roman_numeral.upper()[i]]
            back = roman_symbols[roman_numeral.upper()[i+1]]
            if front > back:
                if back is roman_symbols[roman_numeral.upper()[len(roman_numeral)-1]]:
                    value += front + back
                    i += 2
                else:
                    value += front
                    i += 1
            elif front < back:
                value += back - front
                i += 2
                if back not in backlist and front not in frontlist:
                    raise ValueError('Not a Roman numeral')
            elif front >= back:
                value += front + back
                i += 2
            elif front > roman_symbols[roman_numeral.upper()[i-1]]:
                value += front - roman_symbols[roman_numeral.upper()[i-1]]
        else:
            value += roman_symbols[roman_numeral.upper()[i]]
            i += 1
    return value


print(roman_numeral_to_int('CM'))

# Waypoint 16: Play a Melody
print()

MELODY_I_LOVE_YOU = (
     'G3', 'E3', 'G3', 'G3', 'E3', 'G3',
     'A3', 'G3', 'F3', 'E3', 'D3', 'E3', 'F3',
     'E3', 'F3', 'G3', 'C3', 'C3', 'C3', 'C3', 'C3', 'D3', 'E3', 'F3', 'G3',
     'G3', 'D3', 'D3', 'F3', 'E3', 'D3', 'C3',
     'G3', 'E3', 'G3', 'G3', 'E3', 'G3',
     'A3', 'G3', 'F3', 'E3', 'D3', 'E3', 'F3',
     'E3', 'F3', 'G3', 'C3', 'C3', 'C3', 'C3', 'C3', 'D3', 'E3', 'F3', 'G3',
     'G3', 'D3', 'D3', 'F3', 'E3', 'D3', 'C3',
)

MELODY_FUR_ELISE = (
    'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'Ab4', 'B4', 'C5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'C5', 'B4', 'A4',
    'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'Ab4', 'B4', 'C5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'C5', 'B4', 'A4',
    'B4', 'C5', 'D5', 'E5',
    'G4', 'F5', 'E5', 'D5',
    'F4', 'E5', 'D5', 'C5',
    'E4', 'D5', 'C5', 'B4',
    'E4', 'E5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'Ab4', 'B4', 'C5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'C5', 'B4', 'A4',
)

MELODY_HAPPY_BIRTHDAY_TO_YOU = (
    'C4', 'C4', 'D4', 'C4', 'F4', 'E4',
    'C4', 'C4', 'D4', 'C4', 'G4', 'F4',
    'C4', 'C4', 'C5', 'A4', 'F4', 'E4', 'D4',
    'A#4', 'A#4', 'A4', 'F4', 'G4', 'F4',
)

def sharp_cvtr(notes):
    notes = notes.replace(notes[0],chr(ord(notes[0])+1).lower())
    notes = notes.replace('#','b')
    return notes


def play_melody(melody, sound_basedir):
    pygame.display.set_mode((200,100))
    for notes in melody:
        sound = sound_basedir+'/'+notes.lower()+'.ogg'
        
        if notes[1] == '#':
            sound = sound_basedir+'/'+sharp_cvtr(notes).lower()+'.ogg'
               
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(0)
        time.sleep(0.5)


play_melody(MELODY_I_LOVE_YOU, 'D:\INTEK\Sounds\Piano')

