#!/usr/bin/env python3
# -*- coding: utf-8 -*-

itr = int(input())

result = []
for i in range(itr):
    number = input()
    if number[::-1] == number:
        result.append('Ronde!')
    else:
        for i in number:
            if number.count(i) >= 4:
                result.append('Ronde!')
                break
            index = number.index(i)
            if number[index:index+3] == i*3:
                result.append('Ronde!')
                break
        else:
            result.append('Rond Nist')

for res in result:
    print(res)