def count_elements_above_average(input_list):
    average = list_average(input_list)
    elements_above_average = 0

    for element in input_list:
        if element > average:
            elements_above_average += 1

    return elements_above_average


def list_average(input_list):
    return sum(input_list) / len(input_list)


def elements_above_average(input_list):
    result = []

    for elements in input_list:
        try:
            result.append(count_elements_above_average(elements))

        except ZeroDivisionError:
            result.append("DZIELENIE PRZEZ ZERO")

        except TypeError:
            result.append("ZŁA WARTOŚĆ")

    return result


def main():
    my_list = [[1, 2, 3], [5, 6, 7], [], [3, 4, 5], ["12a", 1, 4]]
    print(elements_above_average(my_list))


if __name__ == "__main__":
    main()
