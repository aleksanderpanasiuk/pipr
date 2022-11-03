def iterate_100():
    for i in range(100):
        if 0 == i % 15:
            print("fizzbuzz")
        elif 0 == i % 3:
            print("fizz")
        elif 0 == i % 5:
            print("buzz")
        else:
            print(i)


iterate_100()
