cook_book = {}

with open('recipes.txt', 'rt') as fp:
    while True:
        dish = fp.readline().strip()
        if len(dish) > 0:
            ingred_num = int(fp.readline().strip())
            recipe_list = []
            for i in range(0, ingred_num):
                recipe_dict = {}
                recipe_str = fp.readline().strip()
                ingred_line = recipe_str.split(' | ')
                recipe_dict['ingredient_name'] = ingred_line[0]
                recipe_dict['quantity'] = int(ingred_line[1])
                recipe_dict['measure'] = ingred_line[2]
                recipe_list.append(recipe_dict)

            cook_book[dish] = recipe_list
            space = fp.readline().strip()
        else:
            break

print(cook_book)
