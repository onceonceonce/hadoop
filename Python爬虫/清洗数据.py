import pandas as pd

df = pd.read_csv('北京平谷数据.csv', encoding='utf-8')
pd.set_option('display.max_columns', None)
df = df.fillna('无')  # 替换所有NaN
# 户型,楼层,面积,装修情况,价格,小区,区域,房屋朝向,配置电梯,挂牌时间,房屋用途
df.drop('房屋朝向', axis=1, inplace=True)
# 去除每一列的前后空格
columns_to_strip = ['户型', '楼层', '面积', '装修情况', '价格', '小区', '区域', '配置电梯', '挂牌时间', '房屋用途']
# 转换为字符串类型后再去除空格
df[columns_to_strip] = df[columns_to_strip].astype(str).apply(lambda x: x.str.strip())
# 进行其他的操作，比如替换\r\n
df.replace(r'\s+|\\n', ' ', regex=True, inplace=True)
df['面积'] = df['面积'].str.replace('平米', '', regex=False)  # 价格去掉平米
a = df.sort_values(by='价格', ascending=False).head(10)  # 按照某一个字段排序
df.to_csv('北京平谷数据处理之后.csv', index=False, encoding='utf_8_sig')
