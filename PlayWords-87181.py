#https://quera.ir/problemset/technology/87181/%D8%B3%D8%A4%D8%A7%D9%84-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D8%A8%D8%A7%D8%B2%DB%8C-%DA%A9%D9%84%D9%85%D9%87%D9%87%D8%A7

def words_check(text):
    char_list =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    words = text.split()
    good_list = dict()
    for word in words:
        good, bad = 0,0
        new_word = ''
        for char in word:
            if char not in char_list:
                bad += 1
            if char in char_list:
                good += 1
                new_word += char
        if good > bad:
            good_list.setdefault(new_word.title(), 0)
            good_list[new_word.title()] += 1
    return good_list