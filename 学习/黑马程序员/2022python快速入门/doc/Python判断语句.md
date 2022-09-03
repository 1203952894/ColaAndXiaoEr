# Python 判断语句

> author : Cola
> Time : 2022.8.20
> To : 学习 Python 中判断语句的用法 

> 进行逻辑判断，是生活中常见的行为。同样在程序中，进行逻辑判断也是最为基础的功能

**目录结构：**

> - 布尔类型和比较运算符
>
>   - 布尔类型用于表示：真和假
>   - 比较运算符用于计算：真和假
> - if 语句的基本格式
>
>   - 逻辑判断语句中 if 的基本格式
>   - 布尔类型数据在判断语句中的作用
> - if else 语句
>
>   - if else 语句的组合用法
> - if elif else 语句
>
>   - 用 if elif else 语句进行多条件判断
> - 判断语句的嵌套
> - 猜数字案例

## 布尔类型和比较运算符

### 布尔类型用于表示：真和假

> 在程序中我们通过布尔类型来描述真和假，用其表示现实生活的逻辑
>
> - True 表示真
> - False 表示假
>
> 注意： True 本质上是一个数字记作 1 False 记作 0
>
> 布尔类型的定义： 变量名称 = 布尔类型字面量
>
> 布尔类型不仅可以通过自行定义得到还可以通过计算的方式获取，即使用比较运算符得到布尔类型的结果

```python
result = 10 > 5 	# 可以通过比较运算符得到布尔类型数据
print (f"10 > 5 的结果是：{result} 类型为：{type(result)}")
```



### 比较运算符用于计算：真和假


<img src="https://raw.githubusercontent.com/1203952894/macminiPicGo/main/20220820160923.png"/>


## if 语句的基本格式

### 逻辑判断语句中 if 的基本格式

```python
age = input ("请输入年龄")
if int(age) > 18:	# Python 通过缩进判断代码块的归属方式
	print ("成年")
print ("光阴似箭，柠月如风 ～") 
```

### 布尔类型数据在判断语句中的作用

> 判断语句的结果  True 会执行 if 内的代码语句 False 不会执行

## if else 语句

### if else 语句的组合用法

> 上面我们通过 if 来执行满足条件的代码 在 python 中我们可以通过 else 来执行不满足条件的代码

```python
age = input ("请输入年龄")
if int(age) > 18:
	print (“成年")
else:					# else 不需要判断条件且同 if一样 else 代码块也需要缩进
	print ("输入格式有误或未成年")
```

## if elif else 语句

### 用 if elif  esle 语句进行多条件判断

> 某些场景下，判断条件不止一个可能存在多个点情况，python 为我们提供了 elif 语句来满足多条件判断

```python
height = input ("请输入你的身高：")
if int(height) > 180:
	print ("你好高")
elif int(height) > 160:
	print ("不错哦")
else:
	print (“输入格式有误或低")
```

## 判断语句的嵌套

> 有的时候，不仅仅需要多个并列条件 还要满足前置条件才会二次判断的多层需求 我们可以通过 嵌套来实现

```python
age = input ("请输入年龄：")
if int(age) > 18:
	vip_num = int(input("请输入会员等级："))
	if vip_num >= 3:
	print (f"欢迎您尊贵的svip {vip_num} 超级会员")
	elif vip_num < 3:
	printf (f"欢迎您尊敬vip {vip_num} 普通会员")
	else:
	print ("会员输入格式有误")
else:
	print ("您还未成年")

```

## 猜数字案例 

> 随机产生一个（1-10）范围内的数字通过判断进行猜数字
>
> 如果没猜中 提示 猜大或猜小了

```python
import random  # 导入 random 模块用于生成随机数字

guess_num = random.randint(1, 10)  # 随机产生（1-10）范围内的数字
user_num = int(input("请输入你猜的数字(1-10)："))

while guess_num  != user_num:
    if guess_num <  user_num:
        print("猜大了")
        user_num = int(input("再试一次："))
    elif guess_num > user_num:
        print("猜小了")
        user_num = int(input("再试一次："))
    else:
        print("输入格式有误")

print(f"猜对了 guess_num = {guess_num}")

```
