
import pandas as pd
from roomate_db import *


def view_user(user,file):
    try:
        if os.path.exists(file):
            df = pd.read_csv(file)
            df.set_index('user',inplace=True)
            df = df.loc[user]
            if len(df)>0:
                return df
        return []
    except Exception as E:
        return []

def check_user(user,file):
    try:
        df = pd.read_csv(file)
        df.set_index('user',inplace=True)
        return str(df.loc[[user]].sum(numeric_only=True).sum())
    except:
        return False

def total_file(file):
    try:
        df = pd.read_csv(file)
        file_sum =df.sum(numeric_only=True).sum()
        return str(file_sum)
    except:
        return False
def pdf_db():
    try:
        obj = rommate_db()
        val = obj.pdf_generated()
        for k in val:
            return k[0]
    except:
        return False
