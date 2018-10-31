import os
from unittest.mock import Mock

from service import Service

test_inputs = [0, 0.1, -0.1, 1, -1, 2, -2, 10, -10, 1000, -1000]
divide_outputs = [0, 100, -100, 10, -10, 5, -5, 1, -1, 0.01, -0.01]

def service_w_mocked_random():
	serv = Service()
	serv.bad_random = Mock('bad_random')
	serv.bad_random.return_value = 10
	return serv

def test_bad_random():
	assert(service_w_mocked_random().bad_random() == 10)

def test_divide():
	serv = service_w_mocked_random()

	# divide by zero and catch the exception
	try:
		result = serv.divide(test_inputs[0])
		assert(False)
	except ZeroDivisionError:
		assert(True)

	# test all other inputs
	for i in range(1,len(test_inputs)):
		result = serv.divide(test_inputs[i])
		assert(result == divide_outputs[i])

	
def test_abs_plus():	
	serv = Service()

	test_outputs = [1, 1.1, 1.1, 2, 2, 3, 3, 11, 11, 1001, 1001]

	# test all inputs
	for i in range(0, len(test_inputs)):
		result = serv.abs_plus(test_inputs[i])
		assert(result == test_outputs[i])

def test_complicated_function():
	serv = service_w_mocked_random()

	# divide by zero and catch the exception
	try:
		result = serv.divide(test_inputs[0])
		assert(False)
	except ZeroDivisionError:
		assert(True)
	
	# test all other inputs
	for i in range(1, len(test_inputs)):
		result = serv.complicated_function(test_inputs[i])
		assert(result[0] == divide_outputs[i])
		assert(result[1] == 0)

