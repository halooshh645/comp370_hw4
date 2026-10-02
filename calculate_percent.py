ponies = {
    "Twilight Sparkle": 4759,
    "Rarity": 2673,
    "Pinkie Pie": 2897,
    "Rainbow Dash": 3093,
    "Fluttershy": 2129
}

total_lines = 36800

for pony, lines in ponies.items(): # Ponies.items gives you both key and values because ponies is dictionary
    percentage = lines / total_lines * 100
    print(pony, percentage)
