import os
import sys
import urllib.request

papago_nmt_id = sys.argv[1]
papago_nmt_secret = sys.argv[2]
#papago_detect_id = sys.argv[3]
#papago_detect_secret = sys.argv[4]

'''
#언어 감지
def detect_language(txt):
    encQuery = urllib.parse.quote(txt)
    data = "query=" + encQuery

    url = "https://openapi.naver.com/v1/papago/detectLangs"

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
'''

#번역
def translate(txt):
    encText = urllib.parse.quote(txt)
    data = "source=en&target=ko&text=" + encText
    
    url = "https://openapi.naver.com/v1/papago/n2mt"
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",papago_nmt_id)
    request.add_header("X-Naver-Client-Secret",papago_nmt_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)


if __name__ == "__main__":
    txt = "HELLO! This is for ppt translation."
    #lang = detect_language(txt)
    translate(txt)
    #여기까지 호출량 35