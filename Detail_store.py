#Версия онлайн-магазина 0.9____________________________________________________________________________
import json
import math 
import colorama 
from colorama import init
init()
from colorama import Fore, Back, Style

#Ввод данных (имя,деньги)_____________________________________________________________________________
print(Fore.BLUE)
user_name = input("Input username -  ")
print(Fore.GREEN)
user_password = input("Input user password of cabinet - ")
#user_moneny = float(input("Input user money - "))


#Логины и пароли от кабинетов 
with open('pasha1121.json') as json_file:
    pass_user = json.load(json_file)

#Проверка и вход в кабинет____________________________________________________________________________

        print("You entered to cabinet")
else:
        print(" Entering failed. \n Wrong password or username! ")

#Пополнение суммы счёта ______________________________________________________________________________
print(Fore.WHITE)
print("Replenish the account! The amount of money in the account = 0 EUR")

#Количество денег на пополнение _______________________________________________________________________
ammount_money_to_replein = float(input("Input quantity of money that you want to replenish -   "))

print(Fore.RED)
numbers_of_creditcard = input("Input numbers of your credit card  -   ")
if len(numbers_of_creditcard) == 16:
    print("✓")
else:
    print("Invalid input!")


print(Fore.WHITE)
data_on_card = input("Input date on credit card. \n It must be 4 numbers on main side of card -    ")
if len(data_on_card) == 4:
    print("✓")
else:
    print("Invalid input!")

print(Fore.WHITE)
cvv_code = input("Input CVV of card on back side of card. \n It must be 3 numbers -   ")
if len(cvv_code) == 3:
    print("✓")
else:
    print("Invalid input!")

print("Your account has been replenished on", ammount_money_to_replein,"EUR")

#Детали для машин ___________________________________________________________________________

class car_window():
    def __init__(self,price,color,model):
        self.price = price 
        self.color = color 
        self.model = model 

    def skoda(self):
        print("Skoda window characteristic : " + self.price,self.color,self.model)

    def mercedes(self):
        print("Mercedes-Bens window characteristic : " + self.price,self.color,self.model)

    def lada(self):
        print("Lada window characteristic : " + self.price,self.color,self.model)

class car_engine():
    def __init__(self,price,model,liters):
        self.price = price 
        self.model = model
        self.liters = liters 

    def BMW(self):
        print("BMW engine characteristic : " + self.price,self.model,self.liters)

    def Audi(self):
        print("Audi engine characteristic : " + self.price,self.model,self.liters)

    def Lamborgini(self):
        print("Lamborgini engine characteristic : " + self.price,self.model,self.liters)

skoda_window_ = car_window("100 EUR","Black","Skoda                    For input(SK)    =  ")
mercedes_window_ = car_window("300 EUR","Black","Mercedes         For input(MB)    =  ")
lada_window = car_window("20 EUR","Red","Lada                         For input(LA)    =  ")
bmw_engine = car_engine("3000 EUR","BMW","3 Liters                    For input(BMW)   =  ")
audi_engine = car_engine("4500 EUR","Audi","4.3 Liters                For input(AU)    =    ")
lamborgigni_engine = car_engine("12000 EUR","Lamborgini","12 Liters    For input(LB)    =  ")

skoda_window_.skoda()
mercedes_window_.mercedes()
lada_window.lada()
bmw_engine.BMW()
audi_engine.Audi()
lamborgigni_engine.Lamborgini()



SK = 100
MB = 350
LA = 20 
BMW = 3000
AU = 4500
LB = 12000

#Выбор детали и её количества _________________________________________________________________________
input_type_of_item = input("Input MODEL of item in list -  ")
if input_type_of_item == 'SK':
    print("You can buy this item,how many items?")
    number_of_items = int(input("Input number of items = "))
    items_cost = (skoda_window*number_of_items + "EUR")

elif input_type_of_item == "MB":
    print("You can buy this item,how many items?")
    number_of_items = int(input("Input number of items = "))
    items_cost = MB*number_of_items
elif input_type_of_item == "BMW":
    print("You can buy this item,how many items?")
    number_of_items = int(input("Input number of items = "))
    items_cost = print(BMW*number_of_items + "EUR")
elif input_type_of_item == "LA":
    print("You can buy this item,how many items?")
    number_of_items = int(input("Input number of items = "))
    items_cost = print(LA*number_of_items + "EUR")
elif input_type_of_item == "AU":
    print("You can buy this item,how many items?")
    number_of_items = int(input("Input number of items = "))
    items_cost = print(AU*number_of_items + "EUR")
elif input_type_of_item == "LB":
    print("You can buy this item,how many items?")
    number_of_items = int(input("Input number of items = "))
    items_cost = print(LB*number_of_items + "EUR")

else:
    print("Wrong name of item!")


#Вывод ____________________________________________________________________________________________________________________
if items_cost <= ammount_money_to_replein:
    account_balance = print(ammount_money_to_replein - items_cost,"EUR")
    print("Thanks for purchase, come again. \n Our support is on car_items@gmail.com or on car_items.com \n Califoenia,Backham street 0043")
else:
    print("Not enough money!Replenish the account,please!")