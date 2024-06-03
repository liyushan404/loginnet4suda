#!/bin/bash
# 检测网络连接状态的脚本

 SCRIPT_PATH="/home/lrr/Documents/suda/Network_Connection/login.py"
    
# 检测网络是否连接
ping -c 4 www.baidu.com > /dev/null 2>&1

# 根据ping的结果设置返回值
if [ $? -eq 0 ]; then
    echo "Network is up"
else
    echo "Network is down"
    python $SCRIPT_PATH || echo "Python script failed"
fi
