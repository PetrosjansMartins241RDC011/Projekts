import requests
from bs4 import BeautifulSoup

ALL_the_URLs = {
    "cutting": "https://onewholesomelife.com/healthy-meal-prep-ideas-for-weight-loss/",
    "maintaining": "https://www.weightandwellness.com/resources/recipes",
    "bulking": "https://dinewithdrinks.com/best-bulking-recipes"
}

def cutting_weight():
    html_text = requests.get(ALL_the_URLs['cutting'])
    soup = BeautifulSoup(html_text.text, 'html.parser')

    recipes = soup.find_all('div', class_='wprm-recipe-roundup-item')

    for i, recipe in enumerate(recipes[:7], start=1):
        recipe_name = recipe.find('h3').text.strip() if recipe.find('h3') else "No title"
        recipe_description = recipe.find('div', class_='wprm-recipe-summary wprm-block-text-normal').text.strip() if recipe.find('div', class_='wprm-recipe-summary wprm-block-text-normal') else "No description"
        meal_recipe = recipe.a['href']
        full_url = f"https://onewholesomelif.com{meal_recipe}"

        print(f"{i}. Recipe Name: {recipe_name}")
        print(f"    Recipe Description: {recipe_description}")
        print(f'    Meal Recipe: {full_url}')

        print('')



def maintaining_weight():
    html_text = requests.get(ALL_the_URLs['maintaining'])
    soup = BeautifulSoup(html_text.text, 'html.parser')

    recipes = soup.find_all('div', class_='col-xs-12 col-sm-6 col-md-3')

    for i, recipe in enumerate(recipes[:7], start=1):
        recipe_name = recipe.find('h2').text.strip() if recipe.find('h2') else "No title"
        recipe_description = recipe.find('p').text.strip() if recipe.find('p') else "No description"
        meal_recipe = recipe.h2.a['href'] if recipe.h2 and recipe.h2.a else "#"
        full_url = f"https://www.weightandwellness.com{meal_recipe}"

        print(f"{i}. Recipe Name: {recipe_name}")
        print(f"    Recipe Description: {recipe_description}")
        print(f'    Meal Recipe: {full_url}')

        print('')


def bulking():
    html_text = requests.get(ALL_the_URLs['bulking'])
    soup = BeautifulSoup(html_text.text, 'html.parser')

    recipe_headings = soup.find_all('h2')

    for i, heading in enumerate(recipe_headings[:7], start=1):
        title_text = heading.get_text(strip=True)
        recipe_name = title_text.split('. ', 1)[-1] if '. ' in title_text else title_text

        description_tag = heading.find_next('p')
        recipe_description = description_tag.get_text(strip=True) if description_tag else "No description"

        link_tag = heading.find_next('a', string="View Recipe")
        meal_recipe = f"https://dinewithdrinks.com{link_tag['href']}" if link_tag and link_tag.has_attr('href') else "No link"

        print(f"{i}. Recipe Name: {recipe_name}")
        print(f"    Recipe Description: {recipe_description}")
        print(f"    Meal Recipe: {meal_recipe}")
        print('')

