import random
import time
import tkinter as tk
start=time.time()
listyfit=[[],[],[],[],[],[],[],[],[]]
listyabc=['a','b','c','d','e','f','g','h','i']
listylen=[[],[],[],[],[],[],[],[],[]]

subject_batch_dict={'Lab Algorithm':['bdais','cc','cse'], 'Java':['javacse'], 'Lab Calculus':['math'], 'CCT':['bdais','cc','cse'], 'Lab Cy. Sec.':['cybergroup'], 'Lab Java':['javacse'], 'Bus. Int.':['bda'], 'Calculus':['math'], 'App. Sec.':['ccis'], 'IOT':['iotgroup'], 'Lab Soft. Eng.':['bdais','cc','cse'], 'Algorithm':['cseis','bdacc'], 'Cy. Sec.':['cybergroup'], 'Sass':['sassgroup'], 'Intelligent Machine':['all'], 'Lab IOT':['iotgroup'], 'Lab Sass':['sassgroup'], 'Soft. Eng.':['cseis','bdacc'], 'Cinema':['cine'], 'Adv. Ep.':['ep'], 'Lab Bus. Int.':['bda'], 'Lab App. Sec.':['ccis'], 'TOC':['cse']}

def subjectlistnew(total_subject_list):
    global subject_batch_dict
    one=[]
    two=[]
    three=[]
    four=[]
    five=[]
    for i in total_subject_list:
        batch=len(subject_batch_dict[i])
        if batch==1:
            one.append(i)
        elif batch==2:
            two.append(i)
        elif batch==3:
            three.append(i)
        elif batch==4:
            four.append(i)
        else:
            five.append(i)
    one.sort()
    two.sort()
    three.sort()
    four.sort()
    five.sort()
    main_subject=one
    for j in two:
        main_subject.append(j)
    for j in three:
        main_subject.append(j)
    for j in four:
        main_subject.append(j)
    for j in five:
        main_subject.append(j)
    return main_subject



