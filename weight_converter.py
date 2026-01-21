weight = float(input("Enter your weight: "))
unit = input("Kilogram(K) or Pound(P) ? ")


if unit == "K":
    weight *= 2.205
    print(f"Your weight is {round(weight, 3)} Pound")
elif unit == "P" :
    weight /= 2.205
    print(f"Your weight in Kilogram is {round(weight, 3)}")
else:
    print(f"{unit} was not valid")
