"""Print out all the melons in our inventory."""


from melons import melon_information 
# print(melon_information)


def print_melon(name, price, seedlessness, flesh_color, rind_color, average_weight):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'

    if seedlessness:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds, are {flesh_color} {rind_color}, weight {average_weight} pound and are ${price}. ')


for melon in melon_information:

    print_melon(melon["name"], melon["price"], melon["seedlessness"], melon["flesh_color"], melon["rind_color"],
    melon["average_weight"])
