from lib.Spammer import Spammer
from utils.io import question, log
from utils.interfaces import banner
from utils.functions import is_production
from utils.colors import blue, white, yellow

def main ():
    print (banner)
    
    log ("info", f"""
      {blue}input spam target{white}
      example: {yellow}08xxxxxxxxx1{white}, {yellow}08xxxxxxxxx2{white}
    """)
    
    target = question("input spam target")
    total = int(question("total spam"))
    targets = target.split(",")
    
    for phone in targets:
        phone = phone.strip()
        
        for x in range(total):
            spammer = Spammer(target=phone)
            spammer.start()

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        if not is_production():
            raise error
        log("info", "error occured, restarting script !")
        main()
