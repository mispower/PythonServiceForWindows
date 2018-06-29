# 基于python创建windows服务

## 描述

基于业务需求，用到基于windows下的flume服务消费日志数据，利用python将flume启动脚本做成windows随机启动服务。

## 环境准备
-	本程序基于python调用flume启动脚本，是故需要python、jdk1.7+、flume等组件。
-	python调用windows服务，所以依赖pywin32包：pyhton -m pip install pywin32
git


