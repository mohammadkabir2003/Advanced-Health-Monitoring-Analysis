def filter_nondigits(data: list) -> list:
    # Initialize an empty list to store the cleaned data
    cleaned_data = []

    # Iterate over each item in the input data list
    for item in data:
        # Strip the newline character from the string (if any)
        item = item.strip("\n")

        # Check if the item consists only of digits (i.e., a valid number)
        if item.isdigit():
            # Convert the string to an integer and append it to the cleaned data list
            cleaned_data.append(int(item))

    # Return the cleaned data list containing only valid integers
    return cleaned_data
        
    pass
