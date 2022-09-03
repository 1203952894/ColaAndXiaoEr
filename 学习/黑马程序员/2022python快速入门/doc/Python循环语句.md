# Python 循环语句

> author : Cola
> Time : 2022.8.20
> To : 学习 Python 中的循环语句

> 循环普遍存在于日常生活中同样循环也是程序中很重要的一个功能例如：轮播图等都是通过循环实现的

**目录结构：**

> - while 循环的基础语法
>   - while 循环的基础应用
> - while 循环的基础案例
> - while 循环的嵌套应用
>   - while 循环嵌套的基本格式
>   - while 循环嵌套的应用
>   - 使用 while 循环的嵌套打印九九乘法表
> - for 循环的基础语法
>   - 基础语法
>   - range 语句
>   - 变量作用域
> - for 循环嵌套应用
> - 循环中断：break和continue

## while 循环的基础语法

### while 循环的基础应用

> while 循环 的语法格式：
>
> while 条件：
>
> 条件满足时，事件1
>
> 条件满足时，事件2
>
> ......
>
> 注意事项：
>
> - 条件需提供布尔类型，True代表继续 False 表示结束
> - 空格缩进
> - 规划好终止条件否则无限循环

```python
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(f"1-100的和为 {sum}")
```

## while 循环的基础案例

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

## while 循环的嵌套应用

### while 循环嵌套的基本格式

> while 循环嵌套的语法格式：
>
> while 条件1：
>
> 条件1满足时，事件1
>
> 条件1满足时，事件2
>
> ......
>
>     while 条件2：
>
>     条件2满足时，事件1
>
>     条件2满足时，事件2
>
>     ......
>
> 注意事项：
>
> - 注意条件控制，避免无限循环
> - 多层嵌套需要注意缩进

### while 循环嵌套的应用

### 使用 while 循环打印九九乘法表

> print 语句默认输出内容会自动换行 这是因为默认的 end = "\\n" 如果不想换行只需将其换为 end = " "
>
> 制表符： \t 可以让多行字符串进行对齐

```python
row = 1  # 定义外层控制变量
while row <= 9:
    count = 1  # 定义内层控制变量
    while count <= row:
        print(f"{count} * {row} = {count * row}\t", end=" ")
        count += 1
    row += 1
    print()

```

## for 循环的基础语法

### 基础语法

> for 循环的语法格式：
>
> for 临时变量 in 待处理的数据集:
>
> 满足条件时执行的代码
>
> 注意：
>
> - for 循环和 while 循环功能相近但 while 循环的循环条件时自定义的而for循环是**轮询**即对内容进行逐个处理具体流程为从待处理的数据集中逐个取出数据赋值给临时变量因此for循环也被称之为遍历循环
> - for 循环无法定义循环条件，只能被动取出数据进行处理因此for循环一般不存在无限循环因为被处理的数据集不可能无限大
> - 注意缩进

```python
name = "ColaAndXiaoEr"
count = 0   # 计数器
for char in name:
    if char ==  "o":
        count += 1
print(f"字符串{name}中有 {count} 个字符 o ")
```

### range语句

> 上述 for 循环语法中的 待处理数据集严格来说应称之为：**可迭代类型 即其内容可以一个个依次取出的一种类型如：**
>
> - 字符串
> - 列表
> - 元组
>
> range 语句的功能：获得一个数字序列（可迭代类型的一种）
>
> range 语句的格式：
>
> - range (num)
> - range (num1 , num2)
> - range (num1, num2 ,step)
>
> 注意：
>
> - 默认从 0 开始，左闭右开

```python
count = 0
for i in range(1,100):
    if i % 2 == 0:
        count += 1
print(f"1-100 中有{count}个偶数")

```

### 变量作用域

> 上述 for 循环中的临时变量其作用域限定为循环内，这种限定
>
> - 是编程规范的限定而非语法格式上的强制限定
> - 不遵守也可以运行（在 for 循环外也可以访问）但不建议
> - 如果想要访问 建议在 for 循环外定义

## for 循环 嵌套应用 

> 同 while 循环，for 循环也是支持嵌套的 而且 两者可以配合使用

```python
for row in range(1, 10):    # 定义外层控制变量
    for count in range(1, 10):
        if count <= row:
            print(f"{count} * {row} = {count * row}\t", end=" ")
    print()



```

## 循环中断：break和continue

> 无论是 while 循环还是 for 循环都是重复性的 执行特定操作，在此过程中会出现一些情况让我们不得不：
>
> - 跳出某次循环 执行下一次（continue）
> - 提前退出循环 不再执行 （break）
>
> 注意：
>
> - continue 和 break 在 for 循环和 while 循环中作用一致
> - 当用于嵌套循环时，单个 continue 或 break 仅能作用于当前所在循环

```python
"""
某公司，账户余额有1W元，给20名员工发工资。
员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
如果工资发完了，结束发工资。
"""
import random

money = 10000
for num in range(1, 21):
    source = random.randint(1, 10)  # 绩效
    if source < 5:
        print(f"员工{num}本月的绩效成绩为{source}小于 5 不发工资")
        continue
    elif money >= 1000:
        print(f"员工{num}本月的绩效成绩为{source}大于 5 发 1000")
        money -= 1000
        print(f"账户剩余余额为：{money}")
    else:
        print(f"账户剩余余额为：{money}")
        break

```
