import numpy as np s
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
%matplotlib inline

#importing our dataset.
df = pd. read_csv('D:\\Main Flow\\Tasks\\Task5\\heart.csv')

#checking first five rows by calLing df.head（）
df.head()
df.tail()

df.columns.values

#checking for null values
df.isna().sum()

#concise summaru
df.info()

df.hist(bins = 50, grid = False , figsize=(20,15));

df.describe()

questions = ["1. How many people have heart disease and how many people doesn't have heart disease?",
    "2. People of which sex has most heart disease?",
    "3. People of which sex has which type of chest pain most?",
    "4. People with which chest pain are most prone to have heart disease?",
    "5. How many people have diabetes and how many people don't have diabetes?",
    "6. Which age group has the highest incidence of hypertension?",
    "7. Which gender has the highest prevalence of diabetes?"]
questions 

#Let's find the answer of first question.
#1. How many people have heart disease and how many people doesn't have heart disease?"
#getting the values 
df.target.value_counts()
#plotting bar chart.
df.target.value_counts().plot(kind = 'bar', color=["orchid", "salmon"])
plt.title("Heart Disease values")
plt.xlabel("1 = Heart Disease, 0 = No heart Disease") 
plt.ylabel("Amount");
#plotting pie chart.
df.target.value_counts().plot(kind = 'pie', figsize = (8, 6))
plt.legend(["Disease","No disease"]);
#'0' represent 'Female'

#'1' represent 'Male'

#SEX column part

#'0' represent 'No disease'

#'1' represent 'Disease'

#Target column part

#Now let's check how many 'Male' and 'Female' are in the dataset

df.sex.value_counts()
#plotting pie chart.
df.target.value_counts().plot(kind = 'pie', figsize = (8, 6))
plt.title('Male Female ratio')
plt.legend(['Male','Female']);

#Let's find the answer of our 2nd question.

#2.People of which sex has most heart disease?'

pd.crosstab(df.target, df.sex)
sns.countplot(x = 'target', data = df, hue = 'sex')
plt.title("Heart Disease Frequency for Sex") 
plt.xlabel("0 = No heart Disease, 1 = Heart Disease");
sns.countplot(x='target', data=df, hue='sex')
plt.title("Heart Disease Frequency for Sex")
plt.xlabel("0 = No heart Disease, 1 = Heart Disease")
plt.show()
# Check the unique values in 'sex' and 'target' columns
print(df['sex'].unique())
print(df['target'].unique())

# Check for any non-numeric or unexpected values
print(df[df['sex'].apply(lambda x: not str(x).isdigit())])
print(df[df['target'].apply(lambda x: not str(x).isdigit())])
#Number of male is more than double in our dataset than female.

#More than '45% male has heart disease and '75% female has heart disease.

#pLotting a bar chart
df.cp.value_counts().plot(kind = 'bar', color = ['salmon', 'lightskyblue', 'springgreen', 'khaki'])
plt. title( 'Chest pain type vs count');

#Let's move to question 3

#3. 'People of which sex has which type of chest pain most?'

#counting values for different chest paib
df.cp.value_counts();
pd.crosstab(df.sex, df.cp)
pd.crosstab(df.sex, df.cp).plot(kind = 'bar' , color = ['coral','lightskyblue','plum','khaki'])
plt.title('Type of chest pain for sex')
plt.xlabel('0 = Female, 1 = Male');
#Most of "male' has 'type l' chest pain and least of "Male has "type 4' pain.
#in case of 'Female' 'type @' and "type 2' percentage is almost same.

#Now question 4!

#4. People with which chest pain are most pron to have heart disease?'

pd.crosstab(df.cp, df.target)
sns.countplot(x = 'cp', data = df, hue = 'target');
#Most of people who has type @' chest pain has less chance of heart disease.

#And we see the opposite for other types.

#Now let's take look at our age column.

#create a distribution plot with normal distribution curve
sns.displot(x = 'age', data = df, bins = 30, kde = True);
#58-59 year old people are most in the dataset.
#Let's plot another distribution plot for "Maximum heart rate'
sns.displot(x = 'thalach', data = df, bins = 30, kde = True, color = 'chocolate');

# How many people have diabetes and how many people don't have diabetes?

# Mapping the diabetes column for better readability

diabetes_map = {0: 'No Diabetes', 1: 'Diabetes'}
df['diabetes'] = df['diabetes'].map(diabetes_map)

# How many people have diabetes and how many people don't have diabetes?

# Mapping the diabetes column for better readability

diabetes_map = {0: 'No Diabetes', 1: 'Diabetes'}
df['diabetes'] = df['diabetes'].map(diabetes_map)

#7. Which gender has the highest prevalence of diabetes?'
# Counting diabetes cases by gender and determining the gender with the highest prevalence
diabetes_by_gender = df.groupby('sex')['fbs'].sum()
highest_prevalence_gender = diabetes_by_gender.idxmax()

# Displaying gender with the highest prevalence of diabetes
print(f"Gender with the highest prevalence of diabetes: {'Male' if highest_prevalence_gender == 1 else 'Female'}")

# Bar plot for diabetes counts by gender
diabetes_by_gender.plot(kind='bar', color=["lightcoral", "lightseagreen"])
plt.title("Diabetes Counts by Gender")
plt.xlabel("Gender (0 = Female, 1 = Male)")
plt.ylabel("Number of Diabetes Cases")
plt.show()

# Pie chart for diabetes counts by gender
diabetes_by_gender.plot(kind='pie', autopct='%1.1f%%', colors=["lightcoral", "lightseagreen"], startangle=90)
plt.title("Diabetes Distribution by Gender")
plt.ylabel("")  # Removing the y-label for better visualization
plt.show()
