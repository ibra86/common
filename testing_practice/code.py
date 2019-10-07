def common_elements_from_two_lists(a,b):
	return list(set(a+b))

def coded_task_02(s):
	return s.count('a')

def coded_task_03(num):

	# while True:
	# 	if num % 3 == 0:
	# 		num //= 3
	# 		if num == 1:
	# 			return True
	# 	else:
	# 		return False

	while (num % 3 == 0):
		num /= 3
	return num == 1

def coded_task_04(num):	
	digits_list = lambda num: [int(x) for x in str(num)]
	res = sum(digits_list(num))
	while res >= 10:
		res = sum(digits_list(res))
	return res

	# while num >= 10:
	# 	num = sum(divmod(num,10))

def coded_task_05(input_list):
	return [x for x in input_list if x != 0] + [x for x in input_list if x == 0]


def coded_task_06(input_list):

	for i, k in enumerate(range(len(input_list)-2)):
		d1 = input_list[i+1] - input_list[i]
		d2 = input_list[i+2] - input_list[i+1]
		if d1 != d2:
			return False

	return True
		

