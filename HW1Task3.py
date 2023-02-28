print("Введите номер билета")
bilet = int(input())
if(bilet//100000 + bilet//10000%10 + bilet//1000%10 == bilet//100%10 + bilet//10%10 + bilet%10):
    print("Билет счастливый")
else:
    print("Билет не счастливый")