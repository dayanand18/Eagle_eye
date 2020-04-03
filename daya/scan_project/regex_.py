import re

class glob_lst:
    lst = []
    regex_list = []
    result = {"ADHAR": [], "PAN": [], "MOBILE": [], "EMAIL": [], "IP": []}

def file_search(path):
    try:
        for itm in glob_lst.lst:
            if itm.isChecked():
                select_regex(itm.text())
        with open(path,'r') as f:
            content = f.read()
            for Type,reg in glob_lst.regex_list:

                if not content:
                    break
                found = re.findall(reg, content)

                glob_lst.result[Type].__iadd__(found)
    except Exception as E:
        pass
        return False

def select_regex(select):
    try:
        regexes = {"ADHAR":'\d{4}\s?\d{4}\s?\d{4}',
                  "PAN":'[A-Z]{5}[0-9]{4}[A-Z]',
                   "EMAIL":'\S+@\S+',
                   "MOBILE":'[0-9]{10}',
                   "IP":'\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}'}
        reg = regexes.get(select)
        if reg:
            glob_lst.regex_list.append((select,reg))
    except:
        pass
