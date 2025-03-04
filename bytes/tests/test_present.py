import pytest
from bytes.lib.present import Present

def test_present_is_wrapped():
	present = Present()
	present.wrap("nintendo")
	with pytest.raises(Exception) as e:
		present.wrap("nintendo")
	error_message = str(e.value)
	assert error_message == "A contents has already been wrapped."

