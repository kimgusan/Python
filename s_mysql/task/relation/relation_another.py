import datetime

from crud_module import *
from field_trip import FieldTrip
from post import Post
from owner import Owner
from office import Office
from conference_room import ConferenceRoom
from part_time import PartTime
import hashlib


if __name__ == '__main__':
    pass

    # # 학부모 정보 추가
    # save_many_query = "insert into tbl_parent(name, age, gender, address, phone) \
    #                    values(%s, %s, %s, %s, %s)"
    # save_many_params = (
    #     ('한동석', 20, '남자', '경기도 남양주', '01012341234'),
    #     ('홍길동', 30, '여자', '서울시 강남구', '01033333333'),
    #     ('이순신', 40, '선택안함', '경기도 남양주', '01055555555')
    # )
    # save_many(save_many_query, save_many_params)
    #
    # # 아이 추가
    # find_by_id_query = "select id, name, age, gender, address, phone from tbl_parent where id = %s"
    # find_by_id_params = 1,
    # find_by_id_params = 3,
    # find_by_id_params = 2,
    # parent = find_by_id(find_by_id_query, find_by_id_params)
    # parent_id = parent.get("id")
    #
    # save_many_query = "insert into tbl_child(name, age, gender, parent_id) \
    #               values(%s, %s, %s, %s)"
    # save_many_params = (
    #     ('둘리', 4, '남자', parent_id),
    #     ('또치', 9, '여자', parent_id),
    # )
    # save_many_params = (
    #     ('도너', 4, '남자', parent_id),
    # )
    # save_many_params = (
    #     ('마이콜', 11, '선택안함', parent_id),
    # )
    # save_many(save_many_query, save_many_params)
    #
    # # 체험학습 추가
    # save_many_query = "insert into tbl_field_trip (title, content, count) \
    #                    values(%s, %s, %s)"
    # save_many_params = (
    #     ('테스트 제목1', '테스트 내용1', 10),
    #     ('테스트 제목2', '테스트 내용2', 50),
    #     ('테스트 제목3', '테스트 내용3', 40),
    #     ('테스트 제목4', '테스트 내용4', 100)
    # )
    # save_many(save_many_query, save_many_params)
    #
    # # 첨부파일 추가
    # save_query = "insert into tbl_file(file_path, file_name) \
    #               values(%s, %s)"
    # save_params = ('2024/01/18', 'img002.png')
    # save(save_query, save_params)
    #
    # find_all_query = "select id from tbl_file order by id desc"
    # file_id = find_all(find_all_query)[0].get("id")
    #
    # find_all_query = "select id from tbl_field_trip order by id desc"
    # field_trip_id = find_all(find_all_query)[0].get("id")
    #
    # save_query = "insert into tbl_field_trip_file(id, field_trip_id) \
    #               values (%s, %s)"
    # save_params = file_id, field_trip_id
    #
    # save(save_query, save_params)
    #
    # # 체험학습 상세보기
    # find_by_id_query = "select id, title, content, count \
    #                     from tbl_field_trip \
    #                     where id = %s"
    # find_by_id_params = 4,
    # field_trip = find_by_id(find_by_id_query, find_by_id_params)
    #
    # find_all_by_query = "select f.id, f.file_path, f.file_name \
    #                     from tbl_file f join tbl_field_trip_file ft \
    #                     on ft.field_trip_id = %s and f.id = ft.id"
    #
    # files = find_all_by(find_all_by_query, find_by_id_params)
    #
    # field_trip = FieldTrip(field_trip.get("id"), field_trip.get("title"), field_trip.get("content"), field_trip.get("count"), *files)
    # print(field_trip.__dict__)
    # print(field_trip.get_full_path())

# 회원가입
## save_query = "insert into tbl_user(user_id, password, name, address) \
##               values(%s, hex(aes_encrypt(%s, 'hello mysql')), %s, %s)"
# save_query = "insert into tbl_user(user_id, password, name, address) \
#               values(%s, %s, %s, %s)"
# password = hashlib.sha256()
# password.update('5555'.encode('utf-8'))
# password = password.hexdigest()
#
# save_params = 'hgd9999', password, '홍길동', '서울시 강남구'
# save(save_query, save_params)

# 게시글 작성
# find_by_id_query = "select id from tbl_user where id = %s"
# find_by_params = 1,
# user = find_by_id(find_by_id_query,find_by_params)
#
# save_query = "insert into tbl_post (title, content, user_id) \
#               values (%s, %s, %s)"
# save_params = '테스트 제목1', '테스트 내용1', user.get("id")
# save(save_query,save_params)

