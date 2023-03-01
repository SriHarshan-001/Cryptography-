import sys
import time
import AOI
from pyfiglet import Figlet
from huepy import *

custom_fig = Figlet(font='nipples')
usage_msg="\tUsage: " + sys.argv[0] +" (-u) [url]"
help_msg=     usage_msg + "\n" +\
            "\tExample:\n" +\
            "\tTo Start an XSS Injection Attack on an URL: https://demopage.com, do:\n " +\
            "\t$python3 " + sys.argv[0] + " -u https://demopage.com -f <filename>'\n" +\
            "\tif -f option not provided, it will use default payload txtfile-->payload.txt\n" 

if len(sys.argv) < 2 or len(sys.argv) >5 :
    print(usage_msg)
    sys.exit(1)

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print()
    print()
    print(cyan(custom_fig.renderText('d  X  S  S')))
    print(orange(help_msg))
    sys.exit(1)

elif sys.argv[1] == "-u":
    try:
        if sys.argv[3]=="-f":
            resultList=AOI.injection(sys.argv[2],sys.argv[4])
    except:
        resultList=AOI.injection(sys.argv[2])
    for output in resultList:
        print(output)
        print(cyan("----------------------------------------------------------------------------------------------------------------------------"))
        time.sleep(1)
else:
    print("Unrecognized first argument: "+ sys.argv[1])
    print("Please use '-u', '-h', or '--help'.")