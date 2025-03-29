def filter_nondigits(data: list) -> list:
    cleaned_data = []
    for item in data:
        item = item.strip("\n")
        if item.isdigit():
            cleaned_data.append(int(item))

    return cleaned_data        
    pass
