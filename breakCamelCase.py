def solution(s):
    list(s)
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                charIndex = s.index(letter)
                s.insert(charIndex - 1, " ")
    print(s)

solution("heresCamelCasing")