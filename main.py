def mutate_array(local_array_to_mutate):
    local_mutated_array = []
    for element in local_array_to_mutate:
        element = element * element
        local_mutated_array.append(element)
    return local_mutated_array


def print_array(array):
    for element in array:
        print(element)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array_to_mutate = [1, 2, 3, 4, 5, 6]
    print_array(array_to_mutate)
    mutated_array = mutate_array(array_to_mutate)
    print_array(mutated_array)

