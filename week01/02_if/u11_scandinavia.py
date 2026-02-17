country = input("Give me a country name >> ")

SCANDINAVIA = "swedennorwaydenmark"

print(f"{"It is a scandinavian country" if country.casefold() in SCANDINAVIA else "That is not a scandinavian country"}")