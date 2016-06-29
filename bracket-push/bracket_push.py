BRACKETS = {'{': '}', '[': ']', '(': ')'}


def check_brackets(brackets):
    b = [b for b in brackets if b in BRACKETS or b in BRACKETS.values()]
    c = []
    while b:
        next = b.pop(0)
        if next in BRACKETS:
            c.append(BRACKETS[next])
        elif c and next != c.pop():
            return False
    return not c
