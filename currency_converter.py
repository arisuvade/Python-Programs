print("Currency Converter")
print("As of September 7, 2022")

print("""Philippine Peso(PHP)
United States Dollar(USD)
Euro(EUR)
Japanese Yen(JPY)
Korean Won(KRW)
Indian Rupee(INR)""")

money = float(input("How much? "))
currency = input("What currency? ").lower
convert_to = input("Convert to? ").lower

# philippine peso
if currency() == "php":
    if convert_to() == "usd":
        conversion = money / 57.22
        print(str(conversion) + " US Dollars")
    elif convert_to() == "eur":
        conversion = money / 56.59
        print(str(conversion) + " Euros")
    elif convert_to() == "jpy":
        conversion = money * 2.53
        print(str(conversion) + " Yen")
    elif convert_to() == "krw":
        conversion = money * 24.27
        print(str(conversion) + " Won")
    elif convert_to() == "inr":
        conversion = money * 1.40
        print(str(conversion) + " Rupees")

# us dollar
if currency() == "usd":
    if convert_to() == "php":
        conversion = money * 57.22
        print(str(conversion) + " Pesos")
    elif convert_to() == "eur":
        conversion = money * 1.01
        print(str(conversion) + " Euros")
    elif convert_to() == "jpy":
        conversion = money * 144.91
        print(str(conversion) + " Yen")
    elif convert_to() == "krw":
        conversion = money * 1388.33
        print(str(conversion) + " Won")
    elif convert_to() == "inr":
        conversion = money * 79.93
        print(str(conversion) + " Rupees")

# euro
if currency() == "eur":
    if convert_to() == "php":
        conversion = money * 56.61
        print(str(conversion) + " Pesos")
    elif convert_to() == "usd":
        conversion = money * 1.01
        print(str(conversion) + " US Dollars")
    elif convert_to() == "jpy":
        conversion = money * 143.32
        print(str(conversion) + " Yen")
    elif convert_to() == "krw":
        conversion = money * 1373.93
        print(str(conversion) + " Won")
    elif convert_to() == "inr":
        conversion = money * 79.10
        print(str(conversion) + " Rupees")

# japanese yen
if currency() == "jpy":
    if convert_to() == "php":
        conversion = money / 2.53
        print(str(conversion) + " Pesos")
    elif convert_to() == "usd":
        conversion = money / 144.79
        print(str(conversion) + " US Dollars")
    elif convert_to() == "eur":
        conversion = money / 143.32
        print(str(conversion) + " Euros")
    elif convert_to() == "krw":
        conversion = money * 9.58
        print(str(conversion) + " Won")
    elif convert_to() == "inr":
        conversion = money * 1.81
        print(str(conversion) + " Rupees")

# korean won
if currency() == "krw":
    if convert_to() == "php":
        conversion = money / 24.27
        print(str(conversion) + " Pesos")
    elif convert_to() == "usd":
        conversion = money / 1387.34
        print(str(conversion) + " US Dollars")
    elif convert_to() == "eur":
        conversion = money / 1375.11
        print(str(conversion) + " Euros")
    elif convert_to() == "jpy":
        conversion = money / 9.58
        print(str(conversion) + " Yen")
    elif convert_to() == "inr":
        conversion = money / 17.36
        print(str(conversion) + " Rupees")

# indian rupee
if currency() == "inr":
    if convert_to() == "php":
        conversion = money / 1.40
        print(str(conversion) + " Pesos")
    elif convert_to() == "usd":
        conversion = money / 79.86
        print(str(conversion) + " US Dollars")
    elif convert_to() == "eur":
        conversion = money / 79.17
        print(str(conversion) + " Euros")
    elif convert_to() == "jpy":
        conversion = money * 1.81
        print(str(conversion) + " Yen")
    elif convert_to() == "krw":
        conversion = money * 17.36
        print(str(conversion) + " Won")

# add if and elif statement if you wanna add currencies

else:
    print("""Read the currency at the top
Use only the iso code""")
