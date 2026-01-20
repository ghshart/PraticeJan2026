def make_sandwich(bread_type,filling,cheese=None,toasted=False):
    if (cheese) is None:
        cheese = "no cheese"
        return "cheese"

    if not toasted:
        toasted = "toasted"
        return toasted

    print(f"The sandwich is of", bread_type,"with", filling,"and", cheese,"that is",toasted)
    return str(make_sandwich)

make_sandwich("wheat", "turkey", "cheddar", True)