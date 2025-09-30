# (2025-09-24-11:15, 2025-09-24-15:15)
# 2025-09-24-11:15
#

def compare_meetings(meet1, meet2):
    start_meet1, end_meet1 = meet1
    start_meet2, end_meet2 = meet2

    if end_meet2 <= start_meet1 or end_meet1 <= start_meet2:
        return False
    
    return True

# result = compare_meetings((2, 4), (1, 2))
# print(result)

def find_count_compare_meetings(meetings):
    result = {}
    for i, meet in enumerate(meetings): # meet - встреча которую мы со всеми дальше сравниваем
        for j in range(i+1, len(meetings)):
            meet2 = meetings[j]
            is_overlap = compare_meetings(meet, meet2)
            if is_overlap:
                if not i in result:
                    result[i] = None
                if not j in result:
                    result[j] = None

    return len(result)

result = find_count_compare_meetings(((2, 4), (1, 2), (1, 5), (99, 100), (10, 15), (11, 12)))
print(result)