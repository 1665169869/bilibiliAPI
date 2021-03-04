from hashlib import md5
def sign(string):
    m = md5()
    m.update(bytes(string))