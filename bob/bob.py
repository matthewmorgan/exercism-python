# def hey(what):
#  
#     cleaned = what.strip()
#  
#     if (cleaned.isupper()):
#         return 'Whoa, chill out!'
#  
#     if (cleaned.endswith('?')):
#         return 'Sure.'
#  
#     if (cleaned == ''):
#         return 'Fine. Be that way!'
#  
#     return 'Whatever.'

def isSilence(phrase):
    return phrase.strip() == ''
 
 
def isShouting(phrase):
    return phrase.isupper()
 
 
def isQuestion(phrase):
    return phrase.strip().endswith('?')
 
 
def isAnything(_):
    return True
 
def hey(what):
    return [result for condition, result in lookup.items()
            if condition(what)][0]
            
lookup = dict([
          (isSilence, 'Fine. Be that way!'),
          (isShouting, 'Whoa, chill out!'),
          (isQuestion, 'Sure.'),
          (isAnything, 'Whatever.')])