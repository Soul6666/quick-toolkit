# Quick Toolkit

命令行常用小工具集合，纯 Python 实现，无第三方依赖，开箱即用。

## 功能列表

| 命令 | 说明 | 示例 |
|------|------|------|
| `hash` | 计算文件哈希值 | `python main.py hash D:\test.pdf sha256` |
| `rename` | 批量重命名文件 | `python main.py rename D:\照片 旅行_ _final` |
| `tree` | 打印目录树结构 | `python main.py tree D:\项目` |
| `log` | 写入当天日志 | `python main.py log 完成代码审查` |
| `lines` | 统计代码行数 | `python main.py lines D:\源码 .py` |

## 环境要求

- Python 3.7 及以上
- 无需安装任何第三方库

## 使用示例

```bash
# 计算文件 MD5
python main.py hash D:\test.pdf

# 批量重命名，前缀 photo_，后缀 _done
python main.py rename D:\photos photo_ _done

# 查看目录结构
python main.py tree D:\project

# 记录一条日志
python main.py log 今天完成了模块重构

# 统计 Python 文件行数
python main.py lines D:\src .py
```

## 项目结构

```
quick-toolkit/
├── main.py      # 主程序
├── README.md    # 说明文档
└── .gitignore   # 忽略规则
```
