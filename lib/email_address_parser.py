import re

class EmailAddressParser:
    def __init__(self, string):
        self.string = string

    def parse(self):
        # Regex pattern to match email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        # Find all matches
        emails = re.findall(email_pattern, self.string)
        # Return unique emails sorted alphabetically
        return sorted(set(emails))
