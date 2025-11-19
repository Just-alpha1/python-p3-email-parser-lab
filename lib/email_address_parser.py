import re

class EmailAddressParser:
    def __init__(self, string):
        self.string = string

    def parse(self):
        
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
     
        emails = re.findall(email_pattern, self.string)
        
        return sorted(set(emails))