#*************************************************************************************************************
#population creation
#fitness 9
total_timeslot_list=list(range(1,36)) 
total_subject_list=['Lab Algorithm', 'Lab Calculus', 'CCT', 'Lab Cy. Sec.', 'Lab Java', 'Bus. Int.', 'Calculus', 'App. Sec.', 'IOT', 'Lab Soft. Eng.', 'Algorithm', 'Cy. Sec.', 'Sass', 'Intelligent Machine', 'Lab IOT', 'Lab Sass', 'Soft. Eng.', 'Cinema', 'Adv. Ep.', 'Lab Bus. Int.', 'Lab App. Sec.', 'TOC']
total_subject_list=subjectlistnew(total_subject_list)
total_teacher_list=['Jaya Gupta', 'Kavita Chaudhary', 'Poonam Vyas', 'Sonal Jain', 'Gireesh Kaushik', 'Pratishtha Ghosh', 'Devika Kataria', 'Abhishek Vyas', 'Devendra Bhavsar', 'Amit Mishra', 'Sheetal Mundra', 'S Taruna', 'Alok Kumar']
total_batch_list=['ep', 'cine', 'cc', 'javacse', 'all', 'cseis', 'iotgroup', 'bdais', 'bda', 'bdacc', 'cse', 'ccis', 'cybergroup', 'sassgroup', 'math']
#**************************************************************************************************************
#for calculating day
day_timeslot_dict={'mon':[1,2,3,4,5,6,7],'tue':[8,9,10,11,12,13,14],'wed':[15,16,17,18,19,20,21],'thu':[22,23,24,25,26,27,28],'fri':[29,30,31,32,33,34,35]}
#**************************************************************************************************************
#for checking it is lab  or not
subject_lab_credithour_dict={'Lab App. Sec.':2,'Lab Soft. Eng.':2,'Lab Algorithm':2,'Lab Bus. Int.':2,'Lab Java':2,'Lab Cy. Sec.':2,'Lab Calculus':2,'Lab IOT':2,'Lab Sass':4}
#**************************************************************************************************************
#for getting sub-batches
batch_dict={'cse':['epcse','cinecse','cybercse','iotcse','javacse','sasscse'],'bda':['epbda','cinebda','cyberbda','iotbda','sassbda','mathbda'],'cc':['epcc','cinecc','iotcc','sasscc','mathcc'],'is':['epis','cineis','iotis','sassis','mathis'],'cseis':['epcse','cinecse','cybercse','iotcse','javacse','sasscse','epis','cineis','iotis','sassis','mathis'],'bdacc':['epbda','cinebda','cyberbda','iotbda','sassbda','mathbda','epcc','cinecc','iotcc','sasscc','mathcc'],'ibm':['epbda','cinebda','cyberbda','iotbda','sassbda','mathbda','epcc','cinecc','iotcc','sasscc','mathcc','epis','cineis','iotis','sassis','mathis'],'all':['epbda','cinebda','cyberbda','iotbda','sassbda','mathbda','epcc','cinecc','iotcc','sasscc','mathcc','epis','cineis','iotis','sassis','mathis','epcse','cinecse','cybercse','iotcse','javacse','sasscse'],'bdais':['epbda','cinebda','cyberbda','iotbda','sassbda','mathbda','epis','cineis','iotis','sassis','mathis'],'ccis':['epis','cineis','iotis','sassis','mathis','epcc','cinecc','iotcc','sasscc','mathcc'],'ep':['epcse','epbda','epis','epcc'],'cine':['cinecse','cinebda','cinecc','cineis'],'iotgroup':['iotcse','iotbda','iotcc','iotis'],'sassgroup':['sasscse','sassbda','sasscc','sassis'],'math':['mathbda','mathcc','mathis'],'cybergroup':['cybercse','cyberbda'],'javacse':['javacse']}
#**************************************************************************************************************
#fitness 2
subject_teacher_dict={'Intelligent Machine':['Sonal Jain'],'TOC':['Amit Mishra'],'CCT':['Pratishtha Ghosh'],'App. Sec.':['Abhishek Vyas'],'Lab App. Sec.':['Abhishek Vyas'],'Lab Cy. Sec.':['Abhishek Vyas'],'Cy. Sec.':['Abhishek Vyas'],'Lab Algorithm':['S Taruna','Devendra Bhavsar'],'Algorithm':['S Taruna'],'Soft. Eng.':['Gireesh Kaushik'],'Lab Soft. Eng.':['Gireesh Kaushik'],'Bus. Int.':['Devendra Bhavsar'],'Lab Bus. Int.':['Devendra Bhavsar'],'Adv. Ep.':['Sheetal Mundra'],'Calculus':['Jaya Gupta'],'Lab Calculus':['Jaya Gupta'],'Java':['Kavita Chaudhary'],'Lab Java':['Kavita Chaudhary'],'Cinema':['Poonam Vyas'],'IOT':['Devika Kataria'],'Lab IOT':['Devika Kataria'],'Sass':['Alok Kumar'],'Lab Sass':['Alok Kumar']}
#**************************************************************************************************************
#fitness 3
teacher_batch_dict={'Sonal Jain':['all'],'Amit Mishra':['cse'],'Pratishtha Ghosh':['bdais','cc','cse'],'Abhishek Vyas':['ccis','cybergroup'],'S Taruna':['cseis','bdacc','bdais','cse'],'Gireesh Kaushik':['cseis','bdacc','cc','cse','bdais'],'Devendra Bhavsar':['bda','cc'],'Sheetal Mundra':['ep'],'Jaya Gupta':['math'],'Kavita Chaudhary':['javacse'],'Poonam Vyas':['cine'],'Devika Kataria':['iotgroup'],'Alok Kumar':['sassgroup']}
#**************************************************************************************************************
#fitness 4
subject_batch_dict={'Lab Algorithm':['bdais','cc','cse'], 'Java':['javacse'], 'Lab Calculus':['math'], 'CCT':['bdais','cc','cse'], 'Lab Cy. Sec.':['cybergroup'], 'Lab Java':['javacse'], 'Bus. Int.':['bda'], 'Calculus':['math'], 'App. Sec.':['ccis'], 'IOT':['iotgroup'], 'Lab Soft. Eng.':['bdais','cc','cse'], 'Algorithm':['cseis','bdacc'], 'Cy. Sec.':['cybergroup'], 'Sass':['sassgroup'], 'Intelligent Machine':['all'], 'Lab IOT':['iotgroup'], 'Lab Sass':['sassgroup'], 'Soft. Eng.':['cseis','bdacc'], 'Cinema':['cine'], 'Adv. Ep.':['ep'], 'Lab Bus. Int.':['bda'], 'Lab App. Sec.':['ccis'], 'TOC':['cse']}
#**************************************************************************************************************
#load calculation
subject_credithour_dict={'Intelligent Machine':2,'CCT':2,'TOC':3,'App. Sec.':3,'Lab App. Sec.':2,'Algorithm':3,'Soft. Eng.':3, 'Lab Soft. Eng.':2,'Lab Algorithm':2,'Bus. Int.':3,'Lab Bus. Int.':2,'Adv. Ep.':3,'Cy. Sec.':3,'Calculus':3,'Java':2,'Lab Java':2,'Lab Cy. Sec.':2,'Lab Calculus':2,'Cinema':3,'IOT':3,'Lab IOT':2,'Sass':1,'Lab Sass':4}
#***************************************************************************************************************
#fitness 9
invalid_lab_timeslot_list=[4,7,11,14,18,21,25,28,32,35]
#***************************************************************************************************************
# fitness 1
#independent
timeslot_batch_subject_teacher_list=[]         
teacher_timeslot_dict={}
timeslot_batch_dict={}
day_batch_subject_ddlist={}
batch_subject_load_dddict={}
time_batch_teacher_ddlist={}
teacher_time_subject_ddlist={}
batch_time_subject_ddlist={}




