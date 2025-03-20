# Human sacrifice refers to offering a living person as a sacrifice to appease the gods.



## Create Virtual Environment
```
python -m venv priestvenv
```

## Activate Virtual Environment
### On Windows
```
priestvenv\Scripts\activate
```

### On macOS/Linux
```
source priestvenv/bin/activate
```

## Install Requirements
```
pip install -r requirements.txt
```

## Deactivate Virtual Environment
```
deactivate
```


## Project Structure
```
Priest/
├── config/
│   ├── __init__.py
│   ├── settings.py       # 项目配置
│   └── database.py       # 数据库配置
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── spider.py     # 爬虫核心逻辑
│   │   └── scheduler.py  # 调度器（模式选择入口）
│   ├── db/
│   │   ├── __init__.py
│   │   ├── manager.py    # 数据库管理
│   │   └── models.py     # 数据模型
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── downloader.py # 下载管理器
│   │   └── logger.py     # 日志配置
│   └── cli.py            # 命令行入口
├── data/
│   ├── downloads/        # 下载文件存储目录
│   └── database/         # 数据库文件存储目录
├── tests/                # 单元测试
├── requirements.txt      # 依赖文件
└── README.md             # 项目说明

```
