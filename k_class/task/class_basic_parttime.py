# PartTimer

# '모든 직원'에 공통적으로 적용되는 내용
# - 시급
# - 직원수

# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)

# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리

class PartTimer:
    pay_of_hour = 10000
    total_of_part_timers = 0

    def __init__(self, alias, address):
        self.alias = alias
        self.address = address
        self.total_money = 0
        PartTimer.total_of_part_timers += 1

    def calculate_money(self, work_time, **kwargs):
        '''
        :param work_time: 일한 시간
        :param kwargs: bonus = 상여금
        :return:
        '''
        if 'bonus' in kwargs:
            self.total_money = work_time * self.pay_of_hour + kwargs['bonus']
        else:
            self.total_money = work_time * self.pay_of_hour
        return self.total_money




