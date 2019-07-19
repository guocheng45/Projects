#-*- coding: utf-8 -*-
#面试题练习
list1 = "abcdedcba"
list_len = len(list1)
ranges = len(list1)/2
print "ranges:",ranges
i = 0
for i in range(ranges):
    print i
    if(list1[i] != list1[list_len-1-i]):
        print '不对称！'
        break
    elif(list1[i] == list1[list_len-1-i] and i == ranges-1):
        print "对称：","list1[i]",list1[i],"list1[list_len-1-i]",list1[list_len-1-i]
    elif(list1[i] == list1[list_len-1-i] and i < list_len-i-1):
        i = i + 1
    