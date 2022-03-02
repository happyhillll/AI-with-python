import numpy as np
vec=np.array([1,2,3,4,5])
print(vec)

#2차원 배열
mat = np.array([[10,20,30],[60,70,80]])
print(mat)

#모든 값이 0인 2x3 배열 생성
zero_mat=np.zeros((2,3))
print(zero_mat)

#모든 값이 1인 2x3 배열 생성
one_mat = np.ones((2,3))
print(one_mat)

#모든 값이 특정 상수인 배열 생성. 이 경우 7
same_value_mat= np.full((2,2),7)
print(same_value_mat)

#대각선 값이 1이고 나머지 값이 0인 2차원 배열을 생성
eye_mat=np.eye(3)
print(eye_mat)

#np.reshape()는 내부 데이터는 변경하지 않으면서 배열의 구조를 바꿈.
reshape_mat=np.array(np.arange(30)).reshape((5,6))
print(reshape_mat)

#정수 인덱싱
mat=np.array([[1,2],[4,5],[7,8]])
print(mat)

#1행 0열의 원소
print(mat[1,0])


import tensorflow as tf

print(tf.__version__)
a=tf.random.uniform([2,3],0,1)
print(a)
print(type(a))
