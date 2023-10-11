from lib.Spammer import Spammer
from utils.io import question, log
from utils.interfaces import banner
from utils.colors import blue, white, yellow

if __name__ == "__main__":
    print (banner)
    
    log ("info", f"""
      {blue}input spam target{white}
      example: {yellow}628xxxxx1{white}, {yellow}628xxxxx2{white}
    """)
    
    target = question("input spam target")
    targets = target.split(",")
    
    for phone in targets:
        phone = phone.strip()
        
        spammer = Spammer(target=phone)
        spammer.start()