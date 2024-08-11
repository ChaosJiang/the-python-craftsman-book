def string_upper(s: str) -> str:
    chars = []
    for ch in s:
        if ch >= "a" and ch <= "z":
            chars.append(chr(ord(ch) - 32))
        else:
            chars.append(ch)
    return "".join(chars)
