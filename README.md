# TestProject
#### 功能：
> 基于python，selenium，uiautomator的ui自动化工具，只需要通过编写特定格式的yaml文件实现web和android自动化操作
#### 环境准备：
- 安装配置python环境
> windows: https://zhuanlan.zhihu.com/p/344887837
- 安装相应python第三方模块
> pip install -r requirements.txt
#### 代码导读：
- Driver
> 存放chrome驱动位置，请下载自己对应浏览器版本的驱动
- TestCasepy
> python解析脚本位置，解析对应的yaml文件，执行对应的自动化操作
- TestCaseYaml
> yaml脚本位置，在yaml脚本中可以定义需要执行的操作，配置是否使用定时任务
- Run.py
> 在此处实例化对象，指定需要运行的脚本
