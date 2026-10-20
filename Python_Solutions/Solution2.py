def count_vowels(text: str) -> int:
    count = 0
    vowels = "aieou"

    for ch in text.lower():
        if ch in vowels:
            count += 1

    return count

Ans1 = count_vowels("Hello Word")
print(Ans1)

Ans2 = count_vowels("PYTHON DEVELOPER")
print(Ans2)

Ans3 = count_vowels("python developer")
print(Ans3)