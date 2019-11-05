

def output1(eight_hours_sleep,headache,depression,stress_personal_life_work_life):
    if(eight_hours_sleep==2 and headache<=2 and depression<=2 and stress_personal_life_work_life<=2):
        return ('Mental illness')
    else :
       return ('ok')


def output2(hours_sit,sit_straight,cushioned_chair_to_sit,sit_in_front_of_computer):
    if(hours_sit<=3 and sit_straight==2 and cushioned_chair_to_sit==2 and sit_in_front_of_computer<=3):
        return ('Back Pain')
    else :
        return ('ok')

def output3(headache,drinking_alchohol):
    if(drinking_alchohol<=2 and headache==1):
        return ('Stroke')
    else :
        return ('ok')

def output4(smoking,junk_food,stress_personal_life_work_life):
    if(smoking<=2 and junk_food<=2 and stress_personal_life_work_life==1):
        return ('atherosclerosis')
    else :
        return ('ok')

def output5(hours_walk_in_a_day,walk_to_workplace,exercise,junk_food):
    if(hours_walk_in_a_day==1 and walk_to_workplace==1 and exercise==1 and junk_food<=2):
        return ('Obesity')
    else :
        return ('ok')

def output6(smoking,drinking_alchohol,junk_food,stress_personal_life_work_life):
    if(smoking<=2 and drinking_alchohol <=2 and junk_food<=2 and stress_personal_life_work_life==1):
        return ('Heart Disease')
    else :
        return ('ok')

def output7(hours_walk_in_a_day,junk_food,exercise,stress_personal_life_work_life):
    if(hours_walk_in_a_day==1 and junk_food<=2 and exercise==1 and stress_personal_life_work_life<=2):
        return ('High Blood Pressure')
    else :
        return ('ok')


def output9(sit_in_traffic_jam):
    if(sit_in_traffic_jam==1):
        return ('Asthma')
    else :
        return ('ok')

def output10(exercise,junk_food,sit_in_traffic_jam):
    if(exercise==1 and junk_food<=2 and sit_in_traffic_jam==1):
        return ('Chronic obstructive pulmonary disease,')
    else :
        return ('ok')


def output11(eight_hours_sleep,junk_food,exercise,smoking):
    if(eight_hours_sleep==2 and junk_food<=2 and exercise==1 and smoking<=2):
        return ('Metabolic syndrome')
    else :
        return ('ok')

def output12(headache,tiredness):
    if(headache<=2 and tiredness<=2):
        return ('Chronic renal failure ')
    else :
        return ('ok')


def output13(smoking,drinking_alchohol,hours_sit,sit_straight,cushioned_chair_to_sit):
    if(smoking<=2 and drinking_alchohol<=2 and hours_sit<=2 and sit_straight==2 and cushioned_chair_to_sit==2):
        return ('Osteoporosis')
    else :
        return ('ok')


def output14(hours_spend_on_social_media,use_headphones_or_earphones_constantly):
    if(hours_spend_on_social_media<=2 and use_headphones_or_earphones_constantly<=2):
        return ('Swimmer’s ear')
    else :
        return ('ok')


def output15(smoking,junk_food):
    if(smoking<=2 and junk_food<=2 ):
        return ('Nephritis')
    else :
        return ('ok')


def output16(eight_hours_sleep,hours_spend_on_social_media,sit_in_front_of_computer):
    if(eight_hours_sleep==2 and	hours_spend_on_social_media<=2 and sit_in_front_of_computer<=2):
        return ('Eye Pain')
    else :
        return ('ok')
    
def output17(junk_food,exercise,stress_personal_life_work_life,hours_walk_in_a_day):
    if(junk_food<=2 and exercise==1 and stress_personal_life_work_life<=2 and hours_walk_in_a_day==1):
        return ('Type-II Diabetes')
    else :
        return ('ok')

def outmain(data):
    detected_diseases=[]

    hours_walk_in_a_day=data[0]
    walk_to_workplace=data[1] 
    smoking=data[2]
    drinking_alchohol=data[3]
    hours_sit=data[4]
    sit_straight=data[5] 
    cushioned_chair_to_sit=data[6] 
    sit_in_front_of_computer= data[7]
    walk_after_lunch_dinner=data[8]
    exercise=data[11]
    junk_food=data[14]
    eight_hours_sleep=data[10] 
    hours_spend_on_social_media=data[15]
    stress_personal_life_work_life=data[16]
    sit_in_traffic_jam=data[17]
    use_headphones_or_earphones_constantly=data[18]
    headache=data[20]
    depression=data[21]
    tiredness=data[22]

    o1=output1(eight_hours_sleep,headache,depression,stress_personal_life_work_life)
    o2=output2(hours_sit,sit_straight,cushioned_chair_to_sit,sit_in_front_of_computer)
    o3=output3(headache,drinking_alchohol)
    o4=output4(smoking,junk_food,stress_personal_life_work_life)
    o5=output5(hours_walk_in_a_day,walk_to_workplace,exercise,junk_food)
    o6=output6(smoking,drinking_alchohol,junk_food,stress_personal_life_work_life)
    o7=output7(hours_walk_in_a_day,junk_food,exercise,stress_personal_life_work_life)
    o9=output9(sit_in_traffic_jam)
    o10=output10(exercise,junk_food,sit_in_traffic_jam)
    o11=output11(eight_hours_sleep,junk_food,exercise,smoking)
    o12=output12(headache,tiredness)
    o13=output13(smoking,	drinking_alchohol,	hours_sit,	sit_straight,	cushioned_chair_to_sit)
    o14=output14(hours_spend_on_social_media,use_headphones_or_earphones_constantly)
    o15=output15(smoking,junk_food)
    o16=output16(eight_hours_sleep,hours_spend_on_social_media,sit_in_front_of_computer)
    o17=output17(junk_food,exercise,stress_personal_life_work_life,hours_walk_in_a_day)

    if(o1!="ok"):
        detected_diseases.append(o1)
    if(o2!="ok"):
        detected_diseases.append(o2)
    if(o3!="ok"):
        detected_diseases.append(o3)
    if(o4!="ok"):
        detected_diseases.append(o4)
    if(o5!="ok"):
        detected_diseases.append(o5)
    if(o6!="ok"):
        detected_diseases.append(o6)
    if(o7!="ok"):
        detected_diseases.append(o7)
    if(o9!="ok"):
        detected_diseases.append(o9)
    if(o10!="ok"):
        detected_diseases.append(o10)
    if(o11!="ok"):
        detected_diseases.append(o11)
    if(o12!="ok"):
        detected_diseases.append(o12)
    if(o13!="ok"):
        detected_diseases.append(o13)
    if(o14!="ok"):
        detected_diseases.append(o14)
    if(o15!="ok"):
        detected_diseases.append(o15)
    if(o16!="ok"):
        detected_diseases.append(o16)
    if(o17!="ok"):
        detected_diseases.append(o17)
    
    print(detected_diseases)
    
    return detected_diseases