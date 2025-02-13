def find_character_indexes(astring, achar):
    final = []
    
    for index, letra in enumerate(astring):
        if letra == achar:
            final.append(index)
            
    return final

#print(find_character_indexes("Hello world", "o"))
#print(find_character_indexes("Several instances of the letter e", "e"))
#print(find_character_indexes("A string without the character", "z"))
#print(find_character_indexes("Billions of bilious blue blistering barnacles!", "b"))