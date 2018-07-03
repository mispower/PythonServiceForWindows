# encoding=utf-8
import os
import win32event
import win32service

import win32serviceutil


class PyService4Win(win32serviceutil.ServiceFramework):
    # 服务名
    _svc_name_ = "FlumeService"
    # 服务在windows系统中显示的名称
    _svc_display_name_ = "FlumeService"
    # 服务的描述
    _svc_description_ = "flume消费程序"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.run = True

    def SvcDoRun(self):
        # 实践在某些系统下找不到环境变量，可以用绝对路径访问
        command = "%FLUME_HOME%\\bin\\flume-ng agent -name myflume -f %FLUME_HOME%\\conf\\myflume.conf -property 'flume.root.logger=INFO,LOGFILE,console'"

        result = os.popen(command)

        self.logger.info(result.read())
        # 等待服务被停止
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def SvcStop(self):
        # 先告诉SCM停止这个过程
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # 设置事件
        win32event.SetEvent(self.hWaitStop)
        self.run = False


if __name__ == '__main__':
    # 括号里参数可以改成其他名字，但是必须与class类名一致；
    win32serviceutil.HandleCommandLine(PyService4Win)
