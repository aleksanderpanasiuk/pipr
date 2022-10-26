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


# print_description("oranges", 847)
print_description("apples", 201)
