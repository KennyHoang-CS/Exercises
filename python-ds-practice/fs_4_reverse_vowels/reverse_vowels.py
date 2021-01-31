def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    reversedVowels = []
    tempStr = []
    newStr = []

    for letter in s:
        if letter.lower() in 'aeiou':
            tempStr.append('X')
            reversedVowels.append(letter)
        else:
            tempStr.append(letter)

    reversedVowels.reverse()

    index = 0
    for letter in tempStr:
        if letter == 'X':
            newStr.append(reversedVowels[index])
            index += 1
        else:
            newStr.append(letter)

    return ('').join(newStr)


#print(reverse_vowels("Hello!"))
#print(reverse_vowels("Tomatoes"))
#print(reverse_vowels("Reverse Vowels In A String"))
#print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))