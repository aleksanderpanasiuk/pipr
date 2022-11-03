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
    name = input("Enter product name: ")
    price = input("Enter price: ")

    return name, int(price)


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

    for product in reciept:
        print_product(product, pos)
        pos += 1

    print('-' * 32)

    total_value = get_total_price(reciept)
    formatted_value = format_price(total_value)
    print(f"TOTAL: {formatted_value:>23}")


def get_tax_group(name):
    tax_group_A = {"Milk", "Bread"}
    tax_group_B = {"Bananas", "Oranges"}

    if name in tax_group_A:
        return 'A'
    if name in tax_group_B:
        return 'B'

    return 'E'


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
