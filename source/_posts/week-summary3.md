---
title: week-summary3
date: 2017-03-22 21:15:56
tags:
---

# Jstorm
上周被老大交待了一个任务，就是做一个日志分析系统，刚开始他叫我做一个kafka的消费者然后统计一下就行，后来不知道怎么说的，就谈到storm不错，以前只是听过storm是一个实时计算框架，好像很难的样子，没有应用场景，所以我一直没学，我就去官网看了一下，我的天，这是什么鬼，什么topology,spout,bolt都完全懵逼的，好不容易搞得有点懂了，跟老大说了一下，因为他是阿里粉，所以说用jstorm吧，幸好jstorm 是兼容storm 的，然后就开始搞，我现在算是被jstorm 折腾出阴影来了，第一个折腾的地方就是启动，因为我的电脑默认是python3，而启动脚本是用python2写，加上又是后台启动没打印错误，浪费了一点时间，启动时会报错就是nimbus不支持localhost，你需要把你的hosts改成一下，改成局域网的ip即可，还有一个就是web ui，这也是个坑，不能安装在要root权限的目录下，不然在界面上什么都看不到，jstorm 还有一个天坑，不能使用下面的配置

        Properties conf = new Properties();
        conf.put("kafka.fetch.from.beginning", true);

要用字符串形式

        Properties conf = new Properties();
        conf.put("kafka.fetch.from.beginning", "true");

我特么也是醉，然后折腾了好久。。。
还有一个要注意的是spout和bolt都是用反序列化来生成的，所以构造方法不会被执行，要初始化可以在prepare中，我理解错了几次bolt和grouping，刚开始以为bolt是线程不安全的，直到我理解了task，还有一个就是，还有fieldsGrouping，因为最近要做一个日志分析系统，我用访问时间作为分组，这样相同的时间就会被分到相同的task，我居然担心内存泄露这种问题，真的醉了，我以为storm 实现fieldsGrouping是用一个map来实现的，如果是这样，以前的时间不可能被统计到，必定会内存泄露，还好后来在github问了个问题，一个哥们还打了电话过来，解决了我的问题，内部是取field的hash然后分流到对应的task，storm是无状态的
# Java
Java 有一个大坑，就是 Exception 只能捕获异常，不能捕获error，当然这个很基础，但是常常忘记，如果你的代码是放在Runnable然后提高线程池运行的，要小心了，最好用Throwable捕获，不然抛出错误，你的程序还是会悄无声息地跑下去
# Gradle
使用./gradlew idea 生成idea 的相关文件，如果idea 自动生成，可能无法把resources目录的东西放在classpath下
# Others 
* mybatis 不能使用 table 为方法的参数名，不然会报一些奇怪的错误
* maven 的provided 只要能用来编译，没有作为运行库，没有认真看文档的人小心了，不然要跟我一样杯具了
* mybatis 的 SelectProvider 一不小心会被sql注入
* apache common 有一个很方便的工具类就是RandomStringUtils用来测试还不错
* mybatis 的select可能会缓存，所以在测试的时候要小心缓存
* shadowsocks可以用polipo来转换成https

# 总结
storm中，worker是一个进程，一个worker里面可以有多个executor，也就是线程，每一个executor通常会执行一个task，task 是一个bolt 或spout 的实例，所以无论bolt还是spout都是线程安全的