def ddloadmaker(dicty,fd,sd,td):
    if fd in list(dicty.keys()):
        if sd in list(dicty[fd].keys()):
            dicty[fd][sd]+=td
        else:
            dicty[fd][sd]=td
    else:
        dicty[fd]={sd:td}
    return dicty

def ddlistmaker(ddlist,fd,sd,td):
    if fd in ddlist.keys():
        if sd in ddlist[fd].keys():
            try:
                ddlist[fd][sd].append(td)
            except KeyError:
                ddlist[fd][sd]=[td]
        else:
            ddlist[fd][sd]=[td]
    else:
        ddlist[fd]={sd:[td]}
    return ddlist
            
        
    

def dlistmaker(dicty,fd,sd):
    if fd in list(dicty.keys()):
        dicty[fd].append(sd)
    else:
        dicty[fd]=[sd]
    return dicty
        

def singlelistinlist(first,second):
    list1=batch_dict[first]
    for i in list1:
        for j in second:
            if i in batch_dict[j]:
                return True
    return False


def cgen():
    chrome=[]
    t=random.choice(total_timeslot_list)
    chrome.append(t)
    b=random.choice(total_batch_list)
    chrome.append(b)
    s=random.choice(total_subject_list)
    chrome.append(s)
    te=random.choice(total_teacher_list)
    chrome.append(te)
    return chrome

def crossover(chrome1,chrome2):
    subject1=chrome1[2]
    subject2=chrome2[2]
    teacher1=chrome1[3]
    teacher2=chrome2[3]
    chrome1[2]=subject2
    chrome2[2]=subject1
    chrome1[3]=teacher2
    chrome2[3]=teacher1
    return chrome1, chrome2

