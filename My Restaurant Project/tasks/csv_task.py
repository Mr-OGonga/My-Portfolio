import csv
import time


# DRINKS FUNCTIONS
def drinks():
    with open('csv_data/drinks.csv', encoding='utf-8') as f:
        drinks = csv.DictReader(f, delimiter=',')
        for line in drinks:
            print(line)

def drinks_list():
    with open('csv_data/drinks.csv', encoding='utf-8') as f:
        drinks = csv.DictReader(f, delimiter=',')
        for line in drinks:
            print(f'{line["Drink"]}: {line["Cost"]} - {line["Description"]}')

def drinks_check():
    with open('csv_data/drinks.csv', encoding='utf-8') as f:
        drinks = csv.DictReader(f, delimiter=',')
        drink_list = []
        for line in drinks:
            drink_list.append(line["Drink"].lower())
        return drink_list

def want_another_drink_func():
    want_another_drink = input("\nWould you like another drink? yes/no: ")
    want_another_drink = yes_no(want_another_drink)

    while want_another_drink.lower() not in choices:
        want_another_drink = input("\nThat is an invalid choice, please select \"yes\" or \"no\": ")
        want_another_drink = yes_no(want_another_drink)

    if want_another_drink.lower() == "yes" or want_another_drink.lower() == "y":
        drink = input("\nWhat drink would you like: ")
        camel_drink = camel_case(drink)
    
        while drink not in drinks_check():
            drink = input("Sorry, this drink is unavailable, please select a drink from the list provided above: ")
            camel_drink = camel_case(drink)

        print(f"\nExcellent choice, here is your {camel_drink}!")
        ordered.append(camel_drink)

        order_string = ", ".join(ordered[:-1])
        print(f"\n>> You have ordered ==> {order_string} and {ordered[-1]}")

    else:
        return False


def drinks_cost():
    with open('csv_data/drinks.csv', encoding='utf-8') as f:
        drinks = csv.DictReader(f, delimiter=',')
        for line in drinks:
            print(line["Cost"])



# STARTERS FUNCTIONS
def starters():
    with open('csv_data/starters.csv', encoding='utf-8') as f:
        starters = csv.DictReader(f, delimiter=',')
        for line in starters:
            print(line)


def starters_list():
    with open('csv_data/starters.csv', encoding='utf-8') as f:
        starters = csv.DictReader(f, delimiter=',')
        for line in starters:
            print(f'{line["Starter"]}: {line["Cost"]} - {line["Description"]}, {line["Calories"]}')

def starters_check():
    with open('csv_data/starters.csv', encoding='utf-8') as f:
        starters = csv.DictReader(f, delimiter=',')
        starter_list = []
        for line in starters:
            starter_list.append(line["Starter"].lower())
        return starter_list

def want_another_starter_func():
    want_another_starter = input("\nWould you like another starter? yes/no: ")
    want_another_starter = yes_no(want_another_starter)

    while want_another_starter.lower() not in choices:
        want_another_starter = input("\nThat is an invalid choice, please select \"yes\" or \"no\": ")
        want_another_starter = yes_no(want_another_starter)

    if want_another_starter.lower() == "yes" or want_another_starter.lower() == "y":
        starter = input("\nWhat starter would you like: ")
        camel_starter = camel_case(starter)
    
        while starter not in starters_check():
            starter = input("Sorry, this starter is unavailable, please select a starter from the list provided above: ")
            camel_starter = camel_case(starter)

        print(f"\nExcellent choice, here is your {camel_starter}!")
        ordered.append(camel_starter)

        order_string = ", ".join(ordered[:-1])
        print(f"\n>> You have ordered ==> {order_string} and {ordered[-1]}")

    else:
        return False



# PIZZAS FUNCTIONS
def pizzas():
    with open('csv_data/pizzas.csv', encoding='utf-8') as f:
        pizzas = csv.DictReader(f, delimiter=',')
        for line in pizzas:
            print(line)

def pizzas_list():
    with open('csv_data/pizzas.csv', encoding='utf-8') as f:
        pizzas = csv.DictReader(f, delimiter=',')
        for line in pizzas:
            print(f'{line["Pizza"]}: {line["Cost"]} - {line["Description"]}, {line["Calories"]}')

