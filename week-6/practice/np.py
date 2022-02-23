# 載入 numpy 套件
from os import sep
from unittest import result
import numpy as np

def basic():
    # 根據列表建立 ndarray 物件
    ndarr=np.array([3, 4, -5])
    # 觀察
    print(ndarr.size)
# basic() # 基礎
def ndarray():
    # 一維陣列
    data=np.array([3, 2, 6, 4])
    print(data)
    data=np.empty(4)
    print(data)
    data=np.zeros(3)
    print(data)
    data=np.arange(5)
    print(data)
    
    # 二維陣列
    data=np.array([ # 3x3的陣列
        [2, 3, 2],
        [1, 5, 2],
        [4, 2, 1]
    ])
    print(data)
    data=np.empty([3, 3]) # 資料未指定的 3x3 陣列
    print(data)
    data=np.ones([2, 3])

    # 三維陣列
    data=np.array([ # 2x2x2 陣列
        [
            [3, 1], [1, 2]
        ],
        [ 
            [2, 5], [10, 2]
        ]
    ])
    print(data)
    # 高維陣列
    data=np.ones([2, 1, 1, 2])
    print(data)
# ndarray() # 建立矩陣
def operation():
    # 逐元運算 (elementwise) / shape 必須一樣
    data1=np.array([3, 2, 10])
    data2=np.array([1, 3, 6])
    result=data1+data2
    print("加法", result)
    result=data1*data2
    print("乘法", result)
    result=data1>data2
    print("大於", result)
    result=data1==data2
    print("是否相等", result)

    # 矩陣運算 (matrix)
    data1=np.array([ # 1x2 矩陣
        [1, 3]
    ])
    data2=np.array([ # 2x3 矩陣
        [2, -1, 3],
        [-2, 4, 1]
    ])
    result=data1.dot(data2) # 1x3 矩陣
    # result=data1@data2
    print("內積", result)
    result=np.outer(data1, data2) # 2x6 矩陣
    print("外積", result, sep="\n")

    # 統計運算 (statistics)
    # ndarray 多維陣列 > 陣列
    data=np.array([
        [2, 1, 7],
        [-5, 3, 8]
    ])
    result=data.sum()
    print("總和", result)
    result=data.max()
    result=data.mean()
    result=data.std()

    result=data.sum(axis=0) # 總和 第1個維度
    print(result)
    result=data.sum(axis=1) # 總和 第2個維度
    print(result)

    # 逐值累加
    result=data.cumsum()
    print("逐值累加", result)
    result=data.cumsum(axis=0)
    print("對第1個維度逐值累加", result, sep="\n")
# operation() # 矩陣運算(加減乘除, 大小...)
def control():
    data=np.ones(10)
    print(data)
    print(data.shape)
    
    # 資料轉置
    data=np.array([
        [2, 4, 1],
        [1, 5, 0]
    ])
    print(data.T)
    print(data.T.shape)

    # 扁平化資料
    data=np.array([
        [
            [2, 1, 3], [1, 2, 3]
        ],
        [
            [0, 2, 1], [8, 9, 10]
        ]
    ])
    newData=data.ravel()
    print(newData)

    # 重塑資料形狀
    data=np.array([
        [
            [2, 1, 3], [1, 2, 3]
        ],
        [
            [0, 2, 1], [8, 9, 10]
        ]
    ]) # (2x2x3)
    newData=data.reshape(3, 4)
    print(newData)

    data=np.zeros(18).reshape(3, 2, 3)
    print(data)
    data=np.arange(9).reshape(3, 3)
    print(data)
    print(data.T)
# control() # 操作矩陣(控制資料形, arange後 > 改形)
def index_slice():
    # 多維度資料 indexing
    # 單維度
    data=np.array([1, 5, 2, 10])
    print(data[2])
    # 多維度
    data=np.array([
        [0, 1],
        [10, -5],
        [2, 6]
    ])
    print(data[2, 1])

    # 多維度資料 slicing
    # 單維度
    data=np.array([1, 5, 2, 10])
    print(data[1:3])
    # 多維度
    data=np.arange(12).reshape(4,3)
    print(data)
    print(data[1:3, 0:2])
    print(data[0:2, 1])
    # 使用 ... 代表全都要
    data=data.reshape(2, 2, 3)
    print("3維", data, sep="\n") 
    print(data[0, ...])
    print(data[..., 1:3])
# index_slice() # 矩陣索引查值
def stack():
    # 準備資料
    arr1=np.arange(6).reshape(2, 3)
    arr2=np.arange(6, 12).reshape(2, 3)
    arr3=np.arange(12, 16).reshape(2, 2)
    print("first", arr1, sep="\n")
    print("second", arr2, sep="\n")
    # 合併第1個維度
    result=np.vstack((arr1, arr2))
    print("arr1+arr2", result, sep="\n")
    # 合併第2個維度
    result=np.hstack((arr1, arr2, arr3))
    print(result)
# stack() # 矩陣合併