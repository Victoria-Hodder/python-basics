
def put_hats_on_all_cats():
    """
    Place a hat on every cat by assigning each numbered key
    with a True value
    """
    cats = {}
    for cat in range(1, 101):
        cats[cat] = True
    return cats

def remove_or_put_hat_on_cat():
    """
    Make 100 circuits around the cats, adding or removing "hats"
    (i.e. setting the boolean True or False) depending on the
    circuit number and current boolean value
    """
    cats = put_hats_on_all_cats()

    for circuit in range(2,101):
        for key, value in cats.items():
            if key % circuit == 0 and value == True:
                cats[key] = False
            elif key % circuit == 0 and value == False:
                cats[key] = True
    return cats

def output_cats_with_hats():
    """
    Create a list which returns the numbered keys which have a true
    value (i.e. all the cats which have hats)
    """
    cats = remove_or_put_hat_on_cat().items()
    cats_with_hats = [key for key, value in cats if value == True]
    return cats_with_hats

print(output_cats_with_hats())
