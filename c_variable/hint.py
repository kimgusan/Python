from typing import List, Dict, Set, Tuple, Union, Final


data:Final[int] = 10
print(data)

class A:
    pass

class B:
    @staticmethod
    def test(data: Union[int,str], number: int | float, data1: A, datas: list[int], data_dict: dict[str,int]) -> int:
        return 10