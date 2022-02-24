import pandas as pd

'''
총 세 가지의 데이터 구조 못떼루
1. 시리즈(series)
2. 데이터프레임(dataframe)
3. 패널(panel)
'''

#시리즈
sr=pd.Series([17000,18000,1000,5000],
             index=["피자","치킨","콜라","맥주"])
print('시리즈 출력 :')
print('-'*15)
print(sr)

print('시리즈의 값 : {}'.format(sr.values))
print('시리즈의 인덱스 : {}'.format(sr.index))


#데이터프레임
values=[[1,2,3],[4,5,6],[7,8,9]]
index=['하나','둘','셋']
columns=['A','B','C']

df=pd.DataFrame(values,index=index,columns=columns)
print('데이터프레임 출력 : ')
print(df)

print('데이터프레임의 인덱스 : {}'.format(df.index))
print('데이터프레임의 열이름 : {}'.format(df.columns))
print(df.values)
print(df.index)
print(df.columns)

#데이터프레임의 생성
#리스트로 생성하기
data = [
    ['1000','Steve',90.72],
    ['1001','James',78.09],
    ['1002','Doyeon',98.43],
]

df=pd.DataFrame(data)
print(df)

#열 지정해주기
df=pd.DataFrame(data,columns=['학번','이름','점수'])
print(df)

#딕셔너리로 생성하기
data = {
    '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
    '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
    '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
    }

df = pd.DataFrame(data)
print(df)

#데이터프레임 조회하기
'''
- df.head(n) : 앞 부분을 n개만 보기
- df.tail(n) : 뒷 부분을 n개만 보기
- df['열이름'] : 해당되는 열을 확인
'''
print(df.head(2))
print(df.tail(3))
print(df['학번'])

#외부 데이터 읽기
df=pd.read_csv('')|