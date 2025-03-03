from lib.report_length import report_length

def test_report_length():
	result = report_length("three")
	assert result == "This string was 5 characters long."