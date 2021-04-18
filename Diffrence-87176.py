def game(number):
    return int(max(list(str(number)))) - int(min(list(str(number))))
