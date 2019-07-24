# AirMemo
tips for desktop

### reach
&ensp;&ensp;1.快速记录

&ensp;&ensp;2.发送邮件

&ensp;&ensp;3.配置提醒时间和邮箱

&ensp;&ensp;4.完成回收站功能

&ensp;&ensp;5.版面滚动，固定高度(根据实际场景,限制高度,没有滚动)

&ensp;&ensp;6.单端避免重复打开

### to do
&ensp;&ensp;1.多邮箱自动分割(参考foxmail)

&ensp;&ensp;2.动态布局(已完成)

&ensp;&ensp;3.云同步

&ensp;&ensp;4.异地登录问题，仅允许单端登录

&ensp;&ensp;5.db文件加密

&ensp;&ensp;6.右键菜单时间个数问题

&ensp;&ensp;7.优先级增加

### question

&ensp;&ensp;1.目前最大的问题是id的获取在对象名字中获取的

&ensp;&ensp;2.缺一个美工[捂脸]

未登录的账号是没有token在服务端（登出时token置null）
1、A 登录 账号Joe
账号joe 有token
2、B 登录 账号Joe(无效登录)
    Ser主动发送验证码到用户邮箱
    前端出现验证码输入框登录
    带正确验证码登录，成功登录，更新token
    
    
验证码有效期30分钟
