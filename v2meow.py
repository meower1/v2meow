#this script will make a vless-xtls-utls-reality config
import os
import subprocess
import json


def xtls_reality():

    def install_xray():
        os.system("bash -c \"$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)\" @ install -u root --version 1.8.0")

    #enables google's tcp bbr
    def enablebbr():
        if "net.core.default_qdisc=fq" in open("/etc/sysctl.conf").read():
            print("BBR is already enabled.")
            return
        else:
            print("Enabling BBR...")
            os.system("echo \"net.core.default_qdisc=fq\" >> /etc/sysctl.conf")
            os.system("echo \"net.ipv4.tcp_congestion_control=bbr\" >> /etc/sysctl.conf")
            os.system("sudo sysctl -p")

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
        uuid = uuid_byte.decode("utf-8").rstrip()

        #this section will generate shortId and will put it inside shortid variable
        shortid_btye = subprocess.check_output("openssl rand -hex 8", shell=True)
        shortid = shortid_btye.decode("utf-8").rstrip()

        #this section will get the server's ip and put it inside serverip variable
        serverip_byte = subprocess.check_output("curl ifconfig.me", shell=True)
        serverip = serverip_byte.decode("utf-8")

    def createconfig():
        with open("configs/configxtls.json", "r") as f:
            data = json.load(f)

            #uuid
            data["inbounds"][0]["settings"]["clients"][0]["id"] = uuid.rstrip()

            #private_key
            data["inbounds"][0]["streamSettings"]["realitySettings"]["privateKey"] = private_key.rstrip()

            #shortids
            data["inbounds"][0]["streamSettings"]["realitySettings"]["shortIds"][0] = shortid.rstrip()

            
        #change back to /usr/local/etc/xray/config.json
        with open("/usr/local/etc/xray/config.json", "w") as f:
            json.dump(data,f, indent=4)

    #this function will create the vless link and start the xray service
    def createlink():
        print(f"""vless://{uuid}@{serverip}:443?security=reality&encryption=none&pbk={public_key}&headerType=none&fp=chrome&spx=%2F&type=tcp&flow=xtls-rprx-vision&sni=www.samsung.com&sid={shortid}#Vless-XTLS-uTLS-Reality""".replace(" ",""))
        os.system("systemctl restart xray")
        os.system("systemctl enable xray")


    install_xray()
    try:
        enablebbr()
    except:
        print("failed to activate BBR.")
    generate_variables()
    createconfig()
    createlink()


def h2_reality():

    def install_xray():
        os.system("bash -c \"$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)\" @ install -u root --version 1.8.0")

    #enables google's tcp bbr
    def enablebbr():
        if "net.core.default_qdisc=fq" in open("/etc/sysctl.conf").read():
            print("BBR is already enabled.")
            return
        else:
            print("Enabling BBR...")
            os.system("echo \"net.core.default_qdisc=fq\" >> /etc/sysctl.conf")
            os.system("echo \"net.ipv4.tcp_congestion_control=bbr\" >> /etc/sysctl.conf")
            os.system("sudo sysctl -p")

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
        uuid = uuid_byte.decode("utf-8").rstrip()

        #this section will generate shortId and will put it inside shortid variable
        shortid_btye = subprocess.check_output("openssl rand -hex 8", shell=True)
        shortid = shortid_btye.decode("utf-8").rstrip()

        #this section will get the server's ip and put it inside serverip variable
        serverip_byte = subprocess.check_output("curl ifconfig.me", shell=True)
        serverip = serverip_byte.decode("utf-8")

    def createconfig():
        with open("configs/configh2.json", "r") as f:
            data = json.load(f)

            #uuid
            data["inbounds"][0]["settings"]["clients"][0]["id"] = uuid.rstrip()

            #private_key
            data["inbounds"][0]["streamSettings"]["realitySettings"]["privateKey"] = private_key.rstrip()

            #shortids
            data["inbounds"][0]["streamSettings"]["realitySettings"]["shortIds"][0] = shortid.rstrip()

            
        #change back to /usr/local/etc/xray/config.json
        with open("/usr/local/etc/xray/config.json", "w") as f:
            json.dump(data,f, indent=4)

    #this function will create the vless link and start the xray service
    def createlink():
        print(f"""vless://{uuid}@{serverip}:443?path=%2F&security=reality&encryption=none&pbk={public_key}&fp=chrome&type=http&sni=www.samsung.com&sid={shortid}#Vless-h2-uTLS-Reality""".replace(" ", ""))
        os.system("systemctl restart xray")
        os.system("systemctl enable xray")


    install_xray()
    try:
        enablebbr()
    except:
        print("failed to activate BBR.")
    generate_variables()
    createconfig()
    createlink()    
    

def grpc_reality():

    def install_xray():
        os.system("bash -c \"$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)\" @ install -u root --version 1.8.0")

    #enables google's tcp bbr
    def enablebbr():
        if "net.core.default_qdisc=fq" in open("/etc/sysctl.conf").read():
            print("BBR is already enabled.")
            return
        else:
            print("Enabling BBR...")
            os.system("echo \"net.core.default_qdisc=fq\" >> /etc/sysctl.conf")
            os.system("echo \"net.ipv4.tcp_congestion_control=bbr\" >> /etc/sysctl.conf")
            os.system("sudo sysctl -p")

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
        uuid = uuid_byte.decode("utf-8").rstrip()

        #this section will generate shortId and will put it inside shortid variable
        shortid_btye = subprocess.check_output("openssl rand -hex 8", shell=True)
        shortid = shortid_btye.decode("utf-8").rstrip()

        #this section will get the server's ip and put it inside serverip variable
        serverip_byte = subprocess.check_output("curl ifconfig.me", shell=True)
        serverip = serverip_byte.decode("utf-8")

    def createconfig():
        with open("configs/configgrpc.json", "r") as f:
            data = json.load(f)

            #uuid
            data["inbounds"][0]["settings"]["clients"][0]["id"] = uuid.rstrip()

            #private_key
            data["inbounds"][0]["streamSettings"]["realitySettings"]["privateKey"] = private_key.rstrip()

            #shortids
            data["inbounds"][0]["streamSettings"]["realitySettings"]["shortIds"][0] = shortid.rstrip()

            
        #change back to /usr/local/etc/xray/config.json
        with open("/usr/local/etc/xray/config.json", "w") as f:
            json.dump(data,f, indent=4)

    #this function will create the vless link and start the xray service
    def createlink():
        print(f"""vless://{uuid}@{serverip}:443?mode=multi&security=reality&encryption=none&pbk={public_key}&fp=chrome&type=grpc&serviceName=grpc&sni=www.samsung.com&sid={shortid}#Vless-grpc-uTLS-Reality""".replace(" ", ""))
        os.system("systemctl restart xray")
        os.system("systemctl enable xray")
        


    install_xray()
    try:
        enablebbr()
    except:
        print("failed to activate BBR.")
    generate_variables()
    createconfig()
    createlink()

def delete_reality():
    os.system("bash -c \"$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)\" @ remove")

def exit():
    pass

mode = int(input("Welcome! please choose your preffered protocol : \n1. VLESS-XTLS-uTLS-Reality (Recommended) \n2. VLESS-grpc-uTLS-Reality \n3. Vless-h2-uTLS-Reality \n4. Uninstall \n5. exit \nOption : "))
if mode == 1:
    xtls_reality()
elif mode == 2:
    grpc_reality()
elif mode == 3:
    h2_reality()
elif mode == 4:
    delete_reality()
elif mode == 5:
    exit()