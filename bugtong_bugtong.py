print("Bugtong Bugtong")
print("---------------")

rur = input("Handa ka na ba? (y/n) ")
print("---------------------")
score = 0

if rur == "y":
    sagot1 = input("""Bugtong: Heto na ang magkapatid, nag-uunahang pumanhik.
Sagot: """).lower()
    if sagot1 == "paa":
        print("Tama!")
        score += 1
    else:
        print("Mali!")
    sagot2 = input("""Bugtong: Ate mo, ate ko, ate ng lahat ng tao.
Sagot: """).lower()
    if sagot2 == "atis":
        print("Tama!")
        score += 1
    else:
        print("Mali!")
    sagot3 = input("""Bugtong: Dumaan ang hari, nagkagatan ang mga pari.
Sagot: """).lower()
    if sagot3 == "zipper":
        print("Tama!")
        score += 1
    else:
        print("Mali!")
    sagot4 = input("""Bugtong: Kung kailan mo pinatay, saka pa humaba ang buhay.
Sagot: """).lower()
    if sagot4 == "kandila":
        print("Tama!")
        score += 1
    else:
        print("Mali!")
    sagot5 = input("""Bugtong: Nagbibigay na, sinasakal pa.
Sagot: """).lower()
    if sagot5 == "bote":
        print("Tama!")
        score += 1
    else:
        print("Mali!")
elif rur == "n":
    print("Sige... bye!")
else:
    print("Type (y) kung handa ka na at (n) kung hindi pa.")
print("-------------------------------")
print("Ikaw ay naka " + str(score) + " sa 5 na bugtong.")
