number_of_month = int(input())

if number_of_month == 12 or number_of_month == 1 or number_of_month == 2:
	print("winter")
elif number_of_month > 2 and number_of_month < 6:
	print("spring")
elif number_of_month > 5 and number_of_month < 9:
	print("summer")
else:
	print("autumn")