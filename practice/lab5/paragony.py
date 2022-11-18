import math


def split_price(price):
    price_zl = price // 100
    price_gr = price % 100

    return price_zl, price_gr


def get_description(name, price):
    price_parts = split_price(price)
    return f"Price of {name} is {price_parts[0]}.{price_parts[1]:02}"


def print_description(name, price):
    description = get_description(name, price)
    print(description)


def get_product():
    product_prices = {
        "Bananas": 499,
        "Oranges": 800,
        "Milk": 315,
        "Lollipop": 100,
        "Bread": 509,
    }

    name = input("Enter product name: ")
    amount = input("Enter amount: ")

    return name, int(amount*product_prices.get(name, 0))


def get_total_price(receipt):
    """
    Recieves list of items in receipt as input.
    Returns toal value of receipt.
    """
    total_value = 0

    for name, price in receipt:
        total_value += price

    return total_value


def format_price(price):
    zl, gr = split_price(price)
    return f"{zl}.{gr:02}"


def print_product(praduct, pos):
    name, price = praduct
    price = format_price(price)
    tax_group = get_tax_group(name)
    print(f"{pos:2}. {name:19} {price:>6} {tax_group}")


def print_receipt(date, reciept):
    """
    1. output date
    2. for each element in reciept output that element
    3. output line
    4. output summary
    """

    print(date)
    pos = 1
    tax_value = 0

    for product in reciept:
        print_product(product, pos)
        tax_value += calculate_praduct_tax(product)
        pos += 1

    print('-' * 32)

    total_value = get_total_price(reciept)
    formatted_value = format_price(total_value)
    formatted_tax_value = format_price(tax_value)
    formatted_total_wtax = format_price(total_value+tax_value)

    print(f"TAX: {formatted_tax_value:>25}")
    print(f"TOTAL: {formatted_value:>23}")
    print(f"TOTAL+TAX: {formatted_total_wtax:>19}")


def get_tax_group(name):
    tax_group_A = {"Milk", "Bread"}
    tax_group_B = {"Bananas", "Oranges"}

    if name in tax_group_A:
        return 'A'
    if name in tax_group_B:
        return 'B'

    return 'E'


def get_tax_percentage(tax_group):
    if 'A' == tax_group:
        return 0.12
    if 'B' == tax_group:
        return 0.08
    if 'E' == tax_group:
        return 0.22

    return 0


def calculate_praduct_tax(product):
    name = product[0]
    price = product[1]
    tax_multiplier = get_tax_percentage(get_tax_group(name))
    return math.ceil(price * tax_multiplier)


my_receipt = [
    ("Bananas", 499),
    ("Oranges", 1803),
    ("Milk", 315),
    ("Lollipop", 100)
]

if not my_receipt:
    print("Receipt is empty")
else:
    print_receipt("2022-11-3", my_receipt)
