import string

def word_count(filename, normalize):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            
    except FileNotFoundError:
        return []
    
    words = text.split()
    
    proper = (normalize(word) for i, word in enumerate(words)
              if i > 0 and words[i-1][-1].isalpha() and word[0].isupper())
    
    return list(set(proper))