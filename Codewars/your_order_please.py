def order(sentence):
    if sentence == "":
        return ""
    sentence += " "
    word = ""
    dict = {}
    for elem in sentence:
        if elem != " ":
            word += elem
        else:
            for i in word:
                print(i, is_Number(i))
                if is_Number(i):
                    dict[int(i)] = word
                    print(dict)
                else:
                    continue
            word = ""
    sortKeys = sorted(dict)
    str = ""
    for i in sortKeys:
        if i in dict:
            str += dict[i] + " "
    return str.rstrip()

def is_Number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

print(order("abc1 msanm2 sdfui3 asd9asd 5sdmn 7asd"))