import sys
sys.path.append('..')

from lib.queue import Queue


def hot_potato(name_list, num):
    # Finish the function
    q=Queue()
    for i in name_list:
        q.enqueue(i)
    while q.size()>1:
        for _ in range(num):
            tmp=q.dequeue()
            q.enqueue(tmp)
        q.dequeue()
    remaining_person=q.dequeue()

    return remaining_person

print(hot_potato(["Susan", "Brad", "Kent", "David"], 6))              # 回傳 "Brad"
print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))  # 回傳 "Susan"
