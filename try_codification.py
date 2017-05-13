import rsa
from rsa import *

(key_pub, key_private) = rsa.newkeys(512)


#a = int(input())
#b = int(input())
#c = int(input())

codif_a = 1268311464890071164077654130442639735793047525428368396496951129829722322898852661840396132147470917823602009323168501532331145808858080426945819079209569
codif_b = 7256740014320341393958122338101859180203216511626560517015345432942977465652673977
codif_c = 1161582212187755628028874712607128608937332411982927662675347898961443333

key_pub = PublicKey(8429300119105627611820020154834122336950507623364666829045805313421611595921389330869211032628871733639648291452723589778413393745776595967250234809245341, 65537)
key_private = PrivateKey(8429300119105627611820020154834122336950507623364666829045805313421611595921389330869211032628871733639648291452723589778413393745776595967250234809245341, 65537,codif_a, codif_b, codif_c)

def codificate(message):
    crypto = rsa.encrypt(message.encode("KOI8-R"), key_pub)
    return crypto.decode("KOI8-R")

def decodificate(crypto):
    k = crypto.encode("KOI8-R")
    return rsa.decrypt(k, key_private).decode("KOI8-R")

c = 'Zhukovskiy Pitux'

print(decodificate(codificate(c)))