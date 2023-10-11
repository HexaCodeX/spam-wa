from utils.colors import *
from lib.Config import Config

banner = f"""
{ blue }
____ ___  ____ _  _ _  _ ____ ____    _ _ _ ____ 
[__  |__] |__| |\/| |\/| |___ |__/    | | | |__| 
___] |    |  | |  | |  | |___ |  \    |_|_| |  | 
                                                 
{ white }

Author          : { blue } { Config.author } { white }
Github          : { blue } github.com/{ Config.author } { white }
Repository      : { blue } github.com/{ Config.author }/spam-wa { white }
Version         : { blue } { Config.version } { white }
"""