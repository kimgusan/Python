# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트
# 전체 내용을 문자열로 가져오기: file.read()

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""
content = ''
with open('alice.txt', 'r', encoding='utf-8') as file:
    content += file.read().lower()

content = content.replace("\"", ' ').replace("\'",' ').replace("?",' ').replace("!",' ').replace(".",' ').replace(",",' ').replace(')',' ').replace("(", ' ')\
    .replace('\n',' ').replace('[', ' ').replace(']',' ').replace("`",' ').replace('-',' ').replace(';',' ')\
    .replace(':',' ').replace('_',' ').replace('\n\n',' ')

content = content.split(' ')
content_dict = {}


for i in range(len(content)):
    count = 0
    for j in content:
        if content[i] in j:
            count += 1
            content_dict[content[i]] = count

for word, count in content_dict.items():
    if count >= 100 and len(word) >= 2:
        content_dict[word] = count
        print(word, count)



