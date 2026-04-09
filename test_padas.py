
import pandas as pd
# s1=pd.Series([1,2,3,4,5,6],index=['a','a','c','d','e','f'])
# print(s1['a'])


data = {
    'name': ['Mahesh', 'Ramesh', 'Suresh'],
    'age': [25, 26, 27],
    'gender': ['M', 'M', 'M']
}


df = pd.DataFrame(data)

# print(df)
# df.to_html('student_details', index=False)

# print(df['name'])
# print(df['age'])


df = pd.read_csv('titanic.csv')
# print(df.head(10))
# print(df)
# print(df)
# print(df.head())
# print('-----------')
# print(df.tail())

# print(df.shape)
# print(df.info())
# print(df.info())

# print('------------')
# print(df.describe())
# print(df.dtypes)
# print(df.columns)

# print(df.index)

# for i in df.index:
#     print(i)


# print(df.isnull().sum())
# print(df.isnull().sum())
# # print(df)
# print(df['Survived'].value_counts())
# print(df['Survived'].mean()*100)
# print(df['Age'].mean())
# print(df['Fare'].max(), df['Fare'].min())
# print(df['Sex'].value_counts())
# print(df['Embarked'].value_counts())
# print(df['Pclass'].nunique())
# print(df.groupby('Survived')['Age'].mean())
# print(df.groupby('Pclass')['Survived'].mean()*100)
# print(df.groupby('Pclass')['Fare'].mean())
# print(df)
# print(df[['Name', 'Survived']])
# print(df[['Name','Age']])
# print(df[['Name','Sex']])
# print(df.loc[[2, 3, 4], ['Age', 'Name']])
# print('---------------')
# print(df.iloc[[2, 3, 4], [0, 1]])

# print(df[df['Age'] > 30][df['Survived'] == 0][['Age', 'Survived', 'Name']])
# print(df[df['Age']>30][df['Survived']==0][['Age','Survived']])
# print(df[df['Age']>30][df['Survived']==1][['Age','Survived','Name']])
# print(df[df['Age']<30][df['Survived']==1][['Age','Survived','Name']])
# print('---------------')
print(df.groupby("Sex")["Age"].mean())
# print(df.groupby("Pclass")["Age"].mean())
# print(df.groupby("Pclass")["Fare"].mean())


