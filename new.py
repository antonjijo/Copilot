import os
import time
import sys
import pwinput




def center_text(text, width):
    return text.center(width)

terminal_width = os.get_terminal_size().columns


print("\n" + center_text("~ PY & CO ~", terminal_width))
print("\n\n" + center_text("Email:antonjijo2018@outlook.com", terminal_width))
print("\n" + center_text("Contact us : +91 8015687633", terminal_width))

print("\n")
animation = "|/-\\"
for i in range(30):
    time.sleep(0.3)
    sys.stdout.write("\r" + center_text("Loading..." + animation[i % len(animation)], terminal_width))
    sys.stdout.flush()

print("\n\n" + center_text("//~ Loaded Successfully ~//", terminal_width))
input(center_text("Press enter to continue...", terminal_width))

class Laptop:
    price = 0
    processor = ""
    ram = ""
    graphics = ""
    os = ""
    cooler = ""
    display = ""

HP = Laptop()
HP.price = 54999
HP.processor = "i5 7th gen"
HP.ram = "16GB"
HP.graphics = "Nvidia 3050 with 2.69GHZ"
HP.os = "WIN 11"
HP.cooler = "HP integrated cooling vapour system"
HP.display = "15.2inch 4k Amoled Display with 120HZ Refresh rate"

ASUS = Laptop()
ASUS.price = 174999
ASUS.processor = "i7 13th gen with Asus Chip Gen 2"
ASUS.ram = "32GB"
ASUS.graphics = "Nvidia RTX 4070 Super with 3.19GHZ"
ASUS.os = "WIN 11 with integrated Asus Gaming Themes"
ASUS.cooler = "ASUS ROG integrated Gaming cooler with specified cooling chambers"
ASUS.display = "17inch 2.7k Super Amoled Display with Adaptive 144HZ Refresh rate"

MS = Laptop()
MS.price = 2000000
MS.processor = "Snapdragon X Elite"
MS.ram = "64GB"
MS.graphics = "Qualcomm AI Engine"
MS.os = "WIN 11 with Microsoft 365+Copilot"
MS.cooler = "Microdoft Internal Cooling System with cooling chambers"
MS.display = "2-in-1 15inch HDR Display with 120HZ Refresh Rate touch screen"

DELL = Laptop()
DELL.price = 44999
DELL.processor = "Amd Ryzen 5"
DELL.ram = "16GB"
DELL.graphics = "AMD Radeon RX 7600 with 1.89GHZ"
DELL.os = "WIN 11"
DELL.cooler = "DELL cooling vapour"
DELL.display = "15.2inch Amoled Display with 80HZ Refresh rate"

print("\n" + center_text("----- PY & CO -----", terminal_width))
print("\nemail: antonjijo@outlook.com")
print("Phone no: +91 8015687633")