def mutate(chrome,vales):
    '''if vales=='done':
        chrome=cgen()
        return chrome
    elif vales=='tea':
        r=random.choice(subject_teacher_dict[chrome[2]])
        chrome[3]=r
        return chrome
    elif vales=='bat':
        r=random.choice(teacher_batch_dict[chrome[3]])
        chrome[1]=r
        return chrome
    else:
        listy=[0,1,2,3]
        while(True):
            a=random.choice(listy)
            if a==0:
                try:
                    taken_timeslot=teacher_timeslot_dict[chrome[3]]
                    remaining_timeslot=list(set(total_timeslot_list)-set(taken_timeslot))
                    r=random.choice(remaining_timeslot)
                    chrome[a]=r
                    break
                except KeyError:
                    r=random.choice(total_timeslot_list)
                    chrome[a]=r
                    break
            if a==1:
                r=random.choice(teacher_batch_dict[chrome[3]])
                chrome[a]=r
                break
            if a==2:
                change=''
                for key, val in subject_teacher_dict.items():
                    if val==chrome[3]:
                        change=key
                        r=change
                        chrome[a]=r
                        break            
            if a==3:
                r=random.choice(subject_teacher_dict[chrome[2]])
                chrome[a]=r
                break
    return chrome'''
    listy=[0,1,2,3]
    while(True):
        a=random.choice(listy)
        if a==0:
            r=random.choice(total_timeslot_list)
            chrome[a]=r
            break
        if a==1:
            r=random.choice(total_batch_list)
            chrome[a]=r
            break
        if a==2:
            r=random.choice(total_subject_list)
            chrome[a]=r
            break
        if a==3:
            r=random.choice(total_teacher_list)
            chrome[a]=r
            break
    return chrome

