class User:
    def __init__(self, **kwargs):
        '''
        :param kwargs: email = email, password =password, name = name
        '''
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.name = kwargs.get('name')

    def user_add(self):
        return self.email

    # 체크라는 함수 필요
