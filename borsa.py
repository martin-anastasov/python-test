price_kg_veg = float(input())
price_kg_fr = float(input())
total_kg_veg = int(input())
total_kg_fr = int(input())

vegetable = price_kg_veg * total_kg_veg
fruits = price_kg_fr * total_kg_fr
sum = vegetable + fruits

sum_to_eur = sum / 1.94
print(sum_to_eur)