#1
def anagram_number(number):
    if f"{number}"==f"{number}"[::-1]:
        return True
    return False
anagram_number(121121)

#2
def roman_to_int(Str):
    b_list=list(Str)
    print(b_list)
    so=0
    i=0
    for i in range(len(b_list)):
        if i<len(b_list)-1:
            if b_list[i]=="I" and b_list[i+1]=="V":
                so=so+4-5
            elif b_list[i]=="I" and b_list[i+1]=="X":
                so=so+9-10
            elif b_list[i]=="X" and b_list[i+1]=="L":
                so=so+40-50
            elif b_list[i]=="X" and b_list[i+1]=="C":
                so=so+90-100
            elif b_list[i]=="C" and b_list[i+1]=="D":
                so=so+400-500
            elif b_list[i]=="C" and b_list[i+1]=="M":
                so=so+900-1000
            elif b_list[i]=="I":
                so=so+1
            elif b_list[i]=="V":
                so=so+5
            elif b_list[i]=="X":
                so=so+10
            elif b_list[i]=="L":
                so=so+50
            elif b_list[i]=="C":
                so=so+100
            elif b_list[i]=="D":
                so=so+500
            elif b_list[i]=="M":
                so=so+1000
        else:
            if b_list[i]=="I":
                so=so+1
            elif b_list[i]=="V":
                so=so+5
            elif b_list[i]=="X":
                so=so+10
            elif b_list[i]=="L":
                so=so+50
            elif b_list[i]=="C":
                so=so+100
            elif b_list[i]=="D":
                so=so+500
            elif b_list[i]=="M":
                so=so+1000
        i=i+1
    print(so)
roman_to_int("CMX")