def voit(age, citizenship, disqualification):
    if (age < 18): print("Вам меньше 18 лет, голосовать нельзя")
    elif (citizenship != "Russia"): print("Вы не гражданин, голосовать нельзя")
    elif (disqualification == True): print("Вы отстранены от голосования")
    else: print("Голосуйте")

voit(18, "Russia", False)
voit(20, "Russa", False)
voit(16, "Russia", False)
voit(20, "Russia", True)