# 게시글 목록
# find_all_query = "select p.id, title, content, create_date, u.name \
#                   from tbl_user u join tbl_post p\
#                   on u.id = p.user_id\
#                   order by id desc"
# posts = find_all(find_all_query)
# for post in posts:
#     print(post)

# 게시글 상세보기
# find_by_id_query = "select id from tbl_post where id = %s"
# find_by_id_params = 1,
# post = find_by_id(find_by_id_query, find_by_id_params)
# post_id = post.get("id")
#
# find_by_id_query = "select p.id, title, content, create_date, u.name \
#                     from tbl_user u join tbl_post p \
#                     on u.id = p.user_id\
#                     where p.id = %s"
# find_by_id_params = post_id,
# post = find_by_id(find_by_id_query, find_by_id_params)

# 댓글 목록
# find_all_by_query = "select r.id, name, content\
#                from tbl_user u join tbl_reply r \
#                on r.post_id = %s and u.id = r.user_id"
#
# find_all_by_params = post.get("id"),
# replies = find_all_by(find_all_by_query, find_all_by_params)
#
# post = Post(post.get("id"), post.get("title"), post.get("content"), post.get("create_date"), post.get("name"), replies)
# print(post.__dict__)

# 댓글 작성
# find_by_id_query = "select id from tbl_user where id = %s"
# find_by_id_params = 2,
# user = find_by_id(find_by_id_query, find_by_id_params)
# user_id = user.get("id")
#
# find_by_id_query = "select id from tbl_post where id = %s"
# find_by_id_params = 1,
# post = find_by_id(find_by_id_query, find_by_id_params)
# post_id = post.get("id")
#
# save_many_query = "insert into tbl_reply (content, user_id, post_id) \
#                    values (%s, %s, %s)"
# save_many_params = (
#     ('댓글 테스트1', user_id, post_id),
#     ('댓글 테스트2', user_id, post_id),
# )
# save_many(save_many_query, save_many_params)

# 보호자 추가
#     save_query = 'insert into tbl_owner(name, age, phone, address) values (%s, %s, %s, %s)'
#     save_params = ('아버지', 50, '01034320132', '경기도 용인시')
#     save_params = ('어머니', 30, '01034322232', '부산광역시 사상구')
#     # save(save_query, save_params)
#
# # 반려동물 추가
#     find_by_id_query = "select id from tbl_owner where id = %s"
#     find_by_id_params = 1,
#     owner_id = find_by_id(find_by_id_query, find_by_id_params)
#
#     save_query = 'insert into tbl_pet(name, ill_name, weight, owner_id) values (%s, %s, %s, %s)'
#
#     save_many_params =(
#         ('햇살', '암', 2.5, owner_id.get('id')),
#         ('희망', '대장염', 4.5, owner_id.get('id'))
#     )
#     # save_many(save_query, save_many_params)
#
# # 전체 목록(보호자랑 각 반려동물)
#     find_all_query = "select p.*,o.* from tbl_pet p join tbl_owner o\
#                       on p.owner_id = o.id"
#     for i in find_all(find_all_query):
#         print(i)
#
#
#     find_all_query = 'select id, name, age, phone, address from tbl_owner'
#     owners = find_all(find_all_query)
#
#     owners_with_pets = []
#     for owner in owners:
#         find_all_by_query = 'select id, name, ill_name, age, weight,owner_id from tbl_pet where owner_id = %s'
#         find_all_by_params = owner.get('id')
#         pets = find_all_by(find_all_by_query, find_all_query)
#         owners_with_pets.append(Owner(owner.get('id'), owner.get('name'), owner.get('age'), owner.get('phone'), owner.get('address'), pets))
#         for pet in pets:
#             print(pet)



#회원 가입(패스워드 암호화 할 것)
message = "이메일: "
client_email = input(message)
find_by_id_email_query = 'select email from tbl_client where email = %s'
find_by_id_email_params = client_email,
email_check_result = find_by_id(find_by_id_email_query, find_by_id_email_params)

if not email_check_result:
    message = '사용자 이름: '
    client_name = input(message)
    message = '사용 비밀번호: '
    pwd = input(message)

    save_user_query = 'insert into tbl_client (email, password, name) \
                       values (%s, %s ,%s)'
    password = hashlib.sha256()
    password.update(pwd.encode('utf-8'))
    password = password.hexdigest()
    save_user_params = client_email, password, client_name
    save(save_user_query, save_user_params)

