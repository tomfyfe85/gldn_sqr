import pytest
from bytes.lib.password_checker import PasswordChecker

def test_password_checker():
	checker = PasswordChecker()
	assert checker.check('12345667889')

	checker2 = PasswordChecker()
	with pytest.raises(Exception) as e:
		checker2.check('sdf')
	error_msg = str(e.value)
	assert error_msg == "Invalid password, must be 8+ characters."
