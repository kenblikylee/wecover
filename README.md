# wecover

[![Build Status](https://travis-ci.org/kenblikylee/wecover.svg?branch=master)](https://travis-ci.org/kenblikylee/wecover)
[![license](https://img.shields.io/github/license/kenblikylee/wecover)](https://github.com/kenblikylee/wecover/blob/master/LICENSE)

微信公众号图文封面快速制作工具。

![](http://cdn.kenblog.top/wecover_example.png)

## 安装

``` sh
pip install wecover
```

如果已经安装，可更新到最新版：

``` sh
pip install --upgrade wecover
```

## 使用

### 基本使用

``` sh
wecover --logo logo.png --title "算法分析"
wecover -l logo.png -t "算法分析"
wecover logo.png 算法分析
```

### 改变标题和背景颜色

标题字体默认为黑色，背景为白色。如果需要改变默认颜色，需要用到选项 `--color/-c` 和 `--bgcolor/-b`。

``` sh
wecover logo.png "算法分析 (一)" --color "#ffffff" --bgcolor "#000000" 
wecover logo.png "算法分析 (一)" -c "#ffffff" -b "#000000" 
wecover logo.png "算法分析 (一)" "#ffffff" "#000000" 
```

## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2019 kenblikylee
