def reverse_string(text: str) -> str:
    ReverseText = ""

    for i in range(len(text)-1,-1,-1):
        ReverseText += text[i]

    return ReverseText

Ans1 = reverse_string("hello")
print(Ans1)

Ans2 = reverse_string("python")
print(Ans2)