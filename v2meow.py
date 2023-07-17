import os
import subprocess
import json
import re

xtls_path = "configs/configxtls.json"
h2_path = "configs/configh2.json"
grpc_path = "configs/configgrpc.json"
config_path = "/usr/local/etc/xray/config.json"


def install_xray():
    os.system("bash -c \"$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)\" @ install -u root --version 1.8.3")

# enables google's tcp bbr
def enablebbr():
    try:
        if "net.core.default_qdisc=fq" in open("/etc/sysctl.conf").read():
            print("BBR is already enabled.")
            return
        else:
            print("Enabling BBR...")
            os.system("echo \"net.core.default_qdisc=fq\" >> /etc/sysctl.conf")
            os.system("echo \"net.ipv4.tcp_congestion_control=bbr\" >> /etc/sysctl.conf")
            os.system("sudo sysctl -p")
    except:
        print("failed to activate BBR.")


# this function will generate all the neccesary parameters and assign them to the correct variable
def generate_variables():
    global private_key
    global public_key
    global uuid
    global shortid
    global serverip

    # generate public and private key
    x25519 = subprocess.check_output("xray x25519", shell=True)
    privkey_str = x25519.decode("utf-8")

    private_key = privkey_str[13:57]
    public_key = privkey_str[69:112]

    # generate uuid
    uuid_byte = subprocess.check_output("xray uuid", shell=True)
    uuid = uuid_byte.decode("utf-8").rstrip()

    # generate shortid
    shortid_btye = subprocess.check_output("openssl rand -hex 8", shell=True)
    shortid = shortid_btye.decode("utf-8").rstrip()

    # get server_ip
    serverip_byte = subprocess.check_output("curl ifconfig.me", shell=True)
    serverip = serverip_byte.decode("utf-8")


def createconfig(config_type, sni_dest="www.samsung.com", port=443):
    with open(config_type, "r") as f:
        data = json.load(f)

        # uuid
        data["inbounds"][0]["settings"]["clients"][0]["id"] = uuid.rstrip()

        # private_key
        data["inbounds"][0]["streamSettings"]["realitySettings"]["privateKey"] = private_key.rstrip()

        # shortids
        data["inbounds"][0]["streamSettings"]["realitySettings"]["shortIds"][0] = shortid.rstrip()

        # sni
        data["inbounds"][0]["streamSettings"]["realitySettings"]["serverNames"][0] = sni_dest

        data["inbounds"][0]["streamSettings"]["realitySettings"]["dest"] = f"{sni_dest}:443"

        # port
        data["inbounds"][0]["port"] = port

    with open("/usr/local/etc/xray/config.json", "w") as f:
        json.dump(data, f, indent=4)


def createlink(type, sni="www.samsung.com", port=443):
    if type == "h2":

        os.system("clear")
        print("Thank you for using my script :).\n Your link is : \n")
        print(
            f"""vless://{uuid}@{serverip}:{port}?path=%2F&security=reality&encryption=none&pbk={public_key}&fp=chrome&type=http&sni={sni}&sid={shortid}#Vless-h2-uTLS-Reality""".replace(
                " ", ""))
        os.system("systemctl restart xray")
        os.system("systemctl enable xray")

    elif type == "xtls":

        os.system("clear")
        print("Thank you for using my script :).\n Your link is : \n")
        print(
            f"""vless://{uuid}@{serverip}:{port}?security=reality&encryption=none&pbk={public_key}&headerType=none&fp=chrome&spx=%2F&type=tcp&flow=xtls-rprx-vision&sni={sni}&sid={shortid}#Vless-XTLS-uTLS-Reality""".replace(
                " ", ""))
        os.system("systemctl restart xray")
        os.system("systemctl enable xray")

    elif type == "grpc":

        os.system("clear")
        print("Thank you for using my script :).\n Your link is : \n")
        print(
            f"""vless://{uuid}@{serverip}:{port}?mode=multi&security=reality&encryption=none&pbk={public_key}&fp=chrome&type=grpc&serviceName=grpc&sni={sni}&sid={shortid}#Vless-grpc-uTLS-Reality""".replace(
                " ", ""))
        os.system("systemctl restart xray")
        os.system("systemctl enable xray")


