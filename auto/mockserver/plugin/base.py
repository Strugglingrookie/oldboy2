#coding=utf-8
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import yaml,os,hashlib,base64,sys,hmac
reload(sys)
sys.setdefaultencoding('utf-8')

_config = yaml.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)),"config.yml")))

def getCfgValue(*args):
    ret = _config
    for arg in args:
        ret = ret.get(arg)
    return ret

def md5(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()


def rsa_decrypt(encrypt_text):
    pem_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "exts", "private.pem")
    random_generator = Random.new().read
    with open(pem_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
    return text

def hmac_sha256_encrypt(message,secret):
    message = bytes(message).encode('utf-8')
    secret = bytes(secret).encode('utf-8')
    signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
    return signature

