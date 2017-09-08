s = input()
maxstr = ""
maxlen = 0
tmplen = 0
tmpstr = ""
for i in range(len(s)):
    if(s[i] >= '0' and s[i] <= '9'):
        tmplen += 1
        tmpstr += s[i]
    else:
        if(tmplen > maxlen):
            maxlen = tmplen
            maxstr = tmpstr
        tmplen = 0
        tmpstr = ""
if(tmplen > maxlen):
    maxlen = tmplen
    maxstr = tmpstr
print(maxstr)
print(maxlen)