# Egg文件打包与运行

本说明介绍 Python 项目打包为 Egg 文件流程和运行说明。

## 打包

指定 `project_folder` 和 `project_name`，其中后者相当于 Python 的一个 module。

如:

```
project_folder = './projects/demo1'
project_name = 'hello'
```

其中 hello 这个 module 里面需要包含 `__init__.py`，作为入口。

然后里面可以定义一个规范，例如 run() 方法作为入口，启动整个项目。

运行脚本为 build.py，修改里面的配置即可。

打包：

```
python3 build.py
```

这样会生成一个 `dist/hello-1.0-py3.6.egg` 文件。

这样就成功构建了。

可以把 Egg 文件分发到各处。

## 运行

运行可以直接使用 importlib 和 sys 库加载环境变量和动态引入 Egg 文件。

然后直接运行其 run() 方法即可。

当然也可以使用 `subprocess` 以命令行形式启动，效果类似，不过个人更推荐第一种。

