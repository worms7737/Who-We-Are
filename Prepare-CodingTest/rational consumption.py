# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#user_input = input()
#print ("Hello Goorm! Your input is " + user_input)

N = int(input())
items = []

for _ in range(N):
	name, price = input().split()
	price = int(price)
	items.append((name, price))
	
	most_expensive = items[0]
	cheapest = items[0]
	
	for item in items[1:]:
		if item[1] > most_expensive[1]:
			most_expensive = item
		if item[1] < cheapest[1]:
			cheapest = item
			
print(most_expensive[0],most_expensive[1])
print(cheapest[0],cheapest[1])