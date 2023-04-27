import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

df = pd.read_csv("cancer.csv", encoding='ANSI')
print(df)

# 1999 ~ 2020 20년간 연도별 총 발생자 수의 증가와 최다발생 암 top2를 뽑아 한 눈에 확인하고싶다
def graph1():
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
    # 총 발생자수 꺾은선 그래프
    df1 = df.groupby('SEX').get_group('남녀전체').loc[df['CATEGORY']=='모든암']
    xp = df1['YEAR'] # x축 내용이 될 연도
    yp1 = df1['INCIDENCE'] # 발생자수
    

    # 최다발생 top2 뽑기
    df2 = df.groupby('SEX').get_group('남녀전체').loc[df['CATEGORY']!='모든암']
    x1kli = [] 
    x1vli = []
    x2kli = []
    x2vli = []
    for x in range(1999, 2021):
        # 종류와 값을 dict로 담으면 중복이 제거되어 1999~2021 연도만큼 데이터가 안쌓여서 리스트로
        i = 'CATEGORY'
        j = 'INCIDENCE'
        dfx1 = df2.groupby('YEAR').get_group(x)
        dfx2 = dfx1.sort_values(by=['INCIDENCE'], ascending=False).head(2)
        #print(type(dfx2))
        x1vli.append(dfx2[j].iloc[0]) # no.1 암의 발생자수
        x2vli.append(dfx2[j].iloc[1]) # no.2 암의 발생자수
        x1kli.append(dfx2[i].iloc[0]) # no.1 암의 종류
        x2kli.append(dfx2[i].iloc[1]) # no.2 암의 종류

    plt.figure(figsize=(15,6))
    #no.2 암의 발생자수 no.1 암의 발생자수 위에 쌓기
    p1 = plt.bar(xp, x1vli, color='darkturquoise')
    p2 = plt.bar(xp, x2vli, bottom=x1vli, color ='paleturquoise') 

    # 연도별로 어떤 종류가 최다발생했는지 라벨링
    plt.bar_label(p1, labels=x1kli, label_type='center') #no.1
    plt.bar_label(p2, labels=x2kli, label_type='center') #no.2
    plt.ylabel('최다발생 암 분류')

    y2 = plt.twinx()
    y2.plot(xp, yp1, marker='D', label="incidence", color = 'darkmagenta')
    plt.ylabel('발생자수', color='darkmagenta')
    y2.tick_params(axis='y', labelcolor='darkmagenta')
    y2.set_ylim(0, 260000)
    plt.xticks(xp)
    plt.title('연간 암 발생 현황')
    plt.show()


# 특정 한 해(year) 성별에 따른 암 종류별 발생자수를 확인하고싶다
def graph2(year):
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
    dfm = df.groupby('SEX').get_group('남자').loc[df['CATEGORY']!='모든암'].loc[df['YEAR']==year]
    dfm = dfm.sort_values(by=['INCIDENCE'], ascending=False)
    yp = dfm.loc[:,'CATEGORY']
    xpm = dfm.loc[:,'INCIDENCE']

    dfw = df.groupby('SEX').get_group('여자').loc[df['CATEGORY']!='모든암'].loc[df['YEAR']==year]
    xpw = dfw.loc[:,'INCIDENCE']

    plt.figure(figsize=(12,6))
    plt.barh(yp, xpm, color='olive', label='man')
    plt.barh(yp, -xpw, color='gold', label='woman')
    plt.title('성별에 따른 암발생 현황')
    plt.xlabel('발생자수')
    plt.ylabel('분류')
    plt.xticks([-15000,-10000,-5000,0,5000,10000,15000],('15000','10000','5000','0','5000','10000','15000'))
    plt.legend()
    plt.show()

#graph1()
graph2(2020)
