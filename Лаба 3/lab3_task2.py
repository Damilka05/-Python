# TODO Напишите функцию find_common_participants
def find_common_participants(s1, s2, r = ','):
    ans = list(set(s1.split(r)).intersection(s2.split(r)))
    ans.sort()
    return ans

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, r = '|'))
