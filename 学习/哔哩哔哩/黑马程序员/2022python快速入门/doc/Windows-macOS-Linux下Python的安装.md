# Windows macOS Linux 下Python的安装

> author : Cola
>
> Time : 2022.5.21
>
> To : 不同操作系统下 Python 的安装

**目录结构：**

> - Windows 11 下的安装
> - macOS 10.15.7 下的安装
> - Linux(CentOS7) 下的安装



## Windows 11 下的安装

- [官网](https://www.python.org/downloads)
- 选取 msi 文件直接安装
- 无脑 next 后 进入 Terminal 中输入python 检验

## macOS 10.15.7 下的安装

- 下载 package 文件
- 无脑next
- 输入 python3 验证
- 因为 macOS 自带 python2 为了方便使用配置一下环境变量

> echo 'alias python=python3' >> .bash_profile

## Linux(CentenOS7) 下的安装

> 需要了解 yum、cd、wget、vi编辑器、软链接等Linux命令

- 安装依赖程序

> 使用 yum 程序对相关依赖进行安装  
>
> yum install wget zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make zlib zlib-devel libffi-devel -y

- 在官网找到相应的下载链接

> 使用 wget 命令进行下载. 
>
> cd ~
> wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz

- 解压刚才下载好的 tgz

> tar -xvf Python-3.10.4.tgz

- 切换目录到解压后的文件夹进行编译和配置

> 切换目录
>
> cd Python-3.10.4.  
>
> 配置. 
>
> ./configure --prefix=/usr/local/python3.10.4
>
> 编译
>
> make && make install

- 配置软链接

> 删除系统自带老版本的软链接
>
> rm -f /usr/bin/python
>
> 创建软链接
>
> ln -s /usr/local/python3.10.4/bin/python3.10 /usr/bin/python
>
> 创建软链接后，会破坏yum程序的正常使用（只能使用系统自带的python2）
>
> 修改
>
> /usr/bin/yum
> /usr/libexec/urlgrabber-ext-down
>
> 使用vi编辑器，将这2个文件的第一行，从
>
> !/usr/bin/python 修改为 !/usr/bin/python2

- 验证

> 在Linux系统命令行窗口内，直接执行：python 并回车：看到Python 3.10.4字样，即表明安装成功。
