import requests
from bs4 import BeautifulSoup
from huepy import *
    
def param_generator_combination(form,xss_payloads):
    dicList=[]
    for payload in xss_payloads:
        temp_dict={}
        for input_tag in form.find_all("input"):
            if input_tag["type"] != "submit":
                input_tag["value"] = payload
                temp_dict.update({input_tag["name"]:input_tag["value"]})
            if input_tag["type"] == "email":
                input_tag["value"]="123@email.com"
                temp_dict.update({input_tag["name"]:input_tag["value"]})
            if input_tag["type"] == "number":
                input_tag["value"]=1234567890
                temp_dict.update({input_tag["name"]:input_tag["value"]})
        for textarea in form.find_all("textarea"):
            textarea["value"]=payload
            temp_dict.update({textarea["name"]:textarea["value"]})
        dicList.append(temp_dict)
    return dicList


def validator(method,url,payloadList):
    resultList=[]
    for dictionary in payloadList:
        if method.upper()=="POST":
            response=requests.post(url=url,data=dictionary)
        else:
            response=requests.get(url=url,params=dictionary)
        for dict_key in dictionary:
            if dictionary[dict_key] in response.text:
                resultList.append(bad(f"XSS vulnerability found in input '{yellow(dict_key)}' with payload {yellow(dictionary[dict_key])}"))
            else:
                resultList.append(good(f"No XSS vulnerability found in input '{yellow(dict_key)}' with payload {yellow(dictionary[dict_key])}"))
    return resultList
        

def injection(url,filename="payload.txt"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    xss_payload=[]
    
    form =soup.find("form")
    xss_payload=[]

    try:
        method=form["method"]
    except:
        method="GET"
    else:
        method=form["method"]

    file=open(filename,"r",encoding="utf-8")
    for payload in file:
        xss_payload.append(payload)
    

    payloadList=param_generator_combination(form,xss_payload)
    
    new_url=url+form["action"]
    return validator(method,new_url,payloadList)


    
    


