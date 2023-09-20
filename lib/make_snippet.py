def make_snippet(string):
    words = string.split()
    if len(words) < 6:
        return string
    else:
        return ' '.join(words[:5]) + "..."
