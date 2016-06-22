import re


ACTIONS = ['wink', 'double blink', 'close your eyes', 'jump']

def handshake(code):
    code = normalize_code(code)
    shake = [action for ix, action in enumerate(ACTIONS) if 2 ** ix & code]
    return (shake, list(reversed(shake)))[code & 16 > 0]

def code(shake):
    if not all([action in ACTIONS for action in shake]):
        return '0'
    code = ''.join(['1' if a in shake else '0' for a in reversed(ACTIONS)])
    if handshake(code) != shake:
        code = '1' + code
    return code.lstrip('0')

def normalize_code(code):
    if type(code) is int:
        return max(code,0)
    if re.fullmatch(r'[01]*', code):
        return int(code, 2)
    return 0
    