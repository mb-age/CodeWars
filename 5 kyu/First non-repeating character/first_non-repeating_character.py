def first_non_repeating_letter(string):
    s = [i for i in string if string.lower().count(i.lower())==1]
    return s[0] if s else ''