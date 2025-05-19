import requests
from bs4 import BeautifulSoup

ALL_the_URLs = {
    "cutting": "https://onewholesomelife.com/healthy-meal-prep-ideas-for-weight-loss/",
    "maintaining": "https://www.weightandwellness.com/resources/recipes",
    "bulking": "https://dinewithdrinks.com/best-bulking-recipes"
}

def get_cutting_recipes():
    html = requests.get(ALL_the_URLs['cutting'], headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(html.text, 'html.parser')

    recipes = soup.find_all('div', class_='wprm-recipe-roundup-item')
    results = []

    for recipe in recipes[:7]:
        name = recipe.find('h3').text.strip() if recipe.find('h3') else "No title"
        desc = recipe.find('div', class_='wprm-recipe-summary wprm-block-text-normal')
        description = desc.text.strip() if desc else "No description"
        
        href = recipe.a['href'] if recipe.a and recipe.a.has_attr('href') else "#"
        link = href if href.startswith("http") else f"https://onewholesomelife.com{href}"

        results.append((name, description, link))

    return results

        


def get_maintaining_recipes():
    html = requests.get(ALL_the_URLs['maintaining'], headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(html.text, 'html.parser')

    recipes = soup.find_all('div', class_='col-xs-12 col-sm-6 col-md-3')
    results = []
    for recipe in recipes[:7]:
        name = recipe.find('h2').text.strip() if recipe.find('h2') else "No title"
        description = recipe.find('p').text.strip() if recipe.find('p') else "No description"
        
        href = recipe.h2.a['href'] if recipe.h2 and recipe.h2.a else "#"
        link = href if href.startswith("http") else f"https://www.weightandwellness.com{href}"
        results.append((name, description, link))

    return results
        


def get_bulking_recipes():
    html = requests.get(ALL_the_URLs['bulking'], headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(html.text, 'html.parser')


    headings = soup.find_all('h2')
    results = []

    for heading in headings[:7]:
        name = heading.get_text(strip=True)
        name = name.split('. ', 1)[-1] if '. ' in name else name

        description_tag = heading.find_next('p')
        description = description_tag.get_text(strip=True).split('\n')[0] if description_tag else "No description"


        link_tag = heading.find_next('a', string="View Recipe")
        href = link_tag['href'] if link_tag and link_tag.has_attr('href') else "#"
        link = href if href.startswith("http") else f"https://dinewithdrinks.com{href}"

        results.append((name, description, link))

    return results
        

def display_recipes(recipes):
    for i, (name, description, _) in enumerate(recipes, start=1):
        print(f"{i}. {name} - {description}")

def main():
    print("Choose a dieting style:")
    print("1. Cutting")
    print("2. Maintaining")
    print("3. Bulking")

    while True:
        choice = input("enter choice (cutting/maintaining/bulking): ").strip().lower()
        if choice in ALL_the_URLs:
            break
        print("Invalid choice. Choose between 'cutting', 'maintaining' or 'bulking'.")

    if choice == 'cutting':
        recipes = get_cutting_recipes()
    elif choice == 'maintaining':
        recipes = get_maintaining_recipes()
    else:
        recipes = get_bulking_recipes()

    print(f"\n===== {choice.upper()} RECIPES =====")
    display_recipes(recipes)
    
    while True:
        try:
            selected = int(input("\nWhich recipe would you like to try out (1-7)? "))
            if 1 <= selected <= len(recipes):
                print(f"\nLink to recipe: {recipes[selected - 1][2]}")
                break
            else:
                print("Invalid number. Choose between 1-7.")
        except ValueError:
            print("Enter a valid number.")


if __name__ == "__main__":
    main()
