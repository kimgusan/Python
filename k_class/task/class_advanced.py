# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).


class Member:

    number = 0

    def __init__(self, id, password, name):
        self.id = id
        self.password = password
        self.name = name
        Member.number += 1

    @classmethod
    def get_member(cls, id, password, name):
        id = 'admin_' +id
        return cls(id, password, name)

member = Member.get_member("kimgusan", "123", "김규산")
print(member.id)
print(Member.number)









