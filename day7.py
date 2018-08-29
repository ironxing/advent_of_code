import read_csv

m0 = read_csv.read_csv_function("day7_input.csv", ",")

def has_character(s):
    try:
        s.index('>')
        return True
    except ValueError:
        return False

m = []
for i in range(len(m0)):
    if has_character(m0[i][0]):
        m.append(m0[i])

print(m)
print(len(m))
# print(m1[0])
        # m1 = m1.append(m[i][0])
# print(m1)

# for i in range(len(m)):
#     if len(m[i]) == 1:
#         np.delete(m, (i), axis=0)
# print(m)


#
#
#
# # Load in the data and keep only the ones with "->"
# m = [["fwft", "ktlj", "cntj", "xhth"],
#      ["padx", "pbga", "havc", "qoyq"],
#      ["tknk", "ugml", "padx", "fwft"],
#      ["ugml", "gyxo", "ebii", "jptl"]]
#
#
# def find_word(word, matrix):
#     word_found = False
#     for i in range(len(m)):
#         for j in range(1, len(m[i])):
#             if word == m[i][j]:
#                 word_found = True
#     return word_found
#
# for i in range(len(m)):
#     word = m[i][0]
#     word_found = find_word(word, m)
#     if not word_found:
#         print(word)
#         break
