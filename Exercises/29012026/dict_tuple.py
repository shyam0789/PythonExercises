country_pop = {
    "India" : 143,
    "China" : 136,
    "USA" : 32,
    "Pakistan" :21
}

def get_input():
    user_input = input("Choose one of the below: \n1. Print \n2. Add\n3. Remove\n4. Query\n").lower()
    if user_input == "print":
        print_dict()
    elif user_input == "add":
        add_dict()
    elif user_input == "remove":
        remove_dict()
    elif user_input == "query":
        query_dict()
    else:
        print("Enter valid input.")

def print_dict():
    for country, population in country_pop.items():
        print(f"{country} => {population}Mn")

def add_dict():
    country = input("Enter the country name: ")
    if country in country_pop:
        print(f"Country {country} already exists.")
        return
    else:
        population = int(input("Enter the population: "))
        country_pop[country] = population
    print_dict()

def remove_dict():
    country = input("Enter the country to be removed: ")
    if country in country_pop:
        country_pop.pop(country)
        print_dict()
    else:
        print("Country to be removed doesn't exist")

def query_dict():
    country = input("Enter the country for which you need to view the population: ")
    # population = [country_pop[country] for p in country_pop if p == country]
    print(f"Population of {country} is {country_pop[country]} Mn")

get_input()