
def arrange_cats_in_circle():
    """
    Arrange cats in a circle without hats by initialising
    a dictionary where each numbered key has a False value.
    """
    cats = {}
    for cat in range(1, 101):
        cats[cat] = False
    return cats

def remove_or_put_hat_on_cat():
    """
    Make 100 circuits around the cats, removing or putting on
    "hats" (i.e. setting the boolean True or False) depending on
    the round ("circuit") number and current boolean value.
    """
    cats = arrange_cats_in_circle()

    for circuit in range(1,101):
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
