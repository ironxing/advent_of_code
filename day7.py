import read_csv

m0 = read_csv.read_csv_function("day7_input.csv", ",")

#  Clean csv input
m = []
for i in range(len(m0)):
    if len(m0[i])>1:  # keep only the rows with ","
        m.append(m0[i])

for i in range(len(m)):
    str_to_split = m[i][0]
    splitStr = str_to_split.split(" ")
    for j in range(len(splitStr)):
        if j == 0:
            m[i][j] = splitStr[j]
        else:
            m[i].insert(j, splitStr[j])

for i in range(len(m)):
    for j in range(len(m[i])):
        string_raw = m[i][j]
        string_clean = string_raw.replace(" ", "")
        m[i][j] = string_clean

print(m)

#  The name of the bottom program should not be in anywhere to the right of '->'
def find_word(word, matrix):
    word_found = False
    for i in range(len(m)):
        for j in range(3, len(m[i])):  # 3 is the index of '->' in each row
            if word == m[i][j]:
                word_found = True
    return word_found

for i in range(len(m)):
    word = m[i][0]
    word_found = find_word(word, m)
    if not word_found:
        print(word)
        break
