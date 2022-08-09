# 使用 GitHub + picGo 搭建图床

## 1. 概述

**什么是图床:**  

>图床指的是存储图片的服务器  

**为什么使用图床：**  

> 1. 使用图床可以方便对图片的统一处理  
  2. 不存在因电脑硬盘损坏导致图片丢失的问题
  3. 使用Typora等MarkDown文档编写也会很方便
  
## 2. 搭建步骤  

### 2.1 配置 GitHub  

- 首先你需要一个GitHub账号 **注册地址:**[GitHub](https://github.com/)  
- 注册好后登录，然后单机右上角 ➕ 处 创建一个新仓库用于存储图片
  ![新建仓库](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220809154418.png)  
- 填写仓库名和描述(仓库名必须是public的否则存储的图片不能正常访问)
  ![描述信息](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220809154826.png)
- 生成一个token(令牌),用于后续picGo访问GitHub  
 ![主页token入口](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220809155102.png)  
 ![token](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220809155144.png)
 **注意：** 此处token只会在此处出现注意保存
  
### 2.2 下载picGo

- 访问[picGo官网](https://github.com/Molunerfinn/PicGo/releases)根据自己系统选择对应版本下载安装  
- 配置picGo  
  ![picGo](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220809155438.png)  

  > 1. 此处仓库名即为 刚才设置的名称 (标准格式为 用户名/仓库名)
    2. 分支名为 main (GitHub的分支名)
    3. token （刚才生成的token）
    4. 存储路径 （默认为 img/ 即可）
    5. 自定义域名 （即为上传成功后生成的url 标准格式为 https://raw.githubusercontent.com/用户名/仓库名/分支名）    
   
- 设置上传快捷键 
  ![快捷键](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220809155942.png)


### 2.3 配置Typora

- 配置图片上传服务
  ![图片上传服务](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220809160102.png)


## 测试  

- 截取图片后 使用快捷键进行上传 
  ![](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220809160334.png)
- 成功后即可获得该图片的 url 直接粘贴即可
  ![](https://raw.githubusercontent.com/1203952894/cloudimg/main/20220809160504.png)