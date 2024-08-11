def incr_by_one(value):
    if isinstance(value, int):
        return value + 1
    elif isinstance(value, str) and value.isdigit():
        return int(value) + 1
    else:
        print(f"Unable to perform incr for value: {value}")
