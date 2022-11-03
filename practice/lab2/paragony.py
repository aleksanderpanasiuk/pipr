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


def print_reciepts(date, reciept):
    """
    1. output date
    2. for each element in reciept output that element
    3. output line
    4. output summary
    """
    print(date)
    pos = 1

    for name, price in reciept:
        price = format_price(price)
        print(f"{pos:2}. {name:19} {price:>6}")
        pos += 1

    print('-' * 30)

    total_value = get_total_price(reciept)
    formatted_value = format_price(total_value)
    print(f"TOTAL: {formatted_value:>23}")


my_receipt = [
    ("Bananas", 499),
    ("Oranges", 1803),
    ("Milk", 315)
]

print_reciepts("2022-11-3", my_receipt)
