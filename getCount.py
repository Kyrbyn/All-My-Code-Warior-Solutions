def get_count(sentence):
    print("Vowel y will not count")
    vowelsCount = 0;
    vowels = ["a","e","i","o","u"]

    # Turns The Input Text To A List
    
    inputLetters = list(sentence)    
    
    # For Each Entry In The List 
    
    for letter in inputLetters:
        # Find The Vowel a
        if letter == "a":
            print("Vowel a Found")
            vowelsCount = vowelsCount + 1
        # Find The Vowel e
        if letter == "e":
            print("Vowel e Found")
            vowelsCount = vowelsCount + 1
        # Find The Vowel i
        if letter == "i":
            print("Vowel i Found")
            vowelsCount = vowelsCount + 1
        # Find The Vowel o
        if letter == "o":
            print("Vowel o Found")
            vowelsCount = vowelsCount + 1
        # Find The Vowel u
        if letter == "u":
            print("Vowel u Found")
            vowelsCount = vowelsCount + 1
    return(vowelsCount)

print(get_count("aeiou"))