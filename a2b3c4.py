inp = input("Enter: ")

b = ""

for i in range(0, len(inp), 2):
    letter = inp[i]
    count = int(inp[i + 1])
    b += letter * count

print(b)
