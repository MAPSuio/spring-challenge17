def solve(s):
    result = ""
    i = 0
    while i < len(s):
        result += s[i]
        if s[i] != " ":
            i += 3
        else:
            i += 1
    return result

print solve("wowerelolcocoromomere totoro tothohere soshohorowow")
