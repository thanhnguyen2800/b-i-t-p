import math
xA= float(input("nhập vào tọa độ xA: "))
yA= float(input("nhập vào tọa độ yA: "))
xB= float(input("nhập vào tọa độ xB: "))
yB= float(input("nhập vào tọa độ yB: "))
xC= float(input("nhập vào tọa độ xC: "))
yC= float(input("nhập vào tọa độ yC: "))

ab= math.sqrt((xB-xA)**2+(yB-yA)**2)
bc= math.sqrt((xC-xB)**2+(yC-yB)**2)
ac= math.sqrt((xC-xA)**2+(yC-yA)**2)

if (ab+bc>ac) and (ab+ac>bc) and (bc+ac>ab):
    #tính chu vi
    cv= ab+ac+bc
    print("chu vi là: ", cv)
    #tính diện tích
    p=cv/2
    s=math.sqrt(p*(p-ab)*(p-bc)*(p-ac))
    print("diện tích là: ", s)
else:
    print("không tạo thành tam giác")
    
    


