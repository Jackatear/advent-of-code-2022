def can_calculate(dictionary, key):
    check = True
    for value in dictionary[key]:
        if not value.isnumeric():
            return False
    return check

            
        
        
example = {
    'a': ['100','200','300','bob','2109'],
    'b': 249,
    'x': 10000,
    'jack': 'dictionary'}

z = can_calculate(example, 'a')
print(z)