def pizzas_check():
    with open('csv_data/pizzas.csv', encoding='utf-8') as f:
        pizzas = csv.DictReader(f, delimiter=',')
        pizza_list = []
        for line in pizzas:
            pizza_list.append(line["Pizza"].lower())
        return pizza_list

def want_another_pizza_func():
    want_another_pizza = input("\nWould you like another pizza? yes/no: ")
    want_another_pizza = yes_no(want_another_pizza)

    while want_another_pizza.lower() not in choices:
        want_another_pizza = input("\nThat is an invalid choice, please select \"yes\" or \"no\": ")
        want_another_pizza = yes_no(want_another_pizza)

    if want_another_pizza.lower() == "yes" or want_another_pizza.lower() == "y":
        pizza = input("\nWhat pizza would you like: ")
        camel_pizza = camel_case(pizza)
    
        while pizza not in pizzas_check():
            pizza = input("Sorry, this pizza is unavailable, please select a pizza from the list provided above: ")
            camel_pizza = camel_case(pizza)

        print(f"\nExcellent choice, here is your {camel_pizza}!")
        ordered.append(camel_pizza)

        order_string = ", ".join(ordered[:-1])
        print(f"\n>> You have ordered ==> {order_string} and {ordered[-1]}")

    else:
        return False



# PASTAS FUNCTIONS
def pastas():
    with open('csv_data/pastas.csv', encoding='utf-8') as f:
        pastas = csv.DictReader(f, delimiter=',')
        for line in pastas:
            print(line)

def pastas_list():
    with open('csv_data/pastas.csv', encoding='utf-8') as f:
        pastas = csv.DictReader(f, delimiter=',')
        for line in pastas:
            print(f'{line["Pasta"]}: {line["Cost"]} - {line["Description"]}, {line["Calories"]}')

def pastas_check():
    with open('csv_data/pastas.csv', encoding='utf-8') as f:
        pastas = csv.DictReader(f, delimiter=',')
        pasta_list = []
        for line in pastas:
            pasta_list.append(line["Pasta"].lower())
        return pasta_list

def want_another_pasta_func():
    want_another_pasta = input("\nWould you like another pasta? yes/no: ")
    want_another_pasta = yes_no(want_another_pasta)

    while want_another_pasta.lower() not in choices:
        want_another_pasta = input("\nThat is an invalid choice, please select \"yes\" or \"no\": ")
        want_another_pasta = yes_no(want_another_pasta)

    if want_another_pasta.lower() == "yes" or want_another_pasta.lower() == "y":
        pasta = input("\nWhat pasta would you like: ")
        camel_pasta = camel_case(pasta)
    
        while pasta not in pastas_check():
            pasta = input("Sorry, this pasta is unavailable, please select a pasta from the list provided above: ")
            camel_pasta = camel_case(pasta)

        print(f"\nExcellent choice, here is your {camel_pasta}!")
        ordered.append(camel_pasta)

        order_string = ", ".join(ordered[:-1])
        print(f"\n>> You have ordered ==> {order_string} and {ordered[-1]}")

    else:
        return False



# DESSERTS FUNCTIONS
def desserts():
    with open('csv_data/desserts.csv', encoding='utf-8') as f:
        desserts = csv.DictReader(f, delimiter=',')
        for line in desserts:
            print(line)

def desserts_list():
    with open('csv_data/desserts.csv', encoding='utf-8') as f:
        desserts = csv.DictReader(f, delimiter=',')
        for line in desserts:
            print(f'{line["Dessert"]}: {line["Cost"]} - {line["Description"]}, {line["Calories"]}')

def desserts_check():
    with open('csv_data/desserts.csv', encoding='utf-8') as f:
        desserts = csv.DictReader(f, delimiter=',')
        dessert_list = []
        for line in desserts:
            dessert_list.append(line["Dessert"].lower())
        return dessert_list

def want_another_dessert_func():
    want_another_dessert = input("\nWould you like another dessert? yes/no: ")
    want_another_dessert = yes_no(want_another_dessert)

    while want_another_dessert.lower() not in choices:
        want_another_dessert = input("\nThat is an invalid choice, please select \"yes\" or \"no\": ")
        want_another_dessert = yes_no(want_another_dessert)

    if want_another_dessert.lower() == "yes" or want_another_dessert.lower() == "y":
        dessert = input("\nWhat dessert would you like: ")
        camel_dessert = camel_case(dessert)
    
        while dessert not in desserts_check():
            dessert = input("Sorry, this dessert is unavailable, please select a dessert from the list provided above: ")
            camel_dessert = camel_case(dessert)

        print(f"\nExcellent choice, here is your {camel_dessert}!")
        ordered.append(camel_dessert)

        order_string = ", ".join(ordered[:-1])
        print(f"\n>> You have ordered ==> {order_string} and {ordered[-1]}")

    else:
        return False



