# 对数据进行简单的改变，当然这不是一个最优的方式
array = "abcd12345ed125ss123058789sdfdsf4435765768678" + " "

dic = {}
def longest_num_list(array):
    a = []
    for i in range(10):
        a.append(str(i))
    times = 0
    for i in range(len(array)):
        if array[i] not in a:
            if times != 0:
                dic[times] =i
            times = 0
            continue
        else:
            times = times + 1
    position = dic[max(dic.keys())]
    listLength = max(dic.keys())
    print(array[(position - listLength):position])

longest_num_list(array)
