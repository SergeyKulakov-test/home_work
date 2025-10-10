def voit(age: bool, citizenship: bool, disqualification: bool):
    if age and citizenship and not disqualification:
        print("Голосуйте")
    else: print("Вы не можете голосовать")

voit(True, True, False)
voit(True, False, True)
voit(False, True, True)
voit(True, True, True)








