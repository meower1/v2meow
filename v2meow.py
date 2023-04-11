#first i must install the xray core v1.8.0
import os
import subprocess
import json

def install_xray():
    os.system("bash -c \"$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)\" @ install -u root --version 1.8.0")

#this function will generate all the neccesary parameters and assign them to the correct variable 
def generate_variables():
    
    global private_key
    global public_key
    global uuid
    global shortid
    global serverip

    #this section generates a pair of private and public key and stores them inside private_key and public_key variables
    x25519 = subprocess.check_output("xray x25519", shell=True)
    privkey_str = x25519.decode("utf-8")

    private_key = privkey_str[13:57]
    public_key = privkey_str[69:112]

    #this section will generate uuid and put it inside uuid variable
    uuid_byte = subprocess.check_output("xray uuid", shell=True)
    uuid = uuid_byte.decode("utf-8")

    #this section will generate shortId and will put it inside shortid variable
    shortid_btye = subprocess.check_output("openssl rand -hex 8", shell=True)
    shortid = shortid_btye.decode("utf-8")

    #this section will get the server's ip and put it inside serverip variable
    serverip_byte = subprocess.check_output("curl ifconfig.me", shell=True)
    serverip = serverip_byte.decode("utf-8")

def createconfig():
    with open("config.json", "r") as f:
        data = json.load(f)

        #uuid
        data["inbounds"][0]["settings"]["clients"][0]["id"] = uuid.rstrip()

        #private_key
        print(data["inbounds"][0]["streamSettings"]["realitySettings"]["privateKey"])
        data["inbounds"][0]["streamSettings"]["realitySettings"]["privateKey"] = private_key.rstrip()

        #shortids
        data["inbounds"][0]["streamSettings"]["realitySettings"]["shortIds"][0] = shortid.rstrip()

        

    with open("/Users/meower1/Documents/testdir/config.json", "w") as f:
        json.dump(data,f, indent=4)



generate_variables()
createconfig()
#remember to change the createconfig and replace the destination folder of xray config
