origin_list = [300, 2, 12]
altered_list = [origin_list[i] for i in range(1, len(origin_list)) if origin_list[i] > origin_list[i - 1]]
print(altered_list)
