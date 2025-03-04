from bytes.lib.counter import Counter

def test_counter():
	counter = Counter()
	counter.add(5)

	assert "Counted to 5 so far."

	counter.add(5)

	assert "Counted to 10 far"