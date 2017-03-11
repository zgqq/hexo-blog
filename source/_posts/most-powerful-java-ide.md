---
title: 打造最强的java ide
date: 2017-03-11 13:21:35
tags: Intellij IDEA
---
# Intellij IDEA
Intellij IDEA 是最好的java ide 没有之一

# 插件
## ideavim
ideavim 是一个模拟vim的插件，是Jetbrains产品最强的插件之一， 支持常用的vim的快捷键，近期更新了一个超神级feature，就是支持调用idea内置的action，编辑 ~/.ideavimrc，设置生成getter,setter,constructor等的快捷键

    nnoremap <Space>gc :action GenerateConstructor<CR>
    nnoremap <Space>gg :action GenerateGetter<CR>
    nnoremap <Space>gs :action GenerateSetter<CR>
    nnoremap <Space>ga :action GenerateGetterSetter<CR>
    nnoremap <Space>im :action ImplementMethods<CR>
    nnoremap <Space>dm :action DelegateMethods<CR>

重构，提取方法

    vnoremap <Space>em :<C-u>action ExtractMethod<CR>

格式化代码

    nnoremap <Space>rc :action ReformatCode<CR>

显示文件在项目结构 

    nnoremap <Space>pv :action SelectInProjectView<CR>

新增

    nnoremap <Space>nc :action NewClass<CR>
    nnoremap <Space>np :action NewProject<CR>

关闭tab 

    nnoremap <Space>ct :close<CR>
    nnoremap <Space>on :action CloseAllEditorsButActive<CR>

窗口操作

    nnoremap <Space>hw :action HideAllWindows<CR>
    nnoremap <Space>hs :action HideSideWindows<CR>
    nnoremap <Space>lw :action JumpToLastWindow<CR>
    nnoremap <Space>aw :action ActivateProjectToolWindow<CR>

## 快捷键
上面的快捷键虽然超级给力，但是也有无能为力的时候，脱离了编辑环境后，也就没办法使用上面的快捷键，可以分成两类快捷键，第一类就是依赖编辑环境，第二类就是全局快捷键
比如重命名某一个变量，就是依赖编辑环境环境的，所以把它设置为vim 的快捷键那是极好的，比如搜索一个类，有时候我们的光标会在项目结构上，就是脱离了编辑环境，还有即使在编辑环境内，因为vim的快捷键只能在command mode执行，所以把搜索类设置成全局快捷键还是极好的