# CAMEL CASE
def camel_case(order):
    split_order = order.split()
    return_order = " ".join(word[0].upper() + word[1:].lower() for word in split_order)
    # return_order = " ".join(word.capitalize() for word in split_order)
    return return_order


# CHOICES
choices = ["yes", "y", "no", "n"]
ordered = []

# yes/no FUNCTION
def yes_no(answer):
    if "yes" in answer.lower():
        answer = "yes"
    elif "no" in answer.lower():
        answer = "no"
    return answer


# WELCOME
print("Welcome to Our Restaurant, please let us know what you would like to order...\n")

# DRINKS
want_a_drink = input("Firstly, would you like a drink? yes/no: ")
want_a_drink = yes_no(want_a_drink)

while want_a_drink.lower() not in choices:
    want_a_drink = input("\nThat is an invalid choice, please select \"yes\" or \"no\": ")
    want_a_drink = yes_no(want_a_drink)

if want_a_drink.lower() == "yes" or want_a_drink.lower() == "y":
    print("\nDrinks Menu")
    print("------------------------------")
    drinks_list()

    drink = input("\nHere is our drinks menu, please select from the options above: ").lower()
    camel_drink = camel_case(drink)
    
    while drink not in drinks_check():
        drink = input("Sorry, this drink is unavailable, please select a drink from the list provided above: ").lower()
        camel_drink = camel_case(drink)

    print(f"\nExcellent choice, here is your {camel_drink}!")
    ordered.append(camel_drink)

    if len(ordered) != 0:
        print(f"\n>> You have ordered ==> {ordered[0]}")


    # WANT ANOTHER DRINK?
    want_another_drink = "yes"

    while want_another_drink.lower() == "yes" or want_another_drink.lower() == "y":
        if want_another_drink_func() == False:
            print("Okay...\n")
            break

else:
    print("Okay...")


# STARTERS
want_a_starter = input("\nNow, would you like a starter? yes/no: ")
want_a_starter = yes_no(want_a_starter)


while want_a_starter.lower() not in choices:
    want_a_starter = input("\nThat is an invalid choice, please select \"yes\" or \"no\": ")
    want_a_starter = yes_no(want_a_starter)

if want_a_starter.lower() == "yes" or want_a_starter.lower() == "y":
    print("\nStarters Menu")
    print("------------------------------")
    starters_list()

    starter = input("\nHere is our starters menu, please select from the options above: ").lower()
    camel_starter = camel_case(starter)
    
    while starter not in starters_check():
        starter = input("Sorry, this starter is unavailable, please select a starter from the list provided above: ").lower()
        camel_starter = camel_case(starter)

    print(f"\nWonderful choice, here is your {camel_starter}!")
    ordered.append(camel_starter)

    if len(ordered) == 1:
        print(f"\n>> You have ordered ==> {ordered[0]}")
    else:
        order_string = ", ".join(ordered[:-1])
        print(f"\n>> You have ordered ==> {order_string} and {ordered[-1]}")

    # ANOTHER STARTER
    want_another_starter = "yes"

    while want_another_starter.lower() == "yes" or want_another_starter.lower() == "y":
        if want_another_starter_func() == False:
            print("Alright...\n")
            break

else:
    print("Alright...")



# PIZZAS
want_a_pizza = input("\nThirdly, would you like a pizza? yes/no: ")
want_a_pizza = yes_no(want_a_pizza)

while want_a_pizza.lower() not in choices:
    want_a_pizza = input("\nThat is an invalid choice, please select \"yes\" or \"no\": ")
    want_a_pizza = yes_no(want_a_pizza)

