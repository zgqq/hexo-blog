---
title: why-a-method-should-do-a-thing
date: 2017-03-08 08:50:59
tags:
---

相信很多朋友跟我一样，刚开始学编程的时候，经常听到一句话就是方法代码行数要少，但是却无法理解为什么要少，我明明一个方法可以搞定的事，搞要那么多方法干嘛
# 优点
代码片段如下

    public void enterRoomBlockIfInBlocklist(Long userId){
        boolean inBlocklist = false;
        for (Long blockId:blockIds){
        if (lockId.equals(userId)) {
                inBlockList = true;
                break;
            }
        }
        if (inBlockList) {
            System.out.println("Blocked");
        } else {
            System.out.println("Entering room");
        }
    }

这个方法做了两件事，一个就是判断是否在黑名单内，另外一个就是做出相应的动作，但是判断是否在黑名单内似乎不能很快看出来，把代码改成

    public void enterRoomBlockIfInBlocklist(Long userId){
        if (isInBlockList(userId)) {
            System.out.println("Blocked");
        } else {
            System.out.println("Entering room");
        }
    }
    
    public void isInBlockList(Long userId) {
        for (Long blockId:blockIds){
        if (lockId.equals(userId)) {
                return true;
            }
        }
        return false;
    }

经过修改后的代码有如下的优点
## 自解释
isInBlockList 被抽取出来后，别人读代码，只要看到方法名就知道做了什么事，代码相当注释，代码的可读性大大提高

## 可测试
小方法比较容易测试，因为它基本不依赖其它组件，这些小方法就是组件，大方法就是成品，你把小方法测试好了，大方法还会出问题吗？ 这就是为什么web程序要分层的原因，想象一下，如果从接受请求到入库都在一个方法，如果是java写的，估计你一天都在重启了，也不必要抱怨java的重启，目前解决的方法有很多
* 老老实实分层，然后写单元测试
* 使用springboot，机器性能好点是很爽的
* 使用jrebel，一个热部署插件，不过要rmb

## 总结
Best practice就是把方法写小，然后单元测试用起来，才是王道


