import datetime
# print(d.isocalendar().week)



def cal_weekday(d_str):
    m,d,y = [int(i) for i in d_str.split('/')]
    dt = datetime.date(y,m,d)
    return str((dt.isocalendar().week))


def seconds(t_str):
    h,m,s = t_str.split(':')
    return str((int(h)* 3600 + int(m)*60 + int(s)))


print(cal_weekday('09/26/2022'))