if want_a_pizza.lower() == "yes" or want_a_pizza.lower() == "y":
    print("\nPizzas Menu")
    print("------------------------------")
    pizzas_list()

    pizza = input("\nHere is our pizzas menu, please select from the options above: ").lower()
    camel_pizza = camel_case(pizza)

    while pizza not in pizzas_check():
        pizza = input("Sorry, this pizza is unavailable, please select a pizza from the list provided above: ").lower()
        camel_pizza = camel_case(pizza)

    print(f"\nIncredible choice, here is your {camel_pizza}!")
    ordered.append(camel_pizza)

    if len(ordered) == 1:
        print(f"\n>> You have ordered ==> {ordered[0]}")
    else:
        order_string = ", ".join(ordered[:-1])
        print(f"\n>> You have ordered ==> {order_string} and {ordered[-1]}")

    # ANOTHER pizza
    want_another_pizza = "yes"

    while want_another_pizza.lower() == "yes" or want_another_pizza.lower() == "y":
        if want_another_pizza_func() == False:
            print("Sure...\n")
            break

else:
    print("Sure...")



# PASTAS
want_a_pasta = input("\nWould you like a pasta? yes/no: ")
want_a_pasta = yes_no(want_a_pasta)

while want_a_pasta.lower() not in choices:
    want_a_pasta = input("\nThat is an invalid choice, please select \"yes\" or \"no\": ")
    want_a_pasta = yes_no(want_a_pasta)

if want_a_pasta.lower() == "yes" or want_a_pasta.lower() == "y":
    print("\nPastas Menu")
    print("------------------------------")
    pastas_list()

    pasta = input("\nHere is our pastas menu, please select from the options above: ").lower()
    camel_pasta = camel_case(pasta)

    while pasta not in pastas_check():
        pasta = input("Sorry, this pasta is unavailable, please select a pasta from the list provided above: ").lower()
        camel_pasta = camel_case(pasta)

    print(f"\nFantastic choice, here is your {camel_pasta}!")
    ordered.append(camel_pasta)

    if len(ordered) == 1:
        print(f"\n>> You have ordered ==> {ordered[0]}")
    else:
        order_string = ", ".join(ordered[:-1])
        print(f"\n>> You have ordered ==> {order_string} and {ordered[-1]}")

    # ANOTHER pasta
    want_another_pasta = "yes"

    while want_another_pasta.lower() == "yes" or want_another_pasta.lower() == "y":
        if want_another_pasta_func() == False:
            print("Excellent...\n")
            break

else:
    print("Excellent...")



# DESSERTS
want_a_dessert = input("\nFinally, would you like a dessert? yes/no: ")
want_a_dessert = yes_no(want_a_dessert)

while want_a_dessert.lower() not in choices:
    want_a_dessert = input("\nThat is an invalid choice, please select \"yes\" or \"no\": ")
    want_a_dessert = yes_no(want_a_dessert)

if want_a_dessert.lower() == "yes" or want_a_dessert.lower() == "y":
    print("\nDesserts Menu")
    print("------------------------------")
    desserts_list()

    dessert = input("\nHere is our desserts menu, please select from the options above: ").lower()
    camel_dessert = camel_case(dessert)

    while dessert not in desserts_check():
        dessert = input("Sorry, this dessert is unavailable, please select a dessert from the list provided above: ").lower()
        camel_dessert = camel_case(dessert)

    print(f"\nAmazing choice, here is your {camel_dessert}!")
    ordered.append(camel_dessert)

    if len(ordered) == 1:
        print(f"\n>> You have ordered ==> {ordered[0]}")
    else:
        order_string = ", ".join(ordered[:-1])
        print(f"\n>> You have ordered ==> {order_string} and {ordered[-1]}")

    # ANOTHER dessert
    want_another_dessert = "yes"

    while want_another_dessert.lower() == "yes" or want_another_dessert.lower() == "y":
        if want_another_dessert_func() == False:
            print("Lovely stuff...\n")
            break

print("\nThis signals the end of your meal. Bon appétit!!")


# WAIT 7 SECONDS
time.sleep(1.65)
print("..... 🥗")
time.sleep(1.65)
print(".......... 🍝")
time.sleep(1.65)
print("............... 🍮")
time.sleep(1.65)
    

# BILL
total = 0

# drinks
ordered_drinks = ""
with open('csv_data/drinks.csv', encoding='utf-8') as f:
    drinks = csv.DictReader(f, delimiter=',')
    for line in drinks:
        for item in ordered:
            if item == line["Drink"]:
                ordered_drinks += "".join(f'{line["Drink"]}\t{line["Cost"]}') + "\n"
                total += round(float(line["Cost"].split("£")[1]), 2)

