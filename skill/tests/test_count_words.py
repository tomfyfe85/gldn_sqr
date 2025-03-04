from lib.count_words import count_words

def test_count_words():
	result =  count_words('this is words')

	assert result == 3


