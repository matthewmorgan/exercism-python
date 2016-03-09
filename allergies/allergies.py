allergens = ['eggs','peanuts','shellfish','strawberries',
             'tomatoes','chocolate','pollen','cats']

class Allergies:
    
    def __init__(self, score):
        self.score = score
    
    def is_allergic_to(self, allergen):
        return self.score & 1 << allergens.index(allergen)
    
    @property
    def lst(self):
        return [allergen for allergen in allergens
            if self.is_allergic_to(allergen)]