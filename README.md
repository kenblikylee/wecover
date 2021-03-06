# wecover

[![Build Status](https://travis-ci.org/kenblikylee/wecover.svg?branch=master)](https://travis-ci.org/kenblikylee/wecover)
[![license](https://img.shields.io/github/license/kenblikylee/wecover)](https://github.com/kenblikylee/wecover/blob/master/LICENSE)

微信公众号图文封面快速制作工具。一张`logo.png`或网络图片地址，一个标题，一行命令，一键生成微信图文封面，还可以任意改变颜色。

![](http://cdn.kenblog.top/wecover_example.png)

## 安装

``` sh
pip install wecover
```

*如果使用国内镜像(如清华的)，未及时同步，请切换官方镜像：*

``` sh
pip install --index-url https://pypi.org/simple wecover
```

如果已经安装，可更新到最新版：

``` sh
pip install --upgrade wecover
```

## 使用

### 命令行格式

``` sh
wecover <title> [logo_path|logo_url]

wecover --title|-t <title> [--logo|-l <logo_path|logo_url>]
```

LOGO可选。如果当前文件夹存在名为 `logo.png` , `logo.jpg`, `logo.jpeg` 任意一张图片文件，可以不提供 logo 参数，会自动读取其中一张图片作为 LOGO 。

### 基本使用

``` sh
wecover 微信图文封面制作工具
wecover 微信图文封面制作工具 logo.png
wecover 微信图文封面制作工具 "http://cdn.kenblog.top/weixin.jpeg"
wecover --logo logo.png --title "wecover 微信图文封面制作工具"
wecover -l logo.png -t "wecover 微信图文封面制作工具"
```

![](http://cdn.kenblog.top/wecover1.jpg)

### 改变颜色

#### 改变字体颜色

``` sh
wecover <title> [logo_path|logo_url] --color|-c <color>

wecover <title> <logo_path|logo_url> <color>
```

#### 改变背景色

``` sh
wecover <title> [logo_path|logo_url] --bgcolor|-b <color>

wecover <title> <logo_path|logo_url> <color> <bgcolor>
```

#### 示例：生成黑底白字

``` sh
wecover 微信图文封面制作工具 "http://cdn.kenblog.top/weixin.jpeg" white black
# 或使用十六进制颜色值，颜色引号不能省略
wecover 微信图文封面制作工具 "http://cdn.kenblog.top/weixin.jpeg" "#ffffff" "#000000"
# 支持颜色缩写
wecover 微信图文封面制作工具 "http://cdn.kenblog.top/weixin.jpeg" "#fff" "#000"
```

![](http://cdn.kenblog.top/wecover2.jpg)

## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2019 kenblikylee
