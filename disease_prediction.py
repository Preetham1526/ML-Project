from tkinter import *
import numpy as np
import pandas as pd
import sklearn
from tkinter import *

import ctypes,os
from PIL import ImageTk, Image
import statistics
 

import tkinter.filedialog as filedialog 
import tkinter.messagebox as tkMessageBox


l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']


    
tr=pd.read_csv(r"C:\Users\eswar\OneDrive\Desktop\ML Project\Training.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)
X= tr[l1]
y = tr[["prognosis"]]


tr["skin_rash"].unique()
df=pd.read_csv(r"C:\Users\eswar\OneDrive\Desktop\ML Project\Testing.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= df[l1]
y_test = df[["prognosis"]]
np.ravel(y_test)
from sklearn import tree
clf3 = tree.DecisionTreeClassifier()
clf3 = clf3.fit(X,y)
from sklearn.ensemble import RandomForestClassifier
clf4 = RandomForestClassifier()
clf4 = clf4.fit(X,np.ravel(y))
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb=gnb.fit(X,np.ravel(y))
from sklearn import svm
clf5 = svm.SVC()
clf5.fit(X,y)

def DecisionTree():
    l2=[]
    for x in range(0,len(l1)):
        l2.append(0)
    
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    y_t = y_test.values
    y_t = np.reshape(y_t, (1,np.product(y_t.shape)))
   
    score_dt=accuracy_score(y_t[0], y_pred)
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
                
    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]
    
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if psymptoms==['None', 'None', 'None']:
            tkMessageBox.showinfo("Disease Prediction System","Can not predict for all null values")
    else:
        if (h=='yes'):
            return disease[a]

def randomforest():
    l2=[]
    for x in range(0,len(l1)):
        l2.append(0)

    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    y_t = y_test.values
    y_t = np.reshape(y_t, (1,np.product(y_t.shape)))
   
    score_rf=accuracy_score(y_t[0], y_pred)
    
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break
    if psymptoms==['None', 'None', 'None']:
            tkMessageBox.showinfo("Disease Prediction System","Can not predict for all null values")
    else:
        if (h=='yes'):
            return disease[a]

def NaiveBayes():
 
    l2=[]
    for x in range(0,len(l1)):
        l2.append(0)

    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    y_t = y_test.values
    y_t = np.reshape(y_t, (1,np.product(y_t.shape)))
   
    score_nb=accuracy_score(y_t[0], y_pred)
    
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break
    if psymptoms==['None', 'None', 'None']:
            tkMessageBox.showinfo("Disease Prediction System","Can not predict for all null values")
    else:
        if (h=='yes'):
             return disease[a]

def SVM():
    l2=[]
    for x in range(0,len(l1)):
        l2.append(0)
    
    from sklearn.metrics import accuracy_score
    y_pred=clf5.predict(X_test)
    y_t = y_test.values
    y_t = np.reshape(y_t, (1,np.product(y_t.shape)))
   
    score_sv=accuracy_score(y_t[0], y_pred)
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
                
    inputtest = [l2]
    predict = clf5.predict(inputtest)
    predicted=predict[0]
    
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if psymptoms==['None', 'None', 'None']:
            tkMessageBox.showinfo("Disease Prediction System","Can not predict for all null values")
    else:
        if (h=='yes'):
            return disease[a]

def FinalPred():
    pred1=DecisionTree()
    pred2=randomforest()
    pred3=NaiveBayes()
    pred4=SVM()
    print(pred1)
    print(pred2)
    print(pred3)
    print(pred4)
    
    d=[pred1, pred2, pred3,pred4]
    final_pred = statistics.mode(d)
    tkMessageBox.showinfo("Disease Prediction System", "Final Prediction :"+final_pred)
    
algorithms = ["FinalPred"]




try:
    analyze.destroy()
except:
    pass
try:
    about.destroy()
except:
    pass

window = Toplevel()

OPTIONS = tuple(sorted(l1))

Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)

Name = StringVar()
img = Image.open(r"C:\Users\eswar\OneDrive\Desktop\ML Project\homepage.jpg")
img = ImageTk.PhotoImage(img)
panel = Label(window, image=img)
panel.pack(side="top", fill="both", expand="yes")

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0]//2-446)
b= str(lt[1]//2-383)


window.title("HOME - Disease Prediction System")
window.geometry("800x584+"+a+"+"+b)
window.resizable(0,0)


S1En = OptionMenu(window, Symptom1,*OPTIONS)
S1En.place(x=130,y = 187)

S2En = OptionMenu(window, Symptom2,*OPTIONS)
S2En.place(x=130,y = 233)

S3En = OptionMenu(window, Symptom3,*OPTIONS)
S3En.place(x=130,y = 283)

getstarted = Button(window,text = "Final Prediction",command = FinalPred, font = ("Arial Narrow",14,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="#1B6DE8",fg="white",activebackground = "#1B6DE8",activeforeground = "white")
getstarted.place(x=91,y = 406)



window.mainloop()




