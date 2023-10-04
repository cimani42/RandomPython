# number_builder = []
# i = 0
#
# while i <= 50:
#     if i % 2 == 0 :
#         number_builder.append(str(i))
#     i += 1
# print(" ".join(number_builder))

x = "Grapefruit Penguin requirements apple banaa enumerate cheryyy libraries fench francophone"

letters = []

y = 0
while y < len(x):
    if y % 2 == 0:
        letters.append(x[y].upper())
    else:
        letters.append(x[y].lower())
    y += 1
print(" ".join(letters))

words = x.split()
# print(words)
test = [word.upper() if i % 2 == 1 else word for i, word in enumerate(words)]
print(test)

