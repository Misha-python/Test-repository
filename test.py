def inverse (string):
	new = string

	for char in string:
		if char == '0':
			new += '1'

		elif char == '1':
			new += '0'

		else:
			raise ValueError

	return new