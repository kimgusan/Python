# https://ocr.space/OCRAPI
# myapi_key => K83584363188957
# https://api.ocr.space/parse/imageurl?apikey=&url=
# https://api.ocr.space/parse/imageurl?apikey=&url=&language=&isOverlayRequired=true
# 이미지 경로 : https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg
import requests

url = 'https://api.ocr.space/parse/imageurl?apikey=K83584363188957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true'
response = requests.get(url)
response.raise_for_status()

result = response.json()
print(type(result))
print(result['ParsedResults'][0]['ParsedText'])
