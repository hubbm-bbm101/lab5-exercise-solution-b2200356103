import random
number = random.randint(1, 100)
print("sayı 1 ila 100 arasında.")
tahmin = 0
while (tahmin != number):
    tahmin = int(input("bir sayı tut kafandan"))
    if tahmin>number:
        print("tahmininiz sayıdan büyük, daha kükçük bir şey söyleyin!")
    elif tahmin<number:
        print("tahiminiz syaıdan küçük, daha büyük bir şey söyleyin!")
    else:
        print("gotchaa, sayı:" + str(number))