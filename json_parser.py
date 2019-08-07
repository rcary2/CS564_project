#!/usr/bin/env python

import json

#a = open('full_format_recipes.json', 'r')
#recipe_json = json.load(a)
#a.close()

def format_text(text_list):
    formatted_directions = str()
    #Remove double quotes and join with newline chars
    for i in text_list:
        if len(formatted_directions) == 0:
            formatted_directions = i.strip().replace('"','')
        else:
            formatted_directions = '\n'.join([formatted_directions, i.strip().replace('"','')])
    return formatted_directions

def format_list(in_list):
    output = ""
    if isinstance(in_list, list):
        if len(in_list) == 1:
            return in_list[0]
        else:
            for i in in_list:
                if len(output) == 0:
                    output = i.strip()
                else:
                    output = ','.join([output, i.strip()])
            return output
    else:
        return None

        
##### LOAD RECIPES JSON #####
with open('full_format_recipes.json', 'r') as a:
    recipe_json = json.load(a)  

recipe_dict = dict()

for index, item in enumerate(recipe_json):
    #print index, item.keys()
    if len(item.keys()) == 11:
        directions = format_text(item['directions'])
        ingredients = format_text(item['ingredients'])
        categories = format_list(item['categories'])
        recipe_dict[index] = {
            'title': item['title'],
            'calories': item['calories'],
            'fat': item['fat'],
            'protein': item['protein'],
            'sodium': item['sodium'],
            'rating': item['rating'],
            'categores': categories,
            'ingredients': ingredients,
            'directions': directions
            }
        
        del directions, ingredients, categories
    else:
        recipe_dict[index] = None

        
for item in recipe_dict:
    if recipe_dict[item]: #check that not None type
        print str(item) + ": " + recipe_dict[item]['title'] + " --> " + recipe_dict[item]['categores']
##### FINISHED LOADING RECIPES JSON #####


with open('epi_r.csv', 'r') as a:
    recipe_table = pd.read_csv('epi_r.csv')


