# 무게만 측정하는 신호 ( Body Load Cell )
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0
b10 = 0
b11 = 0
b12 = 0
b_total = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]

# 인지 무게 ( Body Load Cell )
p1 = 6
p2 = 7
p3 = 22
p4 = 23
p5 = 4
p6 = 6
p7 = 22
p8 = 24
p_total = [p1, p2, p3, p4, p5, p6, p7, p8]

# 기본값 설정
plate = 10  #아크릴판 무게 10kg으로 가정

total= sum(b_total) + sum(p_total) - plate
print("총 무게: " , total)


# 기준치 설정
standard = total/5
print("기준치: " , standard)

# 인지 신호들 판별
results = []

for p in [p1, p2, p3, p4, p5, p6, p7, p8]:
    if p > standard:
        results.append(1)
    else:
        results.append(0)
print(results)


# 인지 신호 수
ch_total = sum(results)
print("인지 신호 수: " , ch_total)     #감지된 압력센서의 개수


##### 함수들 #####

# 작동 제한 x
def brake():    #acc 조정 -> 0:전원x
    damp = 0
    print("2인 이상 탑승 감지됨. 내리십시오")
    return damp

def detect_people(weight, sensors, num):   # 총무게, 감지된 센서 개수, 센서 ON/OFF 유무 배열
    if weight >= 110:
        passengers = 2
    else:
        if sensors >= 6:
            passengers = 2
        elif num[2]  == 1 & num[3]  == 1 & num[6]  == 1 & num[7] == 1:
            passengers = 2
        elif num[0]  == 1 & num[1]  == 1 & num[4]  == 1 & num[5] == 1:
            passengers = 2
        elif num[0]  == 1 & num[1]  == 1 & num[6]  == 1 & num[7] == 1:
            passengers = 2
        else:
            passengers = 1
    return passengers



person = detect_people(total, ch_total, results)
print("감지된 사람수: " , person)   #감지된 사람 수

if person == 2:
    brake()


# 기준치 설정 /4? 5?
# 더 다양한 경우의 수

# 해당 코드를 raspberrypi 적용