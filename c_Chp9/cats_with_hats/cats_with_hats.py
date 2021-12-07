
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
    Make 100 rounds around the cats starting with the second round
    (the first round is made in put_hats_on_cats())

    In the second round, stop only at every second cat (#2, #4, #6 etc)

    The third round, stop only at every third cat (#3, #6, #9 etc)

    Continue this process until one hundred rounds are made.
    On the last round, stop only at cat #100.
    """
    cats = put_hats_on_all_cats()

    for round in range(2,101):
        for key, value in cats.items():
            if key % round == 0 and value == True:
                cats[key] = False
            elif key % round == 0 and value == False:
                cats[key] = True
    return cats

def output_cats_with_hats():
    """
    Create a list which returns the numbered keys which have a true value
    (i.e. all the cats which have hats)
    """
    cats = remove_or_put_hat_on_cat().items()
    cats_with_hats = [key for key, value in cats if value == True]
    return cats_with_hats

print(output_cats_with_hats())
