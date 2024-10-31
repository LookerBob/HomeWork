def all_variants(text):
    for x in range(len(text)):
        for y in range(len(text) - x):
            # test = '0123456789'
            # print(test[1:4+3])
            yield text[y:y + x + 1]


a = all_variants("abcd")
# print(a)
for i in a:
    print(i)
