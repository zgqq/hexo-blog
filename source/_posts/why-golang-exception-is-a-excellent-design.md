---
title: why-golang-exception-is-a-excellent-design
date: 2017-03-05 00:55:51
tags:
---
# 异常处理
以前我喜欢golang因为它的简洁，但是不喜欢它处理异常方式，加上快工作了，只能继续搞java，我越来越来觉得golang的异常处理方式简直就是一个天才般的设计，golang的异常是通过返回值实现的
在java中，很多人都会这样处理异常

    try {
        methodA()
        methodB();
    }catch (Exception e) {
        throw new RuntimeException(e);
    }

无论method,method2 抛出什么异常都用Exception 来捕获，其实这样做程序的健壮性是很差的，比如
methodA的异常是可恢复的，你直接抛出RuntimeException，程序就会直接挂掉，当然你可以这样做
 
     try {
        methodA();
     }catch (Exception e) {
        
     }
     try {
        methodB();
     } catch( Exception e){
     
     }


另外一种是

     try {
        methodA();
        methodB();
     }catch (AException e) {
        
     }catch (BException e){
        
     }

不过这种的局限性很大，需要方法抛出特有的异常

但是golang是这样处理的 

    value,err := methodA()
    if err != nil  {
    }

    value,err = methodB()
    if err != nil  {
    }

强制处理对应异常，程序就健壮得多了，而且代码优雅得多，其实golang 的error 可以期待了java的各种custom exception，因为custom exception 主要是让客户端更好的捕获异常，golang 通过返回值巧妙地实现了这个功能

# 总结
虽然 golang 有时 err != nil 确实烦，但是换来的程序健壮性，总体上利大于弊
