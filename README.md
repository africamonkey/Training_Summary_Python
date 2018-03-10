# ACM 训练总结系统

## 开发背景

中山大学 ACM 集训队目前正在使用原有的 ACM 训练总结系统（http://www.sysuteam.com）。这个系统能帮助郭嵩山教授、林瀚老师了解集训队的做题情况。然而，这个系统有一些不足之处，例如每支队伍没有自己的主页，队伍不能在上面写总结、发题解。

我参考了一下浙大的队伍主页，包含队伍信息、训练帐号、目标、友情链接、杂事杂项（一些小结和提醒）、板子整理、个人训练、团队训练、比赛记录等信息。他们的队伍主页支持 MarkDown 语法，并且有版本控制（即可以恢复到历史版本）。对于每场比赛，他们都有总结。我们决心做出跟浙大一样好的 ACM 训练总结系统。

## 项目成员

王凯祺

刘梓晖

田启睿

区炜彬

## 拟定功能

比赛的创建与管理

队伍管理

队伍主页（含版本控制），底部包含该队伍参与的所有比赛及总结

比赛列表，及该比赛下每支队的做题情况

## 实现方法

Web 应用框架：Django

数据库：Sqlite3

