# _*_ coding: UTF-8 _*_
# By A.S => @eagle.js

from bs4 import BeautifulSoup
import requests

def find_hosting(fname, rname):
    try:
        f = open(fname, "r")
        ln = f.readlines()
        x = open(rname,"w+")
        for line in ln:
            ip = str(line.strip())
            ipt = str(line.strip())
            if ip.find(":") != -1:
                ip = ip[0:-5]
            if ip.find(" - ") != -1:
                ip = ip[0:ip.find(" - ")]
            page = requests.get("https://www.whoismyisp.org/ip/" + ip)
            soup = BeautifulSoup(page.content, 'html.parser')
            item = soup.find_all(class_="isp")[0]
            item = str(item)
            tmp = item.upper()
            tmp2 = tmp.find("</p>")
            print(ipt + " - " + tmp[15:tmp2-3])
            x.write(ipt + " - " + tmp[15:tmp2-3] + "\n")
        print("|-------------------- Finished --------------------|")
        x.close()    
    except:
        print("File Not Found !")


def filter_ip(n, h, r, ch):
    try:
        f = open(n, "r")
        h = str(h.upper())
        if h.find("+") != -1:
            h = list(h.split("+"))
        else:
            h = list(h)
        ln = f.readlines()
        ch = ch.upper()
        
        tl = []
        tlp = []
        
        x = open(r,"w+")
        
        for line in ln:
            ip = str(line.strip())
            ipt = str(line.strip())
            if ip.find(":") != -1:
                ip = ip[0:-5]
            page = requests.get("https://www.whoismyisp.org/ip/" + ip)
            soup = BeautifulSoup(page.content, 'html.parser')
            item = soup.find_all(class_="isp")[0]
            item = str(item)
            tmp = item.upper()
            tmp2 = tmp.find("</p>")
            tl.append(tmp[15:tmp2-3])
            tlp.append(ipt)
        if ch == "Y":  
            for tb in h:
                for bb in tl:
                    if tb == bb:
                        tl.pop(h.index(tb))
                        tlp.pop(h.index(tb))
            for xl in tl:
                print(tlp[tl.index(xl)] + " - " + xl)
                x.write(tlp[tl.index(xl)] + " - " + xl + "\n")
        elif ch == "N":
            for tb in h:
                for bb in tl:
                    if tb == bb:
                        tl.pop(h.index(tb))
                        tlp.pop(h.index(tb))
            for xl in tl:
                print(tlp[tl.index(xl)])
                x.write(tlp[tl.index(xl)] + "\n")            
        else:
            print("   Error !")
            
        x.close()    
        print("|-------------------- Finished --------------------|")        
    except:
        print("    Error!")


status = True        
while status:
    print('''
|--------------- Ip Locator Started ---------------|
|----------------- Ver 1.0 By A.s -----------------|
|                                                  |
| 1. Start Searching                               |
| 2. Filter                                        |
| 3. Exit                                          |
|--------------------------------------------------|
''')
    
    app_status = input("[*] => ")
    if app_status == "1" :
        get_fname = input("  Enter ip file name => ")
        get_rname = input("  Enter result file name => ")
        find_hosting(get_fname, get_rname)
    elif app_status == "2":
        get_fname = input("  Enter ip file name => ")
        get_hname = input("  Enter hosting name => ")
        get_rname = input("  Enter result file name => ")
        get_ch = input("  Want to print the location too ? (Y/N) => ")
        filter_ip(get_fname, get_hname, get_rname, get_ch)
    elif app_status == "3" :
        status = False

    print("|--------------------------------------------------|")

