# 练习 1

"""
问题描述:
    有一个列表，其中包括 10 个元素，例如这个列表是[1,2,3,4,5,6,7,8,9,0],
要求将列表中的每个元素一次向前移动一个位置，第一个元素到列表的最后，然后输出这个列表。
最终样式是[2,3,4,5,6,7,8,9,0,1]
"""

raw_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(raw_list)

raw_first = raw_list.pop(0)
raw_list.append(raw_first)
print(raw_list)