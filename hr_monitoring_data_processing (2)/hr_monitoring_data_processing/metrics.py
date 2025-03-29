def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    if len(data) == 0:
        return[]
    
    total = 0

    for item in data:
        total += item

    avg = total / len(data)

    return round(avg, 2)
    ...


def maximum(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    """
    if not data:
        return []
    
    max = data[0]

    for item in data:
        if item > max:
            max = item

    return max
    pass


def variance(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    (calculate population variance)
    """
    if len(data) == 0:
        return []
    aver = average(data)
    sum = 0

    for item in data:
        sum += (item - aver) ** 2

    var = sum / len(data)

    return round(var, 2)
    pass


def standard_deviation(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    (calculate population standard deviation)
    """
    if not data:
        return []
    var = variance(data)

    return round(var ** 0.5, 2)

    pass
