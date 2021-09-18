# 1
def day_diff(release_date, code_complete_day):
    import datetime
    day_time=datetime.datetime.strptime(release_date,"%d/%m/%Y")-datetime.datetime.strptime(code_complete_day,"%Y-%d-%m")
    return day_time
day_diff("19/12/2021","2020-12-10")


# 2
def alpha_num(sentence):
    kq=[]
    for k in a.split(" "):
        c=list(k)
        i=0
        j=len(c)-1
        while i<len(c):
            if c[i].isalpha()==True and c[j].isnumeric()==True:
                kq.append(k)
                break
            else:
                i+=1
                j-=1
    return kq
alpha_num("Emma25 is Data scientist50 and AI Expert")