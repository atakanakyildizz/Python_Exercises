# [1.2]

# country_name = "l’Afghanistan"
country_name = "l' Etats-Unis"

if country_name.lower() == "belize" or country_name.lower() == "cambodge" or\
        country_name.lower() == "mexique" or country_name.lower() == "mozambique" or\
        country_name.lower() == "zaïre" or country_name.lower() == "zimbabwe":

    print(f"{country_name} is masculine\n")

elif country_name[-1].lower() == "e":
    country_name = "la " + country_name
    print(f"{country_name} \n"
          f"Country is feminine\n")

elif country_name[0:2].lower() == "l'":
    country_name = country_name[3:]
    country_name = "les " + country_name
    print(f"{country_name} \n"
          f"Country is plural\n")

else:
    country_name = "le " + country_name
    print(f"{country_name} \n"
          f"Country is masculine\n")
