# 2022 Python快速入门

> author: Cola
> Time :2022.8.29 18.31 PM
> To : 学习 Python 基础知识

**目录结构：**

> - [你好 Python](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/%E4%BD%A0%E5%A5%BDPython.md)
> - [Pycharm 的安装与配置](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/Pycharm%20%E7%9A%84%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE.md)
> - [Python 函数](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/Python%E5%87%BD%E6%95%B0.md)
> - [Pythom 函数进阶](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/Python%E5%87%BD%E6%95%B0%E8%BF%9B%E9%98%B6.md)
> - [Python 基础语法](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/Python%E5%9F%BA%E7%A1%80%E8%AF%AD%E6%B3%95.md)
> - [Python 判断语句](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/Python%E5%88%A4%E6%96%AD%E8%AF%AD%E5%8F%A5.md)
> - [Python 数据容器](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/Python%E6%95%B0%E6%8D%AE%E5%AE%B9%E5%99%A8.md)
> - [Python 文件操作](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/Python%E6%96%87%E4%BB%B6%E6%93%8D%E4%BD%9C.md)
> - [Python 循环语句](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/Python%E5%BE%AA%E7%8E%AF%E8%AF%AD%E5%8F%A5.md)
> - [Python 异常模块和包](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/Python%E5%BC%82%E5%B8%B8%E6%A8%A1%E5%9D%97%E5%92%8C%E5%8C%85.md)
> - [各种操作系统下 Python的安装](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/Windows-macOS-Linux%E4%B8%8BPython%E7%9A%84%E5%AE%89%E8%A3%85.md)
> - [地图可视化](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/%E5%9C%B0%E5%9B%BE%E5%8F%AF%E8%A7%86%E5%8C%96.md)
> - [动态柱状图](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/%E5%8A%A8%E6%80%81%E6%9F%B1%E7%8A%B6%E5%9B%BE.md)
> - [折线图可视化](https://github.com/1203952894/ColaAndXiaoEr/blob/main/%E5%AD%A6%E4%B9%A0/%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98/2022python%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/doc/%E6%8A%98%E7%BA%BF%E5%9B%BE%E5%8F%AF%E8%A7%86%E5%8C%96.md)
