matsted1 = {"vegetarian": "no", "vegan": "no", "glucose intolerant": "no"}
matsted2 = {"vegetarian": "yes", "vegan": "yes", "glucose intolerant": "yes"}
matsted3 = {"vegetarian": "yes", "vegan": "yes", "glucose intolerant": "yes"}

vegetarianer = input("Are you vegetarian? ")
veganer = input("Are you vegan?  ")
glutenintoleranse = input("Are you gll ")


if vegetarianer == "yes":
    if glutenintoleranse == "yes":
        if matsted1["vegetarian"] == "yes" and matsted1["glucose intolerant"] == "yes":
            print("matsted1")
        if matsted2["vegetarian"] == "yes" and matsted2["glucose intolerant"] == "yes":
            print("matsted2")
        if matsted3["vegetarian"] == "yes" and matsted3["glucose intolerant"] == "yes":
            print("matsted3")
    if matsted1["vegetarian"] == "yes":
        print("matsted1")
    if matsted2["vegetarian"] == "yes":
        print("matsted2")
    if matsted3["vegetarian"] == "yes":
        print("matsted3")

if veganer == "yes":
    if glutenintoleranse == "yes":
        if matsted1["vegan"] == "yes" and matsted1["glucose intolerant"] == "yes":
            print("matsted1")
        if matsted2["vegan"] == "yes" and matsted2["glucose intolerant"] == "yes":
            print("matsted1")
        if matsted3["vegan"] == "yes" and matsted3["glucose intolerant"] == "yes":
            print("matsted1")
    if matsted1["vegan"] == "yes":
        print("matsted1")
    if matsted2["vegan"] == "yes":
        print("matsted2")
    if matsted3["vegan"] == "yes":
        print("matsted3")