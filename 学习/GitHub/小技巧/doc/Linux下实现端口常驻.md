

# Linux 下实现端口常驻

> author: Cola
> Time :2022.9.3 23.16 PM
> To : 解决 hexo 退出ssl后自动断开问题

**目录结构：**

> - 常用端口命令
> - 实现
>   - 安装 pm2
>   - 编写js脚本文件
>   - 在根目录下运行脚本文件

## 常用端口命令

列出所有端口

```cmake
netstat -ntlp
```

杀死某个端口(以4000 端口为例)

```cmake
lsof -i :4000|grep -v "PID"|awk '{print "kill -9",$2}'|sh

```

## 实现

安装 pm2

```cmake
sudo npm  install -g pm2
```

在博客根目录下面创建一个 **hexo_run.js**

```cmake
//run
const { exec } = require('child_process')
exec('hexo server -p 80',(error, stdout, stderr) => {
        if(error){
                console.log('exec error: ${error}')
                return
        }
        console.log('stdout: ${stdout}');
        console.log('stderr: ${stderr}');
})
```

在根目录下,运行脚本

```cmake
pm2 start hexo_run.js
```
