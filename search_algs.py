def binary_search(arr: list, elem: int, start_index=0, counter=0):
    sep = int(len(arr) / 2)

    counter += 1
    if arr[sep] > elem:
        return binary_search(arr[:sep], elem, start_index, counter)

    counter += 1
    if arr[sep] < elem:
        return binary_search(arr[sep:], elem, start_index + sep, counter)

    return start_index + sep, counter


def interpolation_search(arr: list, elem: int, start_index=0, counter=0):
    sep_multiplier = (elem - arr[0]) / (arr[-1] - arr[0])

    counter += 1
    if sep_multiplier == 1:
        return start_index + len(arr) - 1, counter

    sep = int(len(arr) * sep_multiplier)

    counter += 1
    if arr[sep] > elem:
        return interpolation_search(arr[:sep], elem, start_index, counter)

    counter += 1
    if arr[sep] < elem:
        return interpolation_search(arr[(sep + 1):], elem, start_index + sep + 1, counter)

    return (start_index + sep), counter
