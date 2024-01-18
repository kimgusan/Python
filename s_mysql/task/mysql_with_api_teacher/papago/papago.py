# 파파고 url
# https://openapi.naver.com/v1/papago/n2mt
# client_id => gHq247_MTSLVsgRUfvs8
# client_secret => cv52dDBP5P
import urllib.request
import json

def papago(kor_message):
    client_id = "gHq247_MTSLVsgRUfvs8"
    client_secret = "cv52dDBP5P"
    encoding_text = urllib.parse.quote(kor_message)
    data = f"source=ko&target=en&text={encoding_text}"
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)

    # -H
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response = json.loads(response.read().decode("utf-8"))
        # print(response['message']['result']['translatedText'])
        return response['message']['result']['translatedText']