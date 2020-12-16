#coding:gbk
"""
���þ������㷨���з���
���ߣ������
���ڣ�2020/12/17
"""
import pandas as pd           # ������Ҫ�õĿ�
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sb
import sklearn.utils as sk

# ��������
df = pd.read_csv('frenchwine.csv',encoding='gb18030')
df.columns = ['species', 'alcohol', 'malic_acid', 'ash', 'magnesium',"alcalinity ash"]
# �鿴ǰ6������
df.head()
print(df.head()) 


# �鿴����������ͳ����Ϣ
df.describe()
print(df.describe())

def scatter_plot_by_category(feat, x, y): #���ݵĿ��ӻ� 
    alpha = 0.5
    gs = df.groupby(feat)
    cs = cm.rainbow(np.linspace(0, 1, len(gs)))
    for g, c in zip(gs, cs):
        plt.scatter(g[1][x], g[1][y], color=c, alpha=alpha)

plt.figure(figsize=(20,5))
plt.subplot(131)
scatter_plot_by_category('species', 'alcalinity ash', 'magnesium')
plt.xlabel('alcalinity ash')
plt.ylabel('magnesium')
plt.title('species')
plt.show()

plt.figure(figsize=(20, 10)) #����seaborn������������Ѳ�ͬ����ͼ
for column_index, column in enumerate(df.columns):
    if column == 'species':
        continue
    plt.subplot(2, 3, column_index + 1)
    sb.violinplot(x='species', y=column, data=df)
plt.show()

# ���ȶ����ݽ����з֣������ֳ�ѵ�����Ͳ��Լ�
from sklearn.model_selection import train_test_split #����sklearn���н�����飬����ѵ�����Ͳ��Լ�
all_inputs = df[['alcohol', 'malic_acid',
                             'ash',"alcalinity ash",'magnesium']].values
all_species = df['species'].values

(X_train,
 X_test,
 Y_train,
 Y_test) = train_test_split(all_inputs, all_species, train_size=0.7, random_state=1)#80%������ѡΪѵ����
 
 


# ʹ�þ������㷨����ѵ��
from sklearn.tree import DecisionTreeClassifier #����sklearn���е�DecisionTreeClassifier������������
# ����һ������������
decision_tree_classifier = DecisionTreeClassifier()

# ѵ��ģ��
model = decision_tree_classifier.fit(X_train, Y_train)
# ���ģ�͵�׼ȷ��
print(decision_tree_classifier.score(X_test, Y_test)) 


print(X_test)
model.predict(X_test)
print(model.predict(X_test))#������ԵĽ���������ģ��Ԥ��Ľ��


##���������ӻ�
from IPython.display import Image  
# from sklearn.externals.six import StringIO  #sklearn 0.23�汾�Ѿ�ɾ���������,ֱ�Ӱ�װsix����
from six import StringIO
from sklearn.tree import export_graphviz


features = list(df.columns[:-1])
print(features)


import pydotplus
import os #Ҫ��װһ��Graphviz���
os.environ['PATH'] = os.environ['PATH'] + (';c:\\Program Files\\Graphviz\\bin\\') #
dot_data = StringIO()  
export_graphviz(decision_tree_classifier, out_file=dot_data,feature_names=features,filled=True,rounded=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
# Image(graph[0].create_png())  
graph.write_pdf("frenchwine.pdf") #��frenchwine���ݼ����þ������㷨���ӻ�������ֵ�frenchwine.pdf�ļ���


