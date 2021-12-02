
def generate_cats():
    cats = []
    for cat in range(1, 11):
        cats.append(cat)
    return cats

print(generate_cats())

def generate_cats_dict():
    cats = {}
    for cat in range(1, 11):
        cats[cat] = True
    return cats

print(generate_cats_dict())

def convert_even_keys_to_false():
    cats = generate_cats_dict()

    for key, value in cats.items():
        if key % 2 == 0:
            cats[key] = False
    return cats

print(convert_even_keys_to_false())
