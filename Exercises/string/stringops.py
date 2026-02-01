# Create 3 variables to store street, city and country, now create address variable to store entire
# address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line
street = "9863 W Valley Ranch Pkwy"
city = "Irving"
country = "US"
mailing_address = street + " "+ city +" "+ country
print(mailing_address)
print(f"{street} {city} {country}")
print(f"{street}\n{city}\n{country}")

# Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index
earth_text = "Earth revolves around the sun"
print(earth_text[6:14])
print(earth_text[-23:-15])


# Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
# Use python f string for this.
fruits = 4
veggies = 6
print(f"I eat {veggies} veggies {fruits} fruits daily")


# I have a string variable called s='maine 200 banana khaye'.
# This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.

text = "maine 200 banana khaye"
new_text = text.replace("200","10").replace("banana","samosa")
print(new_text)
