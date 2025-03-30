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
├─ config/                     # 配置模块
│
├─ data/                       # 本地数据资源
│  ├─ database/                # 数据库存储
│  └─ images/                  # 图片资源（即将只保留本地）
│     ├─ following/
│     ├─ ranking/
│     │  ├─ daily/
│     │  ├─ daily_r18/
│     │  ├─ monthly/
│     │  ├─ weekly/
│     │  └─ weekly_r18/
│     └─ users/
│        └─ 
│
├─ migrations/                 # 数据库迁移文件
│
├─ priestvenv/                 # Python 虚拟环境文件夹
│
│
├─ src/
│  ├─ core/                    # 业务逻辑
│  ├─ db/                      # 数据库模型及连接逻辑
│  └─ utils/                   # 工具
│
├─ tests/                      # 测试代码目录


```
