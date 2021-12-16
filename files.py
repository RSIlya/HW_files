
def create_cookbook_from_file(filename, encoding='utf-8'):
    with open(filename, encoding=encoding) as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            cook_book[dish] = []            
            for step in range(int(file.readline().strip())):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredient = {'ingredient_name': ingredient_name.strip(),
                              'quantity': int(quantity),
                              'measure': measure.strip()}
                cook_book[dish] += [ingredient]
            file.readline()
    return cook_book
   
                 
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cookbook_from_file('recipes.txt')
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book: continue
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure,
                                              'quantity': quantity * person_count}
            else:
                shop_list[ingredient_name]['quantity'] += quantity * person_count
    return shop_list

from pprint import pprint

pprint(create_cookbook_from_file('recipes.txt'))
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

    
