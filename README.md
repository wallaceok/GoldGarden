# GoldGarden

介绍：
  GoldGarden基于appium 进行了简单的二次封装，比appium所提供的方法操作更简洁。

  它包含功能:
  * 本框架只是对appium原生方法进行了简单的封装，，这些方法基本能够胜任于我们的移动自动化测试。
  * unittest单元测试框架运行测试
  * HTMLTestRunner生成测试报告
  * 数据驱动、以及对数据库、文件等操作方法
  * log日志的生成、对错误日志及时传送至微信端口
  * 支持并能够胜任monkey的一些测试
  * 采用po模式进行元素分离，对界面操作就行简单的封装

安装：
  * python3.6.6
  * jdk1.8.0
  * android-sdk_r24.3.4-windows
  * appium：1.4.13.1
  * Node.js：node-v4.4.7-x64
  * .net framework4.5
  * Appium-Python-Client
  * pymysql
  * xlrd
  * configparser


***GoldGarden V0.0.3***
  * 优化原HTMLTestRunner报告
  * Base_Page加入一组list随机点击方法
  * 新增发送邮件功能


