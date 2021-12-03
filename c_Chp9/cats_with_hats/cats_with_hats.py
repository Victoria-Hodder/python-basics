
def put_hats_on_cats():
    cats = {}
    for cat in range(1, 101):
        cats[cat] = True
    return cats

# print(put_hats_on_cats())

def remove_or_put_hat_on_cat():
    cats = put_hats_on_cats()

    for round in range(2,101):
        for key, value in cats.items():
            if key % round == 0 and value == True:
                cats[key] = False
            elif key % round == 0 and value == False:
                cats[key] = True
#         print(f"Round {round}: {cats}\n")
    return cats

# print(remove_or_put_hat_on_cat())

cats = remove_or_put_hat_on_cat().items()
cats_with_hats = []

for key, value in cats:
    if value == True:
        # append key to list
        cats_with_hats.append(key)
# return list of cats with hats
print(cats_with_hats)
