from sense_hat import SenseHat
sense=SenseHat()

def code_letters(word):
    """Finds numbers for words"""
    word_upper=word.upper()
    print(word_upper)
    sense.show_message(word)
    
    map={
        'A':2,
        'B':2,
        'C':2,
        'D':3,
        'E':3,
        'F':3,
        'G':4,
        'H':4,
        'I':4,
        'J':5,
        'K':5,
        'L':5,
        'M':6,
        'N':6,
        'O':6,
        'P':7,
        'Q':7,
        'R':7,
        'S':7,
        'T':8,
        'U':8,
        'V':8,
        'W':9,
        'X':9,
        'Y':9,
        'Z':9,

        }
    
    for key,val in map.items():
      word_upper=word_upper.replace(key,str(val))
      
    return word_upper  
    
    #return [map[letter] for letter in word_upper if letter in map.keys()]