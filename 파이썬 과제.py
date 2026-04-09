def adult(age):
    if age >= 20:
        return "성인입니다"
    else:
        return "미성년자"

age = int(input("나이: "))
print(adult(age))