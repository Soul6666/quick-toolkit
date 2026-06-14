---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: a8ffc02f016d7011f1801f954121c3a4_2d21bc00680a11f1a0095254002afed2
    ReservedCode1: Cm5SJDnzg13XRFOv1gqt1Wu1EMzNMZycQFR4ubU3YaMi8U7ay1FY9wLEMDwqumSvxOCHL96kPczPzkeuzAbeiNh9hVOLP+DcFmKdmtoWcheR3TZpuDPQSYlGbZFHXXxq9DwsGBVK/pW3akvsyxWR7GE6st2rKY7ugmRMbdX8G8XVlkiytA674dyzovI=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: a8ffc02f016d7011f1801f954121c3a4_2d21bc00680a11f1a0095254002afed2
    ReservedCode2: Cm5SJDnzg13XRFOv1gqt1Wu1EMzNMZycQFR4ubU3YaMi8U7ay1FY9wLEMDwqumSvxOCHL96kPczPzkeuzAbeiNh9hVOLP+DcFmKdmtoWcheR3TZpuDPQSYlGbZFHXXxq9DwsGBVK/pW3akvsyxWR7GE6st2rKY7ugmRMbdX8G8XVlkiytA674dyzovI=
---

# Quick Toolkit

命令行常用小工具集合，纯 Python 实现，开箱即用。

## 功能

| 命令 | 说明 | 用法 |
|------|------|------|
| `hash` | 计算文件哈希（MD5/SHA1/SHA256） | `python main.py hash <文件路径> [算法]` |
| `rename` | 批量重命名文件 | `python main.py rename <目录> [前缀] [后缀]` |
| `tree` | 打印目录树结构 | `python main.py tree <目录>` |
| `log` | 写入今日日志 | `python main.py log <日志内容>` |
| `lines` | 统计代码行数 | `python main.py lines <目录> [文件后缀]` |

## 快速开始

```bash
# 计算文件 MD5
python main.py hash D:\test.pdf

# 批量重命名（前缀 photo_，后缀 _done）
python main.py rename D:\photos photo_ _done

# 查看目录结构
python main.py tree D:\project

# 记录一条日志
python main.py log 完成今天的代码审查

# 统计 Python 文件行数
python main.py lines D:\src .py
```

## 环境要求

- Python 3.7+
- 无第三方依赖
*（内容由AI生成，仅供参考）*
