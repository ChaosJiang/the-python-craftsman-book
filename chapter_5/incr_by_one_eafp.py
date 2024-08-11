def incr_by_one(value) -> int | None:
    try:
        return int(value) + 1　
    except (TypeError, ValueError) as e:
        print(f"Unable to perform incr for value: {value}, error:{e}")
