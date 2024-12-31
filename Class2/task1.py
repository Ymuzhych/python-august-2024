foods = ("apple", "banana", "orange", "mango", "straberry", "grape", "mandarin", "strawberry")
calories = ("52", "96", "62", "605", "33", "68", "50", "33")

print(foods)
foods_list=list(foods)
print(list(foods))
print(foods_list[4])
print(set(foods_list))

dict_foods = {"apple" : 52, "banana" : 96, "orange" : 62, "mango" : 605, "straberry" : 33 , "grape" : 68, "mandarin" : 50, "strawberry" : 33}
dict_foods["Tomato"] = 60
print(dict_foods)
dict_foods["grape"] = 50
print(dict_foods)


print(dict_foods["apple"] + dict_foods["banana"])