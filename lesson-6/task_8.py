ans_A = 'Твій урок в кабінеті №7'
ans_B = 'Твій урок в кабінеті №13'
ans_V = 'Твій урок в кабінеті №25'
ans_another = 'Твій урок в кабінеті музики'

question = 'В якому ти класі?'
a = input(question)
if a == "А":
    print(ans_A)
else:
    if a == "Б":
        print(ans_B)
    else:
        if a == "В":
            print(ans_V)
        else:
            print(ans_another)