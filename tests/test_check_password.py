from lib.check_codeword import check_codeword

def test_check_code_word():
	result = check_codeword("horse")
	assert result == "Correct! Come in."

	result2 = check_codeword("hodfsdfsdfsdfrse")
	assert result2 == "Close, but nope."

	result3 = check_codeword("asdasdasd")
	assert result3 =="WRONG!"