def xtls_reality(sni, port):
    install_xray()
    enablebbr()
    generate_variables()
    createconfig(xtls_path, sni, port)
    createlink("xtls", sni, port)


def h2_reality(sni, port):
    install_xray()
    enablebbr()
    generate_variables()
    createconfig(h2_path, sni, port)
    createlink("h2", sni, port)


def grpc_reality(sni, port):
    install_xray()
    enablebbr()
    generate_variables()
    createconfig(grpc_path, sni, port)
    createlink("grpc", sni, port)


def delete_reality():
    os.system("bash -c \"$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)\" @ remove")


def exit():
    pass


def manual_mode():
    # manually take sni and port from the user

    os.system("clear")
    try:
        mode = int(input(
            "Select protocol : \n1. VLESS-XTLS-uTLS-Reality (Recommended) \n2. VLESS-grpc-uTLS-Reality \n3. Vless-h2-uTLS-Reality \nOption :  "))
    except:
        print("mode : xtls")
        mode = 1
    try:
        sni = input("Please enter sni(default : www.samsung.com) : ")
    except:
        sni = "www.samsung.com"
    try:
        port = int(input("Please enter port(default : 443) : "))
    except:
        port = 443
        print("invalid value, setting default value")

    if mode == 1:
        xtls_reality(sni, port)
    if mode == 2:
        grpc_reality(sni, port)
    if mode == 3:
        h2_reality(sni, port)


def find_best_sni():
    global best_sni
    try:
        result = []
        avg_value_list = []
        domain_ping_dict = {}

        my_file = open("tlsping/sni.txt", "r")

        data = my_file.read()

        # replacing end splitting the text when newline ('\n') is seen.
        sni_list = data.split("\n")
        my_file.close()

        # this tests all the domains in sni.txt file and puts them in a list called result

        for i in sni_list:
            x = subprocess.check_output(f"tlsping/tlsping {i}:443", shell=True).rstrip().decode('utf-8')
            result.append(x)

        # this extracts all the avg tlsping values from the domains

        for j in result:
            # use regular expressions to extract the "avg" value
            avg_value = re.findall(r"avg/.*?ms.*?(\d+\.?\d*)ms", j)[0]
            avg_value_list.append(avg_value)

        # this puts the sni_list values inside domain_ping_dict as keys and the avg_value_list values as values
        print(avg_value_list)
        domain_ping_dict = {sni_list[i]: float(avg_value_list[i]) for i in range(len(sni_list))}

        # this sorts the dictionary by the values in ascending order
        sorted_dict = dict(sorted(domain_ping_dict.items(), key=lambda item: item[1]))

        # final result :)
        best_sni = list(sorted_dict.keys())[0]
        print(best_sni)

        os.system("clear")
        print("Best SNI is : " + best_sni)
        print("\nPlease use manual mode and enter this sni :)\n")
    except:
        pass


def automatic_setup():
    install_xray()
    enablebbr()
    find_best_sni()
    generate_variables()
    createconfig(xtls_path, best_sni)
    createlink("xtls", best_sni)


def menu():
    os.system("clear")
    mode = int(input(
        "Welcome! please choose your preffered protocol : \n1. Automatic setup \n2. Manual setup (manually set the sni) \n3. Find the best sni for your server \n4. Uninstall \n5. exit \nOption : "))
    if mode == 1:
        automatic_setup()
    elif mode == 2:
        manual_mode()
    elif mode == 3:
        find_best_sni()
    elif mode == 4:
        delete_reality()
    elif mode == 5:
        exit()


try:
    menu()
except ValueError:
    print("invalid input")
    exit()
except KeyboardInterrupt:
    print(" Hope to see you again o/ ")
    exit()
