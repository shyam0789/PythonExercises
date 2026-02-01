List exercise
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ["doctor strange"]
print(heros)
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

#files exercise
with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    next(f)  # This will skip first line in the file which is a header