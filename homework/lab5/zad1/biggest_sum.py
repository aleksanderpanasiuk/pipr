def biggest_sum(substring_length, list):
    if substring_length > len(list):
        substring_length = len(list)

    current_sum = sum(list[:substring_length])
    max_sum = current_sum

    for i in range(0, len(list)-substring_length):
        current_sum += list[i+substring_length]
        current_sum -= list[i]

        max_sum = max(max_sum, current_sum)

    return max_sum
