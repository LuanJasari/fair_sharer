def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in "values" gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """
    values = list(values)  

    n = len(values)

    for _ in range(num_iterations):
        max_index = values.index(max(values))
        max_value = values[max_index]

        give_amount = max_value * share

        left_index = (max_index - 1) % n
        right_index = (max_index + 1) % n

        new_values = values.copy()
        new_values[max_index] -= 2 * give_amount
        new_values[left_index] += give_amount
        new_values[right_index] += give_amount

        values = new_values

    return values
    