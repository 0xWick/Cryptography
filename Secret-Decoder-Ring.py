# A program for decoding cypher from Secret Decoder Ring
# By 0xWick

# Define arrays for PlainText
plainText = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# "Shifts" of ring, // only using two for simplicity
shift_1 = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A"]
shift_2 = ["C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B"]

# Text to Cypher
PlainText = "HEIL HITLER"

Cypher_s1 = ""
Cypher_s2 = ""

index = 0
print(f"Text = {PlainText}")
print("")
print("Text To Cypher:")
# Encode using Shift-1
for i in PlainText:
    for j in plainText:
        if i == j:
            index = plainText.index(j)
            Cypher_s1 += shift_1[index]
print(f"Cypher- Shift1: {Cypher_s1}")

# Encode using Shift-2
for i in PlainText:
    for j in plainText:
        if i == j:
            index = plainText.index(j)
            Cypher_s2 += shift_2[index]
print(f"Cypher- Shift2: {Cypher_s2}")

# Cypher to Text
print("")
print("Cypher To Text:")
PlainText_s1 = ""
PlainText_s2 = ""
index_2 = 0

# Decode using Shift-1
for i in Cypher_s1:
    for j in shift_1:
        if i == j:
            index_2 = shift_1.index(j)
            PlainText_s1 += plainText[index_2]
print(f"Text- Shift1: {PlainText_s1}")

# Decode using Shift-2
for i in Cypher_s2:
    for j in shift_2:
        if i == j:
            index_2 = shift_2.index(j)
            PlainText_s2 += plainText[index_2]
print(f"Text- Shift2: {PlainText_s2}")