def fitness(chrome):
    global listyfit
    global listylen
    global listyabc
    boolean=True
    timeslot=chrome[0]
    batch=chrome[1]
    subject=chrome[2]
    teacher=chrome[3]
    sub_batch=batch_dict[chrome[1]]
    next_timeslot=chrome[0]+1
    fitscore=0
    load=subject_credithour_dict[subject]
    day=''
    adding=0
    for key,val in list(day_timeslot_dict.items()):
        if timeslot in val:
            day=key
    try:
        if(chrome in timeslot_batch_subject_teacher_list):
            pass
            listyfit[0].append('a')
            return fitscore
        else:
            fitscore+=1
            print('a ',fitscore)
    except KeyError:
        fitscore+=1
        print('a ',fitscore)
    try:
        if teacher in subject_teacher_dict[subject]:
            fitscore+=1
            print('b ',fitscore)
        else:
            pass
            listyfit[1].append('b')
            return fitscore
    except KeyError:
        pass
        listyfit[1].append('b')
        return fitscore
    try:
        if batch in teacher_batch_dict[teacher]:
            fitscore+=1
            print('c ',fitscore)
        else:
            pass
            listyfit[2].append('c')
            return fitscore
    except KeyError:
        pass
        listyfit[2].append('c')
        return fitscore
    try:
        if batch in subject_batch_dict[subject]:
            fitscore+=1
            print('d ',fitscore)
        else:
            pass
            listyfit[3].append('d')
            return fitscore
    except KeyError:
        pass
        listyfit[3].append('d')
        return fitscore
    try:
        if (day in list(day_batch_subject_ddlist.keys())) and (batch in list(day_batch_subject_ddlist[day].keys())) and (subject in day_batch_subject_ddlist[day][batch]):
            pass
            listyfit[4].append('e')
            return fitscore
        else:
            fitscore+=1
            print('e ',fitscore)
    except KeyError:
        fitscore+=1
        print('e ',fitscore)
    if subject in list(subject_lab_credithour_dict.keys()):
        adding=2
        if (timeslot in invalid_lab_timeslot_list):
            pass
            listyfit[5].append('f')
            return fitscore
        else:
            fitscore+=1
            print('f ',fitscore)
        try:
            if (teacher in list(teacher_timeslot_dict.keys())) and ((timeslot in teacher_timeslot_dict[teacher]) or (next_timeslot in teacher_timeslot_dict[teacher])):
                pass
                listyfit[6].append('g')
                return fitscore
            else:
                fitscore+=1
                print('g ',fitscore)
        except KeyError:
            fitscore+=1
            print('g ',fitscore)
        a=0
        y=''
        z=''
        if timeslot in list(timeslot_batch_dict.keys()):
            if (singlelistinlist(batch,timeslot_batch_dict[timeslot])):
                pass
                listyfit[7].append('h')
                return fitscore
            else:
                a+=1
        else:
            a+=1
        if next_timeslot in list(timeslot_batch_dict.keys()):
            if (singlelistinlist(batch,timeslot_batch_dict[next_timeslot])):
                pass
                listyfit[7].append('h')
                return fitscore
            else:
                a+=1
        else:
            a+=1
        if a==2:
            fitscore+=1
        else:
            pass
            listyfit[7].append('h')
            return fitscore
    else:
        adding=1
        fitscore+=1
        print('f ',fitscore)
        try:
            if (teacher in list(teacher_timeslot_dict.keys())) and (timeslot in teacher_timeslot_dict[teacher]):
                pass
                listyfit[6].append('g')
                return fitscore
            else:
                fitscore+=1
                print('g ',fitscore)
        except KeyError:
            fitscore+=1
            print('g ',fitscore)
        a=0
        y=''
        z=''
        if timeslot in list(timeslot_batch_dict.keys()):
            if (singlelistinlist(batch,timeslot_batch_dict[timeslot])):
                pass
                listyfit[7].append('h')
                return fitscore
            else:
                fitscore+=1
        else:
            fitscore+=1
    try:
        if (batch in list(batch_subject_load_dddict.keys())):
            print('yes')
            if (subject in list(batch_subject_load_dddict[batch].keys())):
                if (adding+(batch_subject_load_dddict[batch][subject])<=subject_credithour_dict[subject]):
                    fitscore+=1
                    print('i ',fitscore)
                    print('r',adding+(batch_subject_load_dddict[batch][subject]))
                    print('ry',subject_credithour_dict[subject])
                else:
                    listyfit[8].append('i')
                    print('r',adding+(batch_subject_load_dddict[batch][subject]))
                    print('ry',subject_credithour_dict[subject])
                    return fitscore
            else:
                fitscore+=1
                print('i ',fitscore)
        else:
            fitscore+=1
            print('i ',fitscore)
    except KeyError:
        fitscore+=1
        print('i ',fitscore)
    for i in range(9):
        listylen[i]=[int((len(listyfit[i]))),listyabc[i]]
    print('@@@@@@listylen',listylen)
    return fitscore


