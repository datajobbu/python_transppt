import os
import ssl
import json
import urllib.request

import os
import ssl
import json
import urllib.request


def detect_language(txt, dtl_id, dtl_pw):
    """언어감지"""
    papago_detect_id = dtl_id
    papago_detect_secret = dtl_pw
    encQuery = urllib.parse.quote(txt)
    data = "query=" + encQuery

    url = "https://openapi.naver.com/v1/papago/detectLangs"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",papago_detect_id)
    request.add_header("X-Naver-Client-Secret",papago_detect_secret)
    res_ssl = ssl._create_unverified_context()
    response = urllib.request.urlopen(request, data=data.encode("utf-8"), context=res_ssl)
    
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        
        res = json.loads(response_body.decode('utf-8'))
        return(res['langCode'])

    else:
        print("Error Code:" + rescode)


def translate(txt, tp, nmt_id, nmt_pw):
    """번역"""
    if tp == "0":
        src = "en"
        tgt = "ko"
    elif tp == "1":
        src = "ko"
        tgt = "en"
    
    encText = urllib.parse.quote(txt)
    data = "source=" + src + "&target=" + tgt + "&text=" + encText
    
    url = "https://openapi.naver.com/v1/papago/n2mt"
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", nmt_id)
    request.add_header("X-Naver-Client-Secret", nmt_pw)
    res_ssl = ssl._create_unverified_context()
    response = urllib.request.urlopen(request, data=data.encode("utf-8"), context=res_ssl)
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        
        res = json.loads(response_body.decode('utf-8'))
        return(res['message']['result']['translatedText'])

    else:
        return("Error Code:" + rescode)


if __name__ == "__main__":
    txt = "안녕 July?"
    detect_language(txt)
