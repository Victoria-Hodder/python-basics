
def generate_cats():
    cats = []
    for cat in range(1, 101):
        cats.append(f'#{cat}')
    return cats

print(generate_cats())