def afterfitness(chrome):
    boolean=True
    timeslot=chrome[0]
    batch=chrome[1]
    subject=chrome[2]
    teacher=chrome[3]
    next_timeslot=chrome[0]+1
    sub_batch=batch_dict[chrome[1]]
    fitscore=0
    load=subject_credithour_dict[subject]
    adding=1
    day=''
    global teacher_timeslot_dict
    global timeslot_batch_dict
    global day_batch_subject_ddlist
    global batch_subject_load_dddict
    global time_batch_teacher_ddlist
    global teacher_time_subject_ddlist
    global batch_time_subject_ddlist
    for key,val in day_timeslot_dict.items():
        if timeslot in val:
            day=key
    teacher_timeslot_dict=dlistmaker(teacher_timeslot_dict,teacher,timeslot)
    timeslot_batch_dict=dlistmaker(timeslot_batch_dict,timeslot,batch)
    timeslot_batch_subject_teacher_list.append(chrome[:])
    
    if subject in list(subject_lab_credithour_dict.keys()):
        chr2=chrome
        chr2[0]=next_timeslot
        timeslot_batch_subject_teacher_list.append(chr2[:])
        adding=2
        teacher_timeslot_dict=dlistmaker(teacher_timeslot_dict,teacher,next_timeslot)
        timeslot_batch_dict=dlistmaker(timeslot_batch_dict,next_timeslot,batch)
        batch_subject_load_dddict=ddloadmaker(batch_subject_load_dddict,batch,subject,adding)
    else:
        batch_subject_load_dddict=ddloadmaker(batch_subject_load_dddict,batch,subject,adding)
    day_batch_subject_ddlist=ddlistmaker(day_batch_subject_ddlist,day,batch,subject)    
    print('')
    print('timeslot_batch_subject_teacher_list', timeslot_batch_subject_teacher_list)
    print('')
    print('batch_subject_load_dddict', batch_subject_load_dddict)
    print('')
    print('teacher_timeslot_dict ',teacher_timeslot_dict)
    print('')
    print('timeslot_batch_dict ',timeslot_batch_dict)
    print('')
    print('day_batch_subject_ddlist',day_batch_subject_ddlist)
    print('')
    print('')
    end=time.time()
    print("total time minutes ", (end-start)/60)

def working():
    vales=''
    timeslot=0
    subject=''
    batch=''
    teacher=''
    taken=[]
    while(len(taken)!=len(total_timeslot_list)):
        tim=random.choice(total_timeslot_list)
        while (tim in taken):
            tim=random.choice(total_timeslot_list)
        taken.append(tim)
    #for tim in total_timeslot_list:
        timeslot=tim
        for sub in total_subject_list:
            subject=sub
            for tea in subject_teacher_dict[subject]:
                teacher=tea
                for bat in subject_batch_dict[subject]:
                    batch=bat
                    if batch in teacher_batch_dict[tea]:
                        chrome=[timeslot,batch,subject,teacher]
                        print(chrome)
                        fitscore=fitness(chrome)
                        print('fitscore',fitscore)
                        if(fitscore==9):
                            afterfitness(chrome)    
                        else:
                            pass
           
                
                
working()





print(len(timeslot_batch_subject_teacher_list))
timeslot_batch_subject_teacher_list.sort()
for i in timeslot_batch_subject_teacher_list:
    print(i)

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
leena=[]
for i in timeslot_batch_subject_teacher_list:
    c=subject_credithour_dict[i[2]]
    r=[i[2],i[1],c]
    leena.append(r)
leena.sort()
for j in leena:
    print(j)
    





