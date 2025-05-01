s = "a good   example"

result = s.split(" ")
res2 = []
for i in result:
    if i != "":
        res2.append(i)
print(len(res2))
print(res2)
res2.reverse()
res2 = " ".join(res2)
print(res2)


# without functions

s = "a good   example"

# Step 1: Extract words manually
words = []
i = 0
n = len(s)

while i < n:
    # Skip spaces
    while i < n and s[i] == ' ':
        i += 1
    if i >= n:
        break

    # Start of a word
    word = ""
    while i < n and s[i] != ' ':
        word += s[i]
        i += 1

    # Add word to list
    if word != "":
        words.append(word)

# Debug: print number of words and list
print(len(words))
print(words)

# Step 2: Reverse the words manually
start = 0
end = len(words) - 1
while start < end:
    words[start], words[end] = words[end], words[start]
    start += 1
    end -= 1

# Step 3: Build the final string manually
result = ""
for i in range(len(words)):
    result += words[i]
    if i != len(words) - 1:
        result += " "

# Final Output
print(result)
