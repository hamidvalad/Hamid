#https://quera.ir/problemset/technology/87176/%D8%B3%D8%A4%D8%A7%D9%84-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D8%A8%D8%A7%D8%B2%DB%8C-%D8%AA%D9%81%D8%A7%D8%B6%D9%84

def game(number):
    return int(max(list(str(number)))) - int(min(list(str(number))))
