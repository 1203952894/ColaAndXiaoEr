# python入门

> author: Cola
> Time :  2022.7.21

**声明：**  

- 该文档采用的 python 版本为 3.10.0a3
![python](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815132437.png)
- pycharm 版本为 2021.1.3 专业版

**目录结构：**  

> - Python介绍
> - 编辑器与解释器
> - Python 的安装与使用
> - PiP 的安装与使用
> - Pycharm 的安装与使用

## Python 介绍

**目录结构：**  
  
> - python 的来源
> - python 的特点
> - python 的应用方向
> - python 之禅

- **Python 的来源：**

> Python 是一门流行的编程语言。它由 Guido van Rossum 创建，于 1991 年发布。

- **Python 的特点：**

> - 简单易学、明确优雅、开发速度快
> - 跨平台、可移植、可扩展、交互式、解释型、面向对象的动态语言
> - “内置电池”，大量的标准库和第三方库
> - 开源语言,社区活跃，贡献者多，发展动力巨大

- **Python 的应用方向：**

> - 可以在服务器上使用 Python 来创建 Web 应用程序。
> - Python 可以与软件一起使用来创建工作流。
> - Python 可以连接到数据库系统。它还可以读取和修改文件。
> - Python 可用于处理大数据并执行复杂的数学运算。
> - Python 可用于快速原型设计，也可用于生产就绪的软件开发。


![Python 的应用方向](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815141910.png)

- **python 之禅：**

> 在安装好 python 的情况下 
> 1. 在命令行模式输入 python进入交互环境
> 2. 输入 import this

![python 之禅](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815142423.png)

## 编辑器与解释器

**目录结构：**  
      
> - 编译器与解释器的来源
> - 编译器与解释器的区别
> - Python 的运行机制

- **编译器与解释器的来源：**

> 为什么会有编译器/解释器？  

![为什么会有编译器/解释器？](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815143024.png)  

**编译器/解释器：** 高级语言与机器之间的翻译,都是将代码翻译成机器可以执行的二进制机器码，只不过在运行原理和翻译过程
有不同而已.  

- **编译器与解释器的区别：**

> 编译器：先整体编译再执行
> 解释器：边解释边执行  

![编译器与解释器的区别](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815143210.png)  

**编译方式：**运行速度快，但任何一个小改动都需要整体重新编译。可脱离编译环境运行。**代表语言是C语言**
**解释方式：**运行速度慢，但部分改动不需要整体重新编译。不可脱离解释器环境运行。**代表语言是Python语言**  

- **Python 的运行机制：**  

>  首先将.py文件编译成字节码，存储在.pyc文件中（该字节码在虚拟机上运行非cpu）。当python程序第二次运行时，首先程序会在硬盘中寻找.pyc文件，如果找到直接运行，否则重复上述过程。


![Python 的运行机制](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815143428.png)


## Python 的安装与使用

**目录结构：**    

> - Python 的安装
> - Python 的使用

- **Python 的安装：**

[python 官网](https://www.python.org/)
[python 文档地址](https://www.python.org/doc/)  

> **建议：** 采用 Python3 根据官方解释：Python 3 is strongly recommended for any new development. As of January 2020, Python 2 has reached End Of Life status.
> **来源：** [来源](https://wiki.python.org/moin/Python)

1. 进入官网  选取对应自己操作系统的 Python 进行下载

![进入官网](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815144305.png)

2. 直接选取安装程序.exe而不是嵌入式的.zip(方便安装)

![安装程序.exe](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815144449.png)

3. 添加 Python 到环境变量  

![添加 Python 到环境变量 ](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815144601.png)

4. 打开命令行输入 python -V 确认

![确认安装](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815144658.png)

5. 如果出现未识别的命令自行检查环境变量



- **Python 的使用：**

> Python 是一门解释型编程语言，这意味着作为开发人员，您可以在文本编辑器中编写 Python（.py）文件，然后将这些文件放入 python 解释器中执行。

**在命令行中运行python文件的方式如下：**
> python 文件名

![helloworld](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815184047.png)  

![helloworld.py](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815184138.png)  

## PiP 的安装与使用  

**目录结构：**    

> - PiP 的安装
> - PiP 的使用

> **pypi仓库**我们都知道 python 有很多的第三方库或者说是模块。这些库针对不同的应用，发挥不同的作用。我们在实际的项目中肯定会用到这些模块。那如何将这些模块导入到自己的项目中呢?Python 官方的 PyPi 仓库为我们提供了一个统一的代码托管仓库，所有的第三方库，甚至你自己写的开源模块，都可以发布到这里，让全世界的人分享下载.


- **PiP 的安装：**

![PiP 的安装](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815184627.png)
> 在 Python3.4 之后，我们都使用 pip 对 pypi 仓库当中的第三方库进行安装、卸载、更新等操作的命令。


- **PiP 的使用：**

```python
    # 普通安装
    pip install xlwt
    #指定版本安装
    pip install pygame==1.9.6
    # 卸载已安装的库
    pip uninstall xlwt
    # 列出所有已安装的库
    pip list
```

> wheel安装介绍与实现：
> 除了使用上面的方式联网进行安装外，还可以将安装包也就是 wheel 格式的文件，下载到本地，然后使用 pip 进行安装。比如我在 PYPI 上提前下载的 pygame 库的 wheel 文件，后缀名为 whl

1. pip install wheel 安装 wheel 这个库
2. 打开[仓库]( https://www.lfd.uci.edu/~gohlke/pythonlibs)
3.  下载相应库的 .whl 文件
4.  在 dos 命令行安装 pip install ***path.whl

> 换源安装介绍与实现：


- **介绍：**

> 可通过 pip config list 查看当前镜像源

![ 换源安装](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815185134.png) 

1. [阿里云](http://mirrors.aliyun.com/pypi/simple/)
2. [中国科技大学](https://mirrors.bfsu.edu.cn/pypi/web/simple/)
3. [豆瓣(douban)](http://pypi.doubanio.com/simple/)
4. [清华大学](https://pypi.tuna.tsinghua.edu.cn/simple/)
5. [中国科学技术大学](https://mirrors.bfsu.edu.cn/pypi/web/simple/)

- **实现：**

1. 临时修改

> pip install requests -i http://pypi.douban.com/simple  

2. 永久修改  
    1. 点击此电脑，在最上面的的文件夹窗口输入 ： %APPDATA% 
    2. 按回车跳转到以下目录，新建 pip 文件夹
    3. .创建 pip.ini 文件
    4. 打开文件夹，输入以下内容，关闭即可（注意：源镜像可替换)

![永久修改](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815192524.png)

```python
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```

## Pycharm 的安装与使用  

**目录结构：**    

> - Pycharm 的安装
> - Pycharm 的使用

- **Pycharm 的安装：**

> PyCharm 是由 JetBrains 公司打造的一款 Python IDE，支持 Windows、Linux、macOS 系统。[下载地址](https://www.jetbrains.com/pycharm/download/#section=windows)  

![Pycharm 的安装](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815191613.png)

- **Pycharm 的使用：**

1. 配置环境

![配置环境](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815191903.png)

![选择对应python](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815192023.png)

2. 选择项目位置
   
![选择项目位置](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220815192112.png)



