##导入模块
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
## 从文件读取数据，并提取特征数据集X和对应的Zone数据集y
data=pd.read_csv(r"C:\Users\Tg'w\Desktop\桌面\python.update\rainfalldata.csv", encoding='gbk')
x=data.iloc[:,1:5]
y=data.loc[:,['Zone']]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
##进行处理
print ("划分的训练集特征数据是：")
print (x_train)
print ("训练集对应的类别（Zone）是：")
print (x_test)
print ("-------------------")
print ("划分的测试集特征数据是：")
print (y_train)
print ("测试集对应的类别（Zone）是：")
print (y_test)

