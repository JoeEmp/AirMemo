import rsa
import os

# 生成密钥
(pubkey, privkey) = rsa.newkeys(1024)


# 保存密钥
with open('public.pem', 'w+') as f:
    f.write(pubkey.save_pkcs1().decode())

with open('private.pem', 'w+') as f:
    f.write(privkey.save_pkcs1().decode())


# 导入密钥
with open('public.pem', 'r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

with open('private.pem', 'r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())


# 明文
message = 'hello'

# 公钥加密
crypto = rsa.encrypt(message.encode(), pubkey)

# 私钥解密
message = rsa.decrypt(crypto, privkey).decode()
print(message)


class crypto(object):
    def __init__(self, pub=None, pri=None):
        if pub and pri:
            try:
                with open(pub, 'r') as f:
                    self.pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
                with open('private.pem', 'r') as f:
                    self.__privkey = rsa.PrivateKey.load_pkcs1(
                        f.read().encode())
            except Exception as e:
                print(e)
        else:
            (pubkey, privkey) = rsa.newkeys(1024)
            # 保存密钥
            with open('public.pem', 'w+') as f:
                f.write(pubkey.save_pkcs1().decode())
            with open('private.pem', 'w+') as f:
                f.write(privkey.save_pkcs1().decode())

    def decrypt(self,db_file):
        with open(db_file,'r') as f:
            crypto = rsa

    def encrypt(self):
        pass


if __name__ == "__main__":
    os.chdir('/'.join(__file__.split('/')[:-1]))
    db_file = "Air.db"
    pem = {
        "public": "public.pem",
        "private": "private.pem"
    }
