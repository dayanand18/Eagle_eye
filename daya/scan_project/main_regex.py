import re

def file_search(path,selected_itms):
    result = {"ADHAR": [], "PANCARD": [], "MOBILE": [], "EMAIL": [], "IP": []}
    try:
        for itm in selected_itms:
            with open(path,'r') as f:
                file = f.read()
                if itm == "ADHAR":
                    aadhar = re.findall('\d{1,4}\s\d{1,4}\s\d{1,4}', file)
                    result["ADHAR"].__iadd__(aadhar)
                elif itm == "PAN":
                    pan = re.findall('[A-Z]{5}[0-9]{4}[A-Z]', file)
                    result["PANCARD"].__iadd__(pan)
                elif itm == "EMAIL":
                    mails = re.findall('\S+@\S+', file)
                    result["EMAIL"].__iadd__(mails)
                elif itm == "MOBILE":
                    contact = re.findall('[0-9]{10}', file)
                    result["MOBILE"].__iadd__(contact)
                elif itm == "IP":
                    ips = re.findall('\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}', file)
                    result["IP"].__iadd__(ips)
                else:
                    print("no match")
    except Exception as E:
        print(E)
    print(result)
# file_search(r'C:\Users\junaidkhan\PycharmProjects\untitled1\sample.txt',['MOBILE'])
