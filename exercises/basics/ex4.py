def remove_chars(word,n):
    if n < len(word):
        return word[n:]
    return "Not Possible"


print(remove_chars("Chinmay",2))