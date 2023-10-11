from utils.colors import *

icons = {
  "warning": f"[{yellow}!{white}]",
  "info": f"[{blue}•{white}]",
  "danger": f"[{red}∆{white}]",
  "success": f"[{green}✓{white}]",
  "log": f"[{white}<>{white}]",
}

def question (text):
    return input(f"[{gray}?{white}] {text}: ")

def confirm (text):
    _input_ = input(f"[{purple}?{white}] {text} [y/n]: ")
    if _input_ in ["y", "yes"]:
        return True
    elif _input_ in ["n", "no"]:
        return False
    else:
        return confirm(text)

def log (key, text):
    icon_keys = list(icons.keys())
    if not key in icon_keys:
        raise Exception("danger", f"icon with label '{key}' is doesn't exists !")
    
    icon = icons[key]
    print (f"{ icon }: { text }")