while True:
    member_type = input("\nMember or Customer: ")
    member = member_type.lower()
    if member == "member":
        print("\n")
        animation = "|/-\\"
        for i in range(10):
            time.sleep(0.3)
            sys.stdout.write("\r" + center_text("Loading..." + animation[i % len(animation)], terminal_width))
            sys.stdout.flush()
        print("\n\n" + center_text("------- PY & CO -------", terminal_width))
        print("\n" + center_text("<<<<<<<< Member Login Page >>>>>>>>", terminal_width))
        print("\n" + center_text("*** Username & Password ***", terminal_width))
        
        while True:
            username = input("  Enter your username: ")
            password = pwinput.pwinput(prompt='  Enter your password: ', mask='*')
            
            if username == "Jijo" and password == "Py & Co":
                print("\n" + center_text("Your Account is Logged in", terminal_width))
                input("\n" + center_text("<<<<<<<< Continue >>>>>>>>", terminal_width))
                print("\n" + center_text("---------- PY & CO ----------", terminal_width))
                print("\n" + center_text("------------------------------------------------------------------------------------", terminal_width))
                print("\n" + center_text("Location: https://maps.app.goo.gl/ftot14dAKEKyprqc7", terminal_width))
                print(center_text("Email:antonjijo2018@outlook.com", terminal_width))
                print("\n" + center_text("------------ Thanks for visiting --------------", terminal_width))
                input()
                break  
            else:
                print("\n" + center_text("The Username or Password is Incorrect !", terminal_width))
                retry_type = input(center_text("Do you want to try again? (yes/no):", terminal_width))
                retry=retry_type.lower()
                if retry!= "yes":
                    break  

    else:
        animation = "|/-\\"
        for i in range(10):
            time.sleep(0.3)
            sys.stdout.write("\r" + center_text("Loading..." + animation[i % len(animation)], terminal_width))
            sys.stdout.flush()
        print("\n" + center_text("-------------------- PY & CO ---------------------", terminal_width))
        print("\n" + center_text("<<<<<<<<<<<<<<<<<<<< DEALS FOR FESTIVAL SEASON >>>>>>>>>>>>>>>>>>>>>", terminal_width))
        print("\n" + center_text("--------------- SPECIAL DEALS FOR LAPTOPS ---------------", terminal_width))
        print("\nAvailable laptops are:")
        print("1. ASUS Zephyrus 13 Limited Edition!\n2. HP Victus 14 pro\n3. DELL Latitude E6960\n4. MS Surface Laptop 7th Edition")
        print("\nName one of these laptops .......")
        lap_type = input("Name the brand name to give details : ")
        lap = lap_type.lower()
        if lap == "hp":
            animation = "|/-\\"
            for i in range(10):
              time.sleep(0.3)
              sys.stdout.write("\r" + center_text("Loading..." + animation[i % len(animation)], terminal_width))
              sys.stdout.flush()
            print("\nNAME : HP VICTUS 14 PRO")
            print("\n\n\n" + center_text("--------------- SPECIFICATIONS ---------------", terminal_width))
            print("\nPrice                        : Rs.", HP.price)
            print("Display                      :", HP.display)
            print("Processor                    :", HP.processor)
            print("Cooler                       :", HP.cooler)
            print("Graphics card                :", HP.graphics)
            print("RAM                          :", HP.ram)
            print("Operating System             :", HP.os)
        elif lap == "asus":
            animation = "|/-\\"
            for i in range(10):
              time.sleep(0.3)
              sys.stdout.write("\r" + center_text("Loading..." + animation[i % len(animation)], terminal_width))
              sys.stdout.flush()
            print("\nNAME : ASUS ZEPHYRUS 13 LIMITED EDITION")
            print("\n\n\n" + center_text("--------------- SPECIFICATIONS ---------------", terminal_width))
            print("\nPrice                        : Rs.", ASUS.price)
            print("Display                      :", ASUS.display)
            print("Processor                    :", ASUS.processor)
            print("Cooler                       :", ASUS.cooler)
            print("Graphics card                :", ASUS.graphics)
            print("RAM                          :", ASUS.ram)
            print("Operating System             :", ASUS.os)
        elif lap == "dell":
            animation = "|/-\\"
            for i in range(10):
              time.sleep(0.3)
              sys.stdout.write("\r" + center_text("Loading..." + animation[i % len(animation)], terminal_width))
              sys.stdout.flush()
            print("\nNAME : DELL LATITUDE E6960")
            print("\n\n\n" + center_text("--------------- SPECIFICATIONS ---------------", terminal_width))
            print("\nPrice                        : Rs.", DELL.price)
            print("Display                      :", DELL.display)
            print("Processor                    :", DELL.processor)
            print("Cooler                       :", DELL.cooler)
            print("Graphics card                :", DELL.graphics)
            print("RAM                          :", DELL.ram)
            print("Operating System             :", DELL.os)
        elif lap == "ms" or lap == "microsoft":
            animation = "|/-\\"
            for i in range(10):
              time.sleep(0.3)
              sys.stdout.write("\r" + center_text("Loading..." + animation[i % len(animation)], terminal_width))
              sys.stdout.flush()
            print("\nNAME : MS Surface Laptop 7th Edition")
            print("\n\n\n" + center_text("--------------- SPECIFICATIONS ---------------", terminal_width))
            print("\nPrice                        : Rs.", MS.price)
            print("Display                      :", MS.display)
            print("Processor                    :", MS.processor)
            print("Cooler                       :", MS.cooler)
            print("Graphics card                :", MS.graphics)
            print("RAM                          :", MS.ram)
            print("Operating System             :", MS.os)
        else:
            animation = "|/-\\"
            for i in range(15):
              time.sleep(0.3)
              sys.stdout.write("\r" + center_text("Searching..." + animation[i % len(animation)], terminal_width))
              sys.stdout.flush()
            print("\n" + center_text("Sorry, the laptop you typed is not available in this deal!", terminal_width))
            print(center_text("For other laptops contact ph.no:+91 8015687633\n(or)\nemail:antonjijo2018@outlook.com"))
            
        print("\n" + center_text("Location: https://maps.app.goo.gl/ftot14dAKEKyprqc7", terminal_width))
        print(center_text("Email:antonjijo2018@outlook.com", terminal_width))
        print("\n\n" + center_text("---------------           <<<<<<<<<<<  THANKS FOR VISITING  >>>>>>>>>>>             ---------------", terminal_width))
        print("\n\n\n" + center_text("---------------                  <<<<<<< COME AGAIN >>>>>>>               ---------------", terminal_width))
        input()
        break
    