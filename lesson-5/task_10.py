answer = input("Уроки зроблені?")
yes = "Погода гарна?"
no = "Вчитися!"
if answer == "так":
    c = input(yes)
    if c == "так":
        print("Гуляти!")
    else:
        print("Грати!")
else:
    print(no)