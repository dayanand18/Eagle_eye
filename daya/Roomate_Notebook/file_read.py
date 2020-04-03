import csv
import os
from datetime import datetime as dt
def save_file(user,item,price):

    try:
        fl = str(dt.now().strftime('%B%Y'))+'.csv'
        if os.path.exists(fl):
            write_to_csv(fl,user,item,price)
            return True
        else:
            write_to_csv(fl,user,item,price,header=True)
            return True
    except:
        return False


def write_to_csv(main,user,item,price,header=False):
    try:
        with open(main,'a',newline='') as file:
            fieldnames = ["user","item","price"]
            writer = csv.DictWriter(file,fieldnames= fieldnames)
            if header:
                writer.writeheader()
            writer.writerow({'user':user,'item':item,'price':price})
    except:
        pass

