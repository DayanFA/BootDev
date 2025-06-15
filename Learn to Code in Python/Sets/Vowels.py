def count_vowels(text):
    vowels = set("AEIOUaeiou")
    count = 0
    unique = set()

    for char in text:
        if char in vowels:
            count += 1
            unique.add(char)

    return count, unique