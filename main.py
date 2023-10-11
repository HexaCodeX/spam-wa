from utils.io import question
from utils.interfaces import question
from utils.colors import blue, white, yellow

if __name__ == "__main__":
    print (banner)
    
    log ("info", f"""
      {blue}input spam target{white}
      example: {yellow}628xxxxx1{white}, {yellow}628xxxxx2{white}
    """)
    
    target = question("input spam target")
    targets = targets.split(",")
    
    for phone in targets:
        spammer = Spammer(target=phone)
        spammer.start()