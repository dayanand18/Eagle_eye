import os
import csv
import sys
import re

def file_search(path):
    lst = []
    with open(path, 'r') as f:
        f_read = f.read()
        mobile=re.findall('\d{10}',f_read)
        lst.__iadd__(mobile)
        email=re.findall('\S+@\S+',f_read)
        lst.__iadd__(email)
        Adhar = re.findall('\d{4}\s\d{4}\s\d{4}', f_read)
        lst.__iadd__(Adhar)




    return lst
# file_search('C:\\Users\\junaidkhan\\PycharmProjects\\untitled1\\sample.txt')
#     path = 'C:\\Users\\junaidkhan\\Desktop\\dumy'
#     for root,dirs,files in os.walk(path):
#         for file in files:
#             main = os.path.join(root,file)
#             print(main)
#             if file == user:
#                 if file.endswith('.txt'):
#                     with open(f'{main}','r') as f:
#                         f_read = f.read()
#                         mobile=re.findall('\d{10}',f_read)
#                         print(mobile)
#                         email=re.findall('\S+@\S+',f_read)
#                         print(email)
#                         adhar = re.findall('\d{4}\s\d{4}\s\d{4}', f_read)
#                         print(adhar)
#                         # return mobile,email,adhar
#             else:
#                 try:
#                     var = os.path.join(root,file)
#                     if file==user+'.txt':
#                         with open(f'{var}', 'r') as f:
#                             f_read = f.read()
#                             return f_read
#                 except Exception as E:
#                     print(E)
# file_search('sample')





