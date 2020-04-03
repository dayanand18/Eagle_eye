
import re

#full_name,email,company,password,c_password

def is_fullname(name):
    try:
        nms = str(name).split(' ')
        for n in nms:
            if n.isalpha():
                return True
        return False
    except:
        return False

def is_email(mail):
    try:
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        match = re.match(regex,mail)
        if match:
            return True
        return False
    except Exception as E:
        return False

def is_company(company):
    try:
        nms = str(company).split(' ')
        for n in nms:
            if n.isalpha():
                return True
        return False
    except:
        return False

def is_password(p1,p2):
    try:
        if (str(p1) == str(p2)) :
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
            pat = re.compile(reg)
            match = re.search(pat, str(p1))
            if match:
                 return True
        return False
    except:
        return False


def user_input_verified(full_name,email,company,p1,p2):
    try:
        if is_fullname(full_name) and is_email(email) and is_company(company) and is_password(p1,p2):
            return True
        return False
    except:
        return False

