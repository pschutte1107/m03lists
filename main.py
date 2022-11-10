things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
things[0] = things[0].upper()
del things[2]
print(things)


def good():
    return ["Harry", "Hermione", "Ron"]


print(good())


get_odds = (num for num in range(1, 10) if not num % 2 == 0)
count = 0
for num in get_odds:
    if count == 2:
        print(num)
        break
    count += 1
