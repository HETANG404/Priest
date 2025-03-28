import utils.create_folder
from core.spider import *
from utils.create_folder import *



if __name__ == "__main__":
    print('''1.下载排行榜(日/周/月榜)
2.下载画师主页
3.下载个人主页最近更新''')

    url = 'https://www.pixiv.net/'
    while True:
        choice = input('请输入想要下载的模式：')
        if choice == '1':   # https://www.pixiv.net/ranking.php?mode=monthly&p=1&format=json

            valid_modes = {"daily", "weekly"}

            print('输入下载的模式: daily / daily_r18 / weekly / weekly_r18 / monthly')
            mode = input('输入上面的选项之一:')
            
            if mode not in valid_modes:
                raise ValueError("非法模式")

            relative_path = mode

            method_name = f"create_{relative_path}_folder"  # 动态拼接方法名
            method = getattr(utils.create_folder,method_name)  # 获取方法对象

            if callable(method):
                path = method()  # 执行方法
            else:
                raise ValueError(f"未找到方法: {method_name}")

            page = int(input('输入想要下载的页数(50张为一页):'))
            for i in range(page):
                url += f"ranking.php?mode={mode}&p={i+1}&format=json"
                crawler_ranking(url, i, path)

        elif choice == '2':   # https://www.pixiv.net/ajax/user/23945843/profile/all?lang=zh

            user_id = input('输入作者主页号:')

            url += 'ajax/user/' + user_id + '/profile/all?lang=zh'
            crawler_users(url, user_id)

        elif choice == '3':   # https://www.pixiv.net/ajax/follow_latest/illust?lang=zh&mode=r18&p=1
            num = int(input('是否只下载r18(否输入0 是输入1)'))
            page = int(input('输入想要下载的页数(60张为一页):'))
            mode = 'latest'
            url += 'ajax/follow_latest/illust?lang=zh'
            if num:
                url += '&mode=r18'
                mode += '_r18'
            if not os.path.exists(mode):
                os.makedirs(mode)
            for i in range(page):
                url += f"&p={i+1}"
                crawler_latest(url, i, mode)

        else:
            print('输入错误，请输入 1, 2 or 3')
            continue
        break
    print('下载任务结束')

# https://www.pixiv.net/artworks/92691155