def average(data: list) -> float:
    """
    Calculate the average value of the list of integers.

    Args:
        data (list[int]): A list of integers representing heart rate samples.
    
    Returns:
        float: The average of the integers in the list, rounded to two decimal places.
        If the list is empty, returns an empty list.
    """
    if len(data) == 0:
        return []  # Return empty list if the data is empty
    
    total = 0

    for item in data:
        total += item  # Add each item in the data list to total

    avg = total / len(data)  # Calculate the average by dividing the total by the number of items

    return round(avg, 2)  # Return the rounded average to two decimal places


def maximum(data: list) -> float:
    """
    Calculate the maximum value in the list of integers.

    Args:
        data (list[int]): A list of integers representing heart rate samples.
    
    Returns:
        float: The maximum value from the list. If the list is empty, returns an empty list.
    """
    if not data:
        return []  # Return an empty list if the data is empty
    
    max_val = data[0]  # Initialize the max value as the first item in the list

    for item in data:
        if item > max_val:
            max_val = item  # Update max value if a larger value is found

    return max_val  # Return the maximum value


def variance(data: list) -> float:
    """
    Calculate the population variance of the list of integers.

    Args:
        data (list[int]): A list of integers representing heart rate samples.
    
    Returns:
        float: The population variance, rounded to two decimal places. 
        If the list is empty, returns an empty list.
    """
    if len(data) == 0:
        return []  # Return empty list if the data is empty
    
    aver = average(data)  # Get the average of the data
    sum_sq_diff = 0  # Initialize the sum of squared differences

    for item in data:
        sum_sq_diff += (item - aver) ** 2  # Calculate squared difference from the average

    var = sum_sq_diff / len(data)  # Calculate variance by dividing the sum of squared differences by the number of items

    return round(var, 2)  # Return the rounded variance to two decimal places


def standard_deviation(data: list) -> float:
    """
    Calculate the population standard deviation of the list of integers.

    Args:
        data (list[int]): A list of integers representing heart rate samples.
    
    Returns:
        float: The population standard deviation, rounded to two decimal places.
        If the list is empty, returns an empty list.
    """
    if not data:
        return []  # Return empty list if the data is empty
    
    var = variance(data)  # Get the variance of the data

    return round(var ** 0.5, 2)  # Return the square root of the variance (standard deviation), rounded to two decimal places
