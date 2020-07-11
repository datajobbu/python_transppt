import os
import sys
import json
import urllib.request

papago_nmt_id = ""
papago_nmt_secret = ""

papago_detect_id = ""
papago_detect_secret = ""

#언어 확인
def detect_language(txt):
    encText = urllib.parse.quote(txt)
    data = "text=" + encText

    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",papago_detect_id)
    request.add_header("X-Naver-Client-Secret",papago_detect_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode("utf-8"))
    else:
        print("Error Code:" + rescode)