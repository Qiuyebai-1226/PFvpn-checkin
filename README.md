# PFvpn-checkin
用于PFvpn自动签到，适用于nonebot2

### 由于官网加了五秒盾，直接请求方式失效，故采用playwright进行签到

- 新增异步协程版，可进行多账号签到，如使用nonebot需修改`init.py`中发送图片名称，添加签到账号前三位，如将`result.png`修改为`result978.png`

### 12月11日更新   
网站在五秒盾之后又加了一个随机出现的验证码，并且频繁访问会被暂时ban掉   
可以通过[ddddocr](https://github.com/sml2h3/ddddocr)进行打码验证，但验证码不是每次都出现，并且验证码识别准确度堪忧，测试后会有小概率无法通过，新脚本暂时不更新了（主要是菜）

------

<font size="30" color="lightblue">脚本可以使用，稳定性未知，代码很烂，能跑就行</font>

------

# 使用方式

首先安装playwright

```python
pip install playwright
python -m playwright install
```

修改**checkin.py** 中要进行签到的账号和密码

linux无图形界面需要将第七行代码`headless=False`改为`headless=True` 

- 非nonebot使用  

  直接使用checkin.py文件即可，自行设置定时任务


- GitHub action使用  
  fork本项目，在`secrets`中添加`USERS`和`PWDS`两个变量，不同账号使用`;`隔开，自行修改定时运行时间。
  未充分测试，且结果无反馈，请自行测试。

- nonebot使用

  将**checkin.py**文件放在bot根目录，nonebot_plugin_PFvpn_checkin文件夹放置在src/plugins文件夹中，按注释修改**init.py**文件即可

  脚本会定时执行，也可手动进行签到，签到完成后会将页面截图发送给设定的QQ

  ![截图](截图.png)

![网页截图](网页截图.png)
