things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
things[0] = things[0].upper()
del things[2]
print(things)


def good():
    return ["Harry", "Hermione", "Ron"]


print(good())


def get_odds():
    for num in range(1, 10):
        if num % 2 != 0:
            yield num


count = 1
for num in get_odds():
    if count == 3:
        print(num)
        break
    count += 1
