GoldGarden

介绍：

GoldGarden基于appium 进行了简单的二次封装，比appium所提供的方法操作更简洁。

特点：

1.支持并能够胜任monkey的一些测试、
2.log日志的生成、
3.对错误日志及时传送至微信端口
4.数据驱动、以及对数据库、文件等操作方法
5.本框架只是对appium原生方法进行了简单的封装，，这些方法基本能够胜任于我们的移动自动化测试。
6.采用po模式进行元素分离，对界面操作就行简单的封装
7.基于unittest单元测试框架，所以测试文件与测试方法遵循unittest开发。
8.自动生成HTML测试报告生成并发送邮件。

安装说明：

jdk1.8.0
android-sdk_r24.3.4-windows
python 3.6
appium：1.4.13.1
Node.js：node-v4.4.7-x64
.net framework4.5
Appium-Python-Client (pip安装)

Python库：pymysql、xlrd、configparser


appium启动时如何禁止安装Unlock、Setting：http://www.cnblogs.com/xiaoxiaolulu/p/7356488.html  （看完的别忘了加波关注并评论666）


CI持续集成：

tomcat 9.0.0.M4
jenkins 2.0

tomcat配置：https://jingyan.baidu.com/article/54b6b9c0dd0c6a2d593b4743.html
Jenkins war包放到webapps下
启动jenkins：先重启tomcat：startup.bat，然后在浏览器输入http://localhost:8080/jenkins/


