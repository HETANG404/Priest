# Human sacrifice refers to offering a living person as a sacrifice to appease the gods.



## Create Virtual Environment
```
python -m venv priestvenv
```

## Activate Virtual Environment
### On Windows
```
priestvenv\Scripts\activate
priestvenv\Scripts\Activate.ps1 # in powershell? maybe
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
│
├── config/
│   ├── __init__.py
│   ├── settings.py       # 项目配置
│   ├── mysql.py          # MySQL配置
│   └── redis.py          # Redis配置
│
├── src/
│   │
│   ├── core/
│   │   ├── spider.py
│   │   └── scheduler.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── mysql_manager.py   # MySQL操作
│   │   ├── redis_manager.py   # Redis操作
│   │   ├── query_handler.py   # 新增查询处理器
│   │   └── models.py
│   │
│   ├── utils/
│   │   ├── downloader.py
│   │   └── logger.py
│   │
│   └── cli.py
│
├── data/
│   ├── images/
│   └── database/         # 保留目录（存放迁移脚本等）
│
├── migrations/           # 新增数据库迁移目录
├── tests/
├── requirements.txt
└── README.md

```
