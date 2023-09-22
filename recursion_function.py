#word = "SWWworldwordwor"
#print(word[1:])

def cleanWord(word):
    if len(word) == 1:
        return word
    
    if word[0] == word[1]:
        print(f"from condition {word}" )
        return cleanWord(word[1:])
    
    print(f"before return {word}")
        
    return word[0] + cleanWord(word[1:])
# Stach [ ]
print(cleanWord("WWWoooorrrldd"))