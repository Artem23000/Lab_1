def find_common_participants(group_1, group_2, separator=','):
    group_1_sep = group_1.split(separator)
    group_2_sep = group_2.split(separator)
    true_list = list(set(group_1_sep) & set(group_2_sep))
    return sorted(true_list)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_list = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(f"Общие участники: {common_list}")
