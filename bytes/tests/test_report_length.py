from bytes.lib.report_length import *

def test_report_length():
	result = report_length("three")
	assert result == "This string was 5 characters long."