# :star2: Description

One-click Vless-Reality setup with customizable transmission protocol 

## :eyes: Supported modes

> <h3> Automatic Mode : (Recommended) </h3>
Automatically finds the best sni for your server and makes an xtls reality config in one click 


> <h3> Manual Mode :</h3> 

- Manually set the following :
  - Transfer protocol (XTLS - GRPC - H2)
  - Port (default = 443)
  - Sni (default = auto)

> <h3> Sni Finder :</h3>
Scans a modifiable list of sni's inside tlsping/sni.txt and returns the one with the lowest tls latency

## :gear: Setup:

Paste these commands in your terminal : 

` sudo apt install git curl -y ` <br>
` git clone https://github.com/meower1/v2meow.git `<br>
` cd v2meow `<br>
` python3 v2meow.py `



<!-- Roadmap -->

## :compass: TODO / Roadmap

* [x] 1. Enable BBR
* [x] 2. Add support for H2 and GRPC
* [x] 3. Add manual mode for Sni
* [ ] 4. Make it run on Docker
* [ ] 5. Add a status checker function
* [ ] 6. Add Ascii art and better visuals

<!-- Contributing -->

## :wave: Contributing

Contributions are always welcome!

## License
[MIT License](LICENSE)

# فارسی 

این اسکریپت بصورت اتوماتیک در یک کلیک برای شما سرور ریالیتی میسازه. حالت های پشتیبانی شده بالا نوشته شده. 


# طریقه نصب 
دستور زیر رو توی ترمینالتون کپی و پیست کنین.

` curl https://raw.githubusercontent.com/meower1/v2meow/master/v2meow.py -o /tmp/v2meow.py && python3 /tmp/v2meow.py `




