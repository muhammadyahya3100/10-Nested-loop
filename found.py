word = input("Enter you word: ")
character = input("Enter which character you want to find: ")
count = 0
for char in word:
    if char == character:
        count = count+1
print(f"The character {character} has found {count} time in the word {word}")