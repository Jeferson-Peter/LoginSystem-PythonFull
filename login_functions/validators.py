import re

class Validator:
    def password(self, password):
        SpecialSym = ['$', '@', '#', '%', '!', '&', '*']
        val = True

        if len(password) < 10:
            print('length should be at least 10')
            val = False

        if not any(char.isdigit() for char in password):
            print('Password should have at least one numeral')
            val = False

        if not any(char.isupper() for char in password):
            print('Password should have at least one uppercase letter')
            val = False

        if not any(char.islower() for char in password):
            print('Password should have at least one lowercase letter')
            val = False

        if not any(char in SpecialSym for char in password):
            print('Password should have at least one of the symbols $@#')
            val = False
        if val:
            return val

    def password_with_regex(self, password):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,}$"
        # compiling regex
        pat = re.compile(reg)

        # searching regex
        mat = re.search(pat, password)

        # validating conditions
        if mat:
            return True
        else:
            return False


    def email_with_regex(self, email):

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,200}\b'
        if (re.fullmatch(regex, email)):
            return True
        else:
            return False


