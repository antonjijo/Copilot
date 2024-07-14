class Laptop:
    price = 0
    processor = ""
    ram = ""
    graphics = ""
    os = ""
    cooler = ""
    display = ""
    

HP = Laptop()
DELL = Laptop()
ASUS = Laptop()

HP.price = 54999
HP.processor = "i5 7th gen"
HP.ram = "8GB"
HP.graphics = "Nvidia 3050 with 2.69GHZ"
HP.os = "WIN 11"
HP.cooler = "HP integrated cooling vapour system"
HP.display = "15.2inch 4k Amoled Display with 120HZ Refresh rate"

ASUS.price = 174999
ASUS.processor = "i7 13th gen with Asus Chip Gen 2"
ASUS.ram = "8GB"
ASUS.graphics = "Nvidia RTX 4070 Super with 3.19GHZ"
ASUS.os = "WIN 11 with integrated Asus Gaming Themes"
ASUS.cooler = "ASUS ROG integrated Gaming cooler with up to 2hrs complete cooling"
ASUS.display = "17inch 2.7k Super Amoled Display with Adaptive 144HZ Refresh rate"

DELL.price = 44999
DELL.processor = "Amd Ryzen 5"
DELL.ram = "8GB"
DELL.graphics = "AMD Radeon RX™ 7600 with 1.89GHZ"
DELL.os = "WIN 11"
DELL.cooler = "DELL cooling vapour"
DELL.display = "15.2inch Amoled Display with 80HZ Refresh rate"

print("--------------- PY & CO ---------------")
print("email: antonjijo@outlook.com")
print("Phone no: +91 8015687633")
print("  ")

while True:
    member_type = input("Member or Customer: ")
    if member_type.lower() == "member":
        print(" -------------------- PY & CO -------------------------")
        print("  <<<<<<<<<<<<<<<<< Member Login Page  >>>>>>>>>>>>>>>>>>>       ")
        print("  ")
        print("               USERNAME  & PASSWORD    ")
        
        while True:
            username = input("  Enter your username: ")
            password = input("  Enter your password: ")
            
            if username == "Jijo" and password == "Py & Co":
                print("                       YOUR ACCOUNT IS LOGGED IN              ")
                input("            <<<<<<<<<<  Continue  >>>>>>>>>>   ")
                print("   ")
                print(" ------------------- PY & CO ----------------------")
                print("--------------------------------------------------")
                print("Location: https://maps.app.goo.gl/ftot14dAKEKyprqc7")
                print("email: antonjijo2018@outlook.com")
                print("  ")
                print("--------------- THANKS FOR VISITING ---------------")
                input(" ")
                break  
            else:
                print("         The username or password is incorrect !         ")
                retry = input("         Do you want to try again? (yes/no): ")
                if retry.lower() != "yes":
                    break  

    else:
        print("------------------------ PY & CO ------------------------")
        print("   ")
        print("  <<<<<<<<<<<<<<<<<<<< DEALS FOR FESTIVAL SEASON >>>>>>>>>>>>>>>>>>>>>   ")
        print("  ")
        print("--------------- SPECIAL DEALS FOR LAPTOPS ---------------")
        print("  ")
        print("Available laptops are:")
        print("1.ASUS Zephyrus 13 Limited Edition!")
        print("2.HP Victus 14 pro")
        print("3.DELL Latitude E6960")
        print("   ")
        print("Name one of these laptops .......")
        lap = input("Name the brand name to search : ")
        if lap.lower() == "hp":
            print("  ")
            print("NAME : HP VICTUS 14 PRO")
            print("  ")
            print("---------- SPECIFICATIONS ---------")
            print("Price                                 : Rs.", HP.price)
            print("Display                             :", HP.display)
            print("Processor                          :", HP.processor)
            print("Cooler                               :", HP.cooler)
            print("Graphics card                    :", HP.graphics)
            print("RAM                                  :", HP.ram)
            print("Operating System             :", HP.os)
        elif lap.lower() == "asus":
            print("  ")
            print("NAME : ASUS ZEPHYRUS 13 LIMITED EDITION")
            print("  ")
            print("---------- SPECIFICATIONS ---------")
            print("Price                                 : Rs.", ASUS.price)
            print("Display                             :", ASUS.display)
            print("Processor                          :", ASUS.processor)
            print("Cooler                               :", ASUS.cooler)
            print("Graphics card                    :", ASUS.graphics)
            print("RAM                                  :", ASUS.ram)
            print("Operating System             :", ASUS.os)
        elif lap.lower() == "dell":
            print("  ")
            print("NAME : DELL LATITUDE E6960")
            print("  ")
            print("---------- SPECIFICATIONS ---------")
            print("Price                                  : Rs.", DELL.price)
            print("Display                              :", DELL.display)
            print("Processor                           :", DELL.processor)
            print("Cooler                                :", DELL.cooler)
            print("Graphics card                     :", DELL.graphics)
            print("RAM                                   :", DELL.ram)
            print("Operating System               :", DELL.os)
        else:
            print("  ")
            print("Sorry, the laptop you typed is not available in this deal!")
            print("   ")
            print("  ")
            print("For other laptops contact ph.no:+91 8015687633")

        print("   ")
        print("Location: https://maps.app.goo.gl/ftot14dAKEKyprqc7")
        print("email: antonjijo2018@outlook.com")
        print("      ")
        print("---------------           <<<<<<<<<<<  THANKS FOR VISITING  >>>>>>>>>>>             ---------------")
        print("  ")
        print("---------------                  <<<<<<< COME AGAIN >>>>>>>               ---------------")
        input(" ")
        break  
