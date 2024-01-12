# 학교
# 이름, 지역, 학생 수, 선생님 수
# 학교 정보 출력 메소드

class School:

    def __init__(self, name, address, studnet_count=0, teacher_count=0):
        self.name = name
        self.address = address
        self.studnet_count = studnet_count
        self.teacher_count = teacher_count

    def school_info(self):
        return f'{self.name}, {self.address}, 학생 수: {self.studnet_count}, 선생님 수: {self.teacher_count}'
# 선생님
# 이름, 과목, 학교
# 선생님이 추가될 때마다 선생님 수 1증가
# 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가 >>>>> ???????
# 선생님 정보 출력 메소드

class Teacher:
    def __init__(self, name, major, school):
        self.name = name
        self.major = major
        self.school = school # 객체 참조
        self.school.teacher_count += 1

    def add_ability(self, student):
        self.student = student # 객체 참조

        if self.major == student.major:
            student.ability += 1


    def teacher_info(self):
        return f'{self.name}, {self.major}, {self.school.name}'

# 학생
# 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# 학생이 추가될 때마다, 학생 수 1증가
# 학생 정보 출력 메소드
class Student:
    def __init__(self,name, grade,major, school, teacher, ability=0):
        self.name = name
        self.grade = grade
        self.major = major
        self.school = school # 객체 참조
        self.teacher = teacher # 객체 참조
        self.ability = ability
        self.school.studnet_count += 1

    def student_info(self):
        return f'{self.name}, {self.grade}, {self.school.name}, 능력치: {self.ability}'

school = School('상갈초', '용인시')
teacher = Teacher('김규태', '수학', school)
student = Student('김규산','3학년','수학', school, teacher)
print(teacher.teacher_info())
print(student.student_info())
print(school.school_info())

teacher.add_ability(student)
print()

print(teacher.teacher_info())
print(student.student_info())
print(school.school_info())



