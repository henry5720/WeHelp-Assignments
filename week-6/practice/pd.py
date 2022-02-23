from multiprocessing import Condition
from operator import index
import pandas as pd

def Series_basic():
    # Series 單維度資料
    data=pd.Series([20, 10, 15]) # (列表)
    
    # 基本 Series 操作
    print(data)
    print("Max", data.max())
    print("Median", data.median())
    print(data * 2)
    data=data==20 # Series內資料 > 是否和20相等
    print(data)

def DataFrame_basic():
    # DataFrame 雙維度資料
    data=pd.DataFrame({ # (字典)
        "name":["Amy", "Henry", "Bob"],
        "salary":[30000, 50000, 40000]
    }) 
    # 基本 DataFrame 操作
    print(data)
    # 取得特定欄 (column)
    print(data["name"]) # ["欄位名稱"]
    # 取得特定列 (row)
    print(data.iloc[0]) # ilocation[列編號] 順序由0開始累加 

def Series_handle():
    # 資料索引
    data=pd.Series([5, 4, -2, 3, 7], index=["a", "b", "c", "d", "e"])
    print(data)
    # 觀察資料
    print("資料型態", data.dtype)
    print("資料數量", data.size)
    print("資料索引", data.index)
    # 取得資料: 根據數據, 根據索引
    print(data[2], data[0])
    print(data["e"], data["d"])
    # 數字運算 基本, 統計, 順序
    print("最大值", data.max())
    print("總和", data.sum())
    print("標準差", data.std())
    print("中位數", data.median())
    print("最大的3個數", data.nlargest(3))

    # 字串運算: 基本, 串接, 搜尋, 取代
    data=pd.Series(["您好", "Python", "Pandas"])
    print(data.str.lower()) # 改小寫
    print(data.str.len()) # 字串長度
    print(data.str.cat(sep=",")) # 字串串接 自訂separator
    print(data.str.contains("P")) # 字串是否包含 "P"
    print(data.str.replace("您好", "Hello")) # 字串是否包含
# Series_handle()
def DataFrame_handle():
    # 資料索引
    data=pd.DataFrame({
        "name":["Amy", "Henry", "Bob"],
        "salary":[30000, 50000, 40000]
    }, index=["a", "b", "c"])
    print(data)
    # 觀察資料
    print("資料數量", data.size)
    print("資料形狀 (欄,列)", data.shape)
    print("資料索引", data.index)

    # 取得列 (row) 的 Series 資料: 根據順序, 根據索引
    print("取得第2列", data.iloc[1], sep="\n")
    print("取得第c列", data.loc["c"], sep="\n") # 沒有i 

    # 取得欄 (column) 的 Series 資料: 根據欄位名稱
    print("取得 name 欄", data["name"], sep="\n")

    # 得到的資料是 Series
    names=data["name"]
    print("把 name 轉大寫", names.str.upper(), sep="\n")

    # 取得薪水的平均值
    salaries=data["salary"]
    print("薪水的平均值", salaries.mean())
    
    # 建立新欄位
    data["revenue"]=[500000, 400000, 300000]
    data["rank"]=pd.Series([3, 6, 1], index=["a", "b", "c"])
    
    # 操作原欄位 >新欄位
    data["cp"]=data["revenue"]/data["salary"]
    print(data)
# DataFrame_handle()
def Series_filter():
    # 篩選練習 Series 數字
    data=pd.Series([30, 15, 20])
    # condition=[True, False, True]
    condition=data>18
    print(condition)
    filteredData=data[condition]
    print("數字", filteredData, sep="\n")
    
    # 篩選練習 Series 字串
    data=pd.Series(["您好", "Python", "Pandas"])
    # condition=[False, True, True]
    condition=data.str.contains("P")
    filteredData=data[condition]
    print("字串", filteredData, sep="\n")
# Series_filter()
def DataFrame_filter():
    data=pd.DataFrame({
        "name":["Amy", "Henry", "Bob"],
        "salary":[30000, 50000, 40000]
    })
    print(data)
    # condition=[True, False, True]
    condition=data["salary"]>=40000
    filteredData=data[condition]
    print(filteredData)
DataFrame_filter()