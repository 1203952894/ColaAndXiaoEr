## 错误001 网络问题

> 2022.8.9 在连接github仓库时遇到一个报错：Failed to connect to github.com port 443 after 21024 ms: Timed out(大致：21024 ms后仍无法连接到github.com 端口为 443 超时)

**错误信息：443**
**错误原因：** 这样的问题通常是由于网络访问慢导致访问超时，这时候我们可以通过使用设置代理和取消代理的命令来解决
**设置代理：**

```java
git config --global https.proxy
```

**取消代理： sss**

```java
git config --global --unset https.proxy
```

**解决步骤：** 直接在git控制台先输入 设置代理命令 在输入取消代理命令即可解决(**或者使用 git init 命令初始化git**)

## 错误002 443端口连接拒绝

![](https://raw.githubusercontent.com/1203952894/macminiPicGo/main/20220818124720.png)

> export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:789
