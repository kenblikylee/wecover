# wecover

[![Build Status](https://travis-ci.org/kenblikylee/wecover.svg?branch=master)](https://travis-ci.org/kenblikylee/wecover)
[![license](https://img.shields.io/github/license/kenblikylee/wecover)](https://github.com/kenblikylee/wecover/blob/master/LICENSE)

微信公众号图文封面快速制作工具。

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

### 基本使用

``` sh
wecover 微信图文封面制作工具
wecover 微信图文封面制作工具 logo.png
wecover 微信图文封面制作工具 "http://cdn.kenblog.top/weixin.jpeg"
wecover --logo logo.png --title "wecover 微信图文封面制作工具"
wecover -l logo.png -t "wecover 微信图文封面制作工具"
```

## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2019 kenblikylee
