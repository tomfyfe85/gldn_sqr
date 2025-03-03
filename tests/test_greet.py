from lib.greet import *

def test_greet():
	result = greet("tom")
	assert result == 'Hello, tom!'