def populate(frame):
    all_colors = ['AntiqueWhite1','CadetBlue1', 'DarkGoldenrod1', 'DarkOliveGreen1','DarkOrange1','DarkOrchid1','DarkSeaGreen1','DarkSlateGray1','DeepPink2','DeepSkyBlue2','HotPink1','IndianRed1','LemonChiffon2','LightBlue1','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'alice blue', 'antique white', 'aquamarine', 'aquamarine2', 'aquamarine4', 'azure', 'azure2', 'azure3', 'azure4', 'bisque', 'bisque2', 'bisque3', 'bisque4', 'blanched almond', 'blue', 'blue violet', 'blue2', 'blue4', 'brown1', 'brown2', 'brown3', 'brown4', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'cadet blue', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate1', 'chocolate2', 'chocolate3', 'coral', 'coral1', 'coral2', 'coral3', 'coral4', 'cornflower blue', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'cyan', 'cyan2', 'cyan3', 'cyan4', 'dark goldenrod', 'dark green', 'dark khaki', 'dark olive green', 'dark orange', 'dark orchid', 'dark salmon', 'dark sea green', 'dark slate blue', 'dark slate gray', 'dark turquoise', 'dark violet', 'deep pink', 'deep sky blue', 'dim gray', 'dodger blue', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floral white', 'forest green', 'gainsboro', 'ghost white', 'gold', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4','green yellow', 'green2', 'green3', 'green4', 'honeydew2', 'honeydew3', 'honeydew4', 'hot pink', 'indian red', 'ivory2', 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'lavender', 'lavender blush', 'lawn green', 'lemon chiffon', 'light blue', 'light coral', 'light cyan', 'light goldenrod', 'light goldenrod yellow', 'light grey', 'light pink', 'light salmon', 'light sea green', 'light sky blue', 'light slate blue', 'light slate gray', 'light steel blue', 'light yellow', 'lime green', 'linen', 'magenta2', 'magenta3', 'magenta4', 'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'medium aquamarine', 'medium blue', 'medium orchid', 'medium purple', 'medium sea green', 'medium slate blue', 'medium spring green', 'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'navajo white', 'navy', 'old lace', 'olive drab', 'orange', 'orange red', 'orange2', 'orange3', 'orange4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'pale goldenrod', 'pale green', 'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff', 'pink', 'pink1', 'pink2', 'pink3', 'pink4', 'plum1', 'plum2', 'plum3', 'plum4', 'powder blue', 'purple', 'purple1', 'purple2', 'purple3', 'purple4', 'red', 'red2', 'red3', 'red4', 'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'sandy brown', 'sea green', 'seashell2', 'seashell3', 'seashell4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'sky blue', 'slate blue', 'slate gray', 'snow', 'snow2', 'snow3', 'snow4', 'spring green', 'steel blue', 'tan1', 'tan2', 'tan4', 'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'tomato', 'tomato2', 'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'violet red', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white smoke', 'yellow', 'yellow green', 'yellow2', 'yellow3', 'yellow4']
    day=[1,8,15,22,29]
    dicty={}
    count=0
    for j in day:
        for i in range(1,8):
            count+=1
            dicty[count]=[j,i]
    def total(chap):
        tiny=0
        for i in timeslot_batch_subject_teacher_list:
            if i[0]==chap:
                tiny+=1
        return tiny
    global timeslot_batch_subject_teacher_list
    daily=['','Mon','Tue','Wed','Thu','Fri']
    listy=['','9-10','10-11','11-12','12-1','2-3','3-4','4-5']
    count=0
    tcount=0
    recount=0
    chap=''
    rday=[1,8,15,22,29,36,42,54]
    ddd=0
    checked=[]
    flag=0
    for j in range(0,8):
        for i in range(0,36):
            if (i==0) and (j>0):
                b = tk.Label(frame, text=listy[j],relief="solid")
                b.grid(row=i, column=j)
            elif (j==0) and (i in day):
                count+=1
                b = tk.Label(frame, text=daily[count],relief="solid")
                b.grid(row=i, column=j, rowspan=5)
            elif(i>0) and (j>0):
                for key,val in dicty.items():
                    if val==[i,j]:
                        chap=key
                        tcount=recount
                        recount+=1
                        color=random.choice(all_colors)
                        break
                if i >=rday[tcount] and i<rday[recount]:
                    for a in timeslot_batch_subject_teacher_list:
                        if a[0]==chap:
                            r=timeslot_batch_subject_teacher_list.index(a)
                            if r in checked:
                                continue
                            else:
                                bat=a[1]
                                sub=a[2]
                                str1=bat+' '+sub
                                b = tk.Label(frame, text=str1,bg=color)
                                b.grid(row=i, column=j)
                                checked.append(r)
                                flag=1
                                break
                    if flag==1:
                        flag=0
                        continue
                    b = tk.Label(frame, text='',bg='white')
                    b.grid(row=i, column=j)
        recount=0
        tcount=0

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="#ffffff")
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((8,8), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

print('')
end=time.time()
print("total time minutes ", (end-start)/60)

root.mainloop()











        



    
    
    