# 회사 추가
    message = '회사를 등록 하시겠습니까?\n' + 'Y/n\n'
    choice_office = input(message)
    if choice_office == 'Y':
        message = '회사 이름: '
        office_name = input(message)
        message = '회사 지역: '
        office_address = input(message)

        save_office_query = 'insert into tbl_office (name, location) \
                             values (%s ,%s)'
        save_office_params = (office_name, office_address)
        save(save_office_query, save_office_params)


else:
    print('이미 등록된 이메일 입니다.')

# 회의실 추가

message = '어느 회사에 회의실을 추가 하시겠습니까?'
office_name = input(message)

find_by_id_query = 'select id from tbl_office where name = %s'
find_by_id_params = office_name
office_dict = find_by_id(find_by_id_query,find_by_id_params)

if office_dict is not None:
    save_conference_room_query = 'insert into tbl_conference_room (office_id) \
                                  values (%s)'
    save_conference_params = office_dict.get('id')
    save(save_conference_room_query, save_conference_params)

# # 회의실 추가 시 회의실마다 이용시간 시간 추가 => 실제로는 회사를 선택해서 사용 가능한 회의실 번호를 뿌려줘야 할 것 같음
# # 아래쪽에 회의실 사용 가능 시간 추가 항목을 따로 만들어서 사용해야 할 것 같음
#
    find_by_id_conference_room_query = 'select id from tbl_conference_room order by 1 desc'
    conference_room_dict = find_by_id(find_by_id_conference_room_query, None)

    message = '신규 회의실 예약 가능 시간 등록이 필요합니다\n' + '회의실 이용 가능 시간을 작성해주세요\n' + \
              'ex) 12:00:00 or HH24MISS\n'
    part_time = input(message) # 질문: 여기서 형식에 앉맞는 경우 에러로 뺄수 있나? (1292, "Incorrect time value: '1234**' for column 'time' at row 1")
    save_part_time_query = 'insert into tbl_part_time (time, conference_room_id) values (%s, %s)'
    save_part_time_params = (part_time, conference_room_dict.get('id'))
    save(save_part_time_query, save_part_time_params)

else:
    print('회사가 없습니다')

# # 날짜를 문자열로
# # 1. datetime.datetime.isoformat()
# # 2. datetime.date.isoformat()
# # 회의실 예약 가능 시간 추가(회사 등록 없이 나중에 예약할 때 사용하는 부분)

message1 = "회의실 예약 시스템 입니다." + "이메일과 회사명을 입력해 주세요\n" + "이메일: "
client_email = input(message1)
find_by_id_email_query = 'select email from tbl_client where email = %s'
find_by_id_email_params = client_email,
email_check_result = find_by_id(find_by_id_email_query, find_by_id_email_params)

if email_check_result is not None:
    message2 = '어느 회사에 회의실을 추가 하시겠습니까?'
    office_name = input(message2)
    find_all_by_conference_room_query = 'select * from tbl_conference_room c join tbl_office o \
                                         on c.office_id = o.id and o.name = %s \
                                         join tbl_part_time p \
                                         on o.id = p.conference_room_id'
    find_all_by_conference_room_params = office_name
    office_dict = find_all_by(find_all_by_conference_room_query,find_all_by_conference_room_params)
    # print(office_dict)
    # 시간이 객체 형태로 나오는 부분이 있어서 시간 중복값을 걸러내는 방법을 모르겠음
    conference_room_dict = find_by_id(find_all_by_conference_room_query,find_all_by_conference_room_params)


    if conference_room_dict is not None:
        message = "예약 하고 싶은 시간을 정하세요: " + "ex) 12:00:00\n"
        time = input(message)
        save_reservation_query = 'insert into tbl_reservation (time, client_email, conference_room_id) \
                                  values (%s,%s, %s)'
        save_reservation_params = (time, email_check_result.get('email'), conference_room_dict.get('conference_room_id'))
        save(save_reservation_query, save_reservation_params)
    else:
        print('회사가 없습니다')
else:
    print('이메일이 없습니다')

    # 회의실 전체 내용 조회(예약이 이미 완료된 회의실 시간은 보여지지 않는다.)
    find_all_query = 'select id, office_id from tbl_conference_room \
                      where id not in (select b.conference_room_id from tbl_conference_room a join tbl_reservation b \
                      group by b.id)'
    result = find_all(find_all_query)
    for i in result:
        print(i)