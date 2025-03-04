from bytes.lib.greet import greet

def test_greet():
	result = greet("tom")
	assert result == 'Hello, tom!'