# starters
ordered_starters = ""
with open('csv_data/starters.csv', encoding='utf-8') as f:
    starters = csv.DictReader(f, delimiter=',')
    for line in starters:
        for item in ordered:
            if item == line["Starter"]:
                ordered_starters += "".join(f'{line["Starter"]}\t{line["Cost"]}') + "\n"
                total += round(float(line["Cost"].split("£")[1]), 2)

# pizzas
ordered_pizzas = ""
with open('csv_data/pizzas.csv', encoding='utf-8') as f:
    pizzas = csv.DictReader(f, delimiter=',')
    for line in pizzas:
        for item in ordered:
            if item == line["Pizza"]:
                ordered_pizzas += "".join(f'{line["Pizza"]}\t{line["Cost"]}') + "\n"
                total += round(float(line["Cost"].split("£")[1]), 2)

# pastas
ordered_pastas = ""
with open('csv_data/pastas.csv', encoding='utf-8') as f:
    pastas = csv.DictReader(f, delimiter=',')
    for line in pastas:
        for item in ordered:
            if item == line["Pasta"]:
                ordered_pastas += "".join(f'{line["Pasta"]}\t{line["Cost"]}') + "\n"
                total += round(float(line["Cost"].split("£")[1]), 2)

# desserts
ordered_desserts = ""
with open('csv_data/desserts.csv', encoding='utf-8') as f:
    desserts = csv.DictReader(f, delimiter=',')
    for line in desserts:
        for item in ordered:
            if item == line["Dessert"]:
                ordered_desserts += "".join(f'{line["Dessert"]}\t{line["Cost"]}') + "\n"
                total += round(float(line["Cost"].split("£")[1]), 2)



# SERVICE CHARGE
bill_choice = input("\nI hope you enjoyed your meal, you made some great choices!! Would you like to see your bill? yes/no: ")
yes_no(bill_choice)

while bill_choice.lower() not in choices:
    bill_choice = input("\nPlease choose \"yes\" or \"no\". Would you like to pay your bill?: ")
    yes_no(bill_choice)

if bill_choice.lower() == "no" or bill_choice.lower() == "n":
    print("\nSorry, you're not allowed to run out on your bill. A 50% service charge has been added!!!")
    grand_total = round(total * (100 + float("50")) / 100, 2)
    service_charge = True
    tip_amount = "50"
else:
    print("\nExcellent, we thank you kindly for your custom.")
    service_charge = False

    # ADD A TIP?
    optional_tip = input("\nWould you like to add a tip? yes/no: ")
    yes_no(optional_tip)

    while optional_tip.lower() not in choices:
        optional_tip = input("\nThat is an invalid choice, please select \"yes\" or \"no\": ")
        yes_no(optional_tip)
    

    if optional_tip.lower() == "yes" or optional_tip.lower() == "y":
        service_charge = True
        tip_amount = input("\nWhat percentage(%) tip would you like to give? Please type a nummber: ")

        while not tip_amount.isdigit():
            tip_amount = input("\nPlease type the percentage(%) amount you would like to give as a tip in number form: ")

        grand_total = round(total * (100 + float(tip_amount)) / 100, 2)
    else:
        grand_total = total



# GIVE BILL
print(f"""\n
-----------------------
BILL
-----------------------
""")


if ordered_drinks != "":
    print(f"""-----------------------
DRINKS
-----------------------
{ordered_drinks}""")

if ordered_starters != "":
    print(f"""-----------------------
STARTERS
-----------------------
{ordered_starters}""")

if ordered_pizzas != "":
    print(f"""-----------------------
PIZZAS
-----------------------
{ordered_pizzas}""")

if ordered_pastas != "":
    print(f"""-----------------------
PASTAS
-----------------------
{ordered_pastas}""")

if ordered_desserts != "":
    print(f"""-----------------------
DESSERTS
-----------------------
{ordered_desserts}""")

if service_charge == True:
    print(f"""-----------------------
Total: £{total:.2f}
Service Charge: {tip_amount}%""")

print(f"""-----------------------
GRAND TOTAL: £{grand_total:.2f}
-----------------------
""")
