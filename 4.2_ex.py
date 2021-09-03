# source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result_list = []
# for i in range(1, len(source_list)):
#     if source_list[i] > source_list[i - 1]:
#         result_list.append(source_list[i])
# print(result_list)

source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [source_list[i] for i in range(1, len(source_list)) if source_list[i] > source_list[i - 1]]
print(result_list)
