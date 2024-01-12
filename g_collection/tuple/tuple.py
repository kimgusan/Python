# mutable: 변할 수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10
print(data_list2)

# immutable: 변할 수 없는
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1
# data_tuple2[0] = 10
data_tuple2 = data_tuple1 + (5, 6)
print(data_tuple2)
print(data_tuple1)

datas = 1, 2
print(datas, type(datas))
print(datas[0])

ERROR_CODE = 1,
print(ERROR_CODE[0], type(ERROR_CODE))



