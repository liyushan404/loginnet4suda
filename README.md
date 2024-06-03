# 苏大校园网自动登录脚本

> **本脚本适用于Linux系统**

1. 下载或复制脚本到本地
2. 在`login.py`文件中修改用户名和密码设置，其中用户名后跟随运营商的英文缩写
3. 为shell脚本添加运行权限`sudo chmod +x check_network.sh`
4. 使用linux中的crontab实现定时任务，在每天早上6点运行脚本

    `crontab -e` 选3进入vim界面

    `0 6 * * * /path/to/check_network.sh`。 其中`/path/to/check_network.sh`是你本地shell脚本的路径
6. 检查cron任务创建以及状态
 
    `sudo service cron status`

     `crontab -l`

