#items
beer_i = 200
snack_i = 100
Yakitori_i = 100
pcard = -150
sale = 0.2
#kosuu
beer_k = 2
snack_k = 1
Yakitori_k = 2
sum_v = (beer_i * beer_k) + (snack_i * snack_k) + ((Yakitori_i * (1 - sale)) * Yakitori_k) - pcard
print("The total of shopping is", sum_v)
