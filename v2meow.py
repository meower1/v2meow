#this script will make a vless-xtls-utls-reality config
import os
import subprocess
import json
import re


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
        os.system("clear")
        print("Thank you for using my script :).\n Your link is : \n")

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
        os.system("clear")
        print("Thank you for using my script :).\n Your link is : \n")

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
        os.system("clear")
        print("Thank you for using my script :).\n Your link is : \n")

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

def manual_mode():
    os.system("clear")
    mode = int(input("Select protocol : \n1. VLESS-XTLS-uTLS-Reality (Recommended) \n2. VLESS-grpc-uTLS-Reality \n3. Vless-h2-uTLS-Reality \nOption :  "))  

    if mode == 1:
        xtls_reality()
        config = "configs/configxtls.json"
    elif mode == 2:
        grpc_reality()
        config = "configs/configgrpc.json"
    elif mode == 3:
        h2_reality()
        config = "configs/configh2.json"

    os.system("clear")

    with open(config, "r") as f:
        data = json.load(f)
    
    sni_dest = input("Enter SNI : ")

    #uuid
    data["inbounds"][0]["settings"]["clients"][0]["id"] = uuid.rstrip()

    #private_key
    data["inbounds"][0]["streamSettings"]["realitySettings"]["privateKey"] = private_key.rstrip()

    #shortids
    data["inbounds"][0]["streamSettings"]["realitySettings"]["shortIds"][0] = shortid.rstrip()

    data["inbounds"][0]["streamSettings"]["realitySettings"]["serverNames"][0] = sni_dest

    data["inbounds"][0]["streamSettings"]["realitySettings"]["dest"] = f"{sni_dest}:443"

    #change back to /usr/local/etc/xray/config.json
    with open("/usr/local/etc/xray/config.json", "w") as f:
        json.dump(data,f, indent=4)

    os.system("systemctl restart xray")
    os.system("systemctl enable xray")
    os.system("clear")

    print(f"Thank you for using my script :).\nCustom sni : {sni_dest}\nYour link is : \n")

    if mode == 1:
        print(f"""vless://{uuid}@{serverip}:443?security=reality&encryption=none&pbk={public_key}&headerType=none&fp=chrome&spx=%2F&type=tcp&flow=xtls-rprx-vision&sni={sni_dest}&sid={shortid}#Vless-XTLS-uTLS-Reality""".replace(" ",""))
    elif mode == 2:
        print(f"""vless://{uuid}@{serverip}:443?mode=multi&security=reality&encryption=none&pbk={public_key}&fp=chrome&type=grpc&serviceName=grpc&sni={sni_dest}&sid={shortid}#Vless-grpc-uTLS-Reality""".replace(" ", ""))
    elif mode == 3:
        print(f"""vless://{uuid}@{serverip}:443?path=%2F&security=reality&encryption=none&pbk={public_key}&fp=chrome&type=http&sni={sni_dest}&sid={shortid}#Vless-h2-uTLS-Reality""".replace(" ", ""))

def find_best_sni():

    result = []
    avg_value_list = []
    domain_ping_dict = {}

    my_file = open("tlsping/sni.txt", "r")
    
    data = my_file.read()
    
    # replacing end splitting the text 
    # when newline ('\n') is seen.
    sni_list = data.split("\n")
    my_file.close()

    #this tests all the domains in sni.txt file and puts them in a list called result
    try:
        for i in sni_list:
            x= subprocess.check_output(f"tlsping/tlsping {i}:443", shell=True).rstrip().decode('utf-8')
            result.append(x)
    except:    
        pass
        
    #this extracts all the avg tlsping values from the domains
    try:
        for j in result:
        # use regular expressions to extract the "avg" value
            avg_value = re.findall(r"avg/.*?ms.*?(\d+\.?\d*)ms", j )[0]
            avg_value_list.append(avg_value)
    except:
        pass

    # this puts the sni_list values inside domain_ping_dict as keys and the avg_value_list values as values

    print(avg_value_list)
    domain_ping_dict = {sni_list[i]: float(avg_value_list[i]) for i in range(len(sni_list))}

    #this sorts the dictionary by the values in ascending order
    sorted_dict = dict(sorted(domain_ping_dict.items(), key=lambda item: item[1]))

    # #and here's our final result yayy
    best_sni = list(sorted_dict.keys())[0]
    print(best_sni)

    os.system("clear")
    print("Best SNI is : " + best_sni)
    print("\nPlease use manual mode and enter this sni :)\n")




def menu():
    os.system("clear")
    mode = int(input("Welcome! please choose your preffered protocol : \n1. VLESS-XTLS-uTLS-Reality (Recommended) \n2. VLESS-grpc-uTLS-Reality \n3. Vless-h2-uTLS-Reality \n4. Manual Mode \n5. Find the best sni for your server \n6. Uninstall \n7. exit \nOption : "))
    if mode == 1:
        xtls_reality()
    elif mode == 2:
        grpc_reality()
    elif mode == 3:
        h2_reality()
    elif mode == 4:
        manual_mode()
    elif mode == 5:
        find_best_sni()
    elif mode == 6:
        delete_reality()
    elif mode == 7:
        exit()


try : 
    menu()
except ValueError:
    print("invalid input")

#tls scanner snapshot 1

