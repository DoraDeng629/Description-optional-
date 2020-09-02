#Yanyan Deng Homework9 final project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fileName = 'C:/Users/mogud/Desktop/PythonIO/KaggleV2-May-2016.csv'

print("welcome to my final work, let's we think about:\n>>A person makes a doctor appointment, receives all the instructions and no-show. Who to blame? \n>")

ready= input ('Are you ready to explore my work?\n>>')

answer={'yes','Yes','YES','sure','yeah','yup','si','oui','Y','y','shi'}

if ready in answer:
    print('Prefect,let\'s get start to see my work!')
else:
    print('Come back when you are ready!')

#get the data information
df = pd.read_csv(fileName)
print(df.info()) 
print(df.head()) 
print(df.describe())

try:
    fh = open('fileName', 'w',encoding='utf8')
    line=fh.write('')
except PermissionError:
    print('Please close any program using the file,and try again')
except IOError:
    print('Do not find the file' )
except NameError:
    print('Do not define the name')
else:
    print('File checked successfully')
    fh.close()

#Rename columns and correct some words
df.rename(columns = {"Hipertension": "Hypertension", "Handcap": "Handicap", "No-show":"No_show"},  inplace=True)
print(df.head(1))
print("Gender", df["Gender"].unique())
print("Age", df["Age"].unique())
print("Scholarship", df["Scholarship"].unique())
print("Hypertension", df["Hypertension"].unique())
print("Diabetes", df["Diabetes"].unique())
print("Alcoholism", df["Alcoholism"].unique())
print("Handicap", df["Handicap"].unique())
print("SMS_received", df["SMS_received"].unique())
print("No_show", df["No_show"].unique())

# Cast data type
df["ScheduledDay"] = pd.to_datetime(df["ScheduledDay"],format = '%Y-%m-%d')
df["AppointmentDay"] = pd.to_datetime(df["AppointmentDay"],format = '%Y-%m-%d')

#Filter data
df= df[df.Age >= 0]
print("Age",df["Age"].unique())

#Then study the factors related to No_show, check whether the gender and age are related to it

# Total No_show number
print(df["No_show"].value_counts())
noshowNumber=88208
showNumber=22319
colors = ["red", "blue"]
x = [0,1]
y = [noshowNumber,showNumber]
labels = ['No', 'Yes']
plt.ylabel('Number of No_show')
plt.title('Overall No_show data')
plt.bar(x, y, tick_label = labels, color = colors)
plt.show()

#Gender and No_show
gender = df["Gender"].value_counts()
print(gender)
proportionGender=pd.crosstab(df.Gender, df.No_show, normalize='index')
print(proportionGender)

#Age and No_show
print(df['Age'].describe())
age_edges = [0, 18, 37, 55, 115] #Cut Age into Different Age Groups
df['Age_group'] = pd.cut(df['Age'], age_edges)
print(df.head())
proportionAge=pd.crosstab(df.Age_group, df.No_show, normalize='index')
print(proportionAge)

#conclusion: The number of people who no_show was more than four times higher than the number of people who showed up, so according to gender and age to see if these factors are related to the absence.
#(1):According to the percentage of statistics, gender has little effect on no show rate.
#(2):Grouped according to age group, patients with 18-37 years old have the highest absent rate, followed by 0-18 years old, and the elderly have the least
#Suggestion:In real life, medical education should be strengthened for people aged 0-37, so that they should pay attention to medical problems and not waste medical resources.
#Especially at this particular time, we should pay more attention to social medical problems and not contempt medical treatment.

