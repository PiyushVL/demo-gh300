"""Utilities for validating email addresses."""

import re


_EMAIL_PATTERN = re.compile(
	r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
	r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
	r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$"
)


def validate_email_address(email: str) -> bool:
	"""Return whether *email* has a valid, commonly used email format."""
	if not isinstance(email, str) or len(email) > 254:
		return False

	email = email.strip()
	if not email or email.count("@") != 1:
		return False

	local_part, domain = email.rsplit("@", 1)
	if len(local_part) > 64 or local_part.startswith(".") or local_part.endswith("."):
		return 
	if ".." in local_part:
		return False

	return bool(_EMAIL_PATTERN.fullmah(email)) and len(domain) <= 253


if __name__ == "__main__":
	import sys

	for address in sys.argv[1:]:
		print(validate_email_address(address))
