import base64
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
#from cryptography.fernet import Fernet
from datetime import datetime
dt = "2020,3,31,20,01"





frm = "2020,3,31,22,1"
to = "2020,4,1,12,01"
user = 'Dayaayb@gmail.com'
K = "Techabcdtechnologies@321!"
lkey = "TechABCD%"+user.lower()+"%"+K+"%Authorizefrom%"+frm+"$*"+to+"%NUser"

#key = Fernet.generate_key() #this is your "password"
key = "Tech@abcd!1@2#3$4Tech@abcd!1@2#3"
print(len(key))


class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]