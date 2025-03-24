import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

OLGA_DIR = BASE_DIR / "olga"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63',
    'Cookie': 'first_visit_datetime_pc=2024-08-05%2020%3A26%3A45; p_ab_id=4; p_ab_id_2=6; p_ab_d_id=1823254108; yuid_b=KJGHiRM; privacy_policy_agreement=7; c_type=24; privacy_policy_notification=0; a_type=0; b_type=0; _im_vid=01JEH3JV9MN6EH99B44FRH7NAE; _gcl_au=1.1.585489448.1739294285; jp1_ad_freq={}; jp1_et_freq={"1490":[0,1741086321039],"2452":[0,1741104317358],"2628":[0,1741104346858],"2629":[0,1741104321040]}; __utma=235335808.706221898.1733593485.1741082686.1742194225.8; __utmc=235335808; __utmz=235335808.1742194225.8.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _gid=GA1.2.1490090015.1742194254; login_ever=yes; cc1=2025-03-17%2016%3A02%3A25; _ga=GA1.1.706221898.1733593485; PHPSESSID=107829211_XlUPxdQEcHcrwRaM1DQkts0khrOkt10m; device_token=0203980cea55b56bec183370b83397f0; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^9=p_ab_id=4=1^10=p_ab_id_2=6=1; __cf_bm=xiMDRSi4Oo5.2_1PdGMbJ6VgoODHjvErrYlQVDinL.k-1742196146-1.0.1.1-Kt90UKuuDnEOf4Bwl3P8F2jzlkWkhMbbo03Pi.YrZRABfvGqYrj3yTe2IF3O1UL0dHQjFvKbFU4TWJKZuQhovMiK06S_qfnUDx0uKKamjDZjIqkvuTsQD_1SFJSmFbZP; _ga_MZ1NL4PHH0=GS1.1.1742194948.3.1.1742196659.0.0.0; cf_clearance=vPWXInlydHJ1doHfUqlLs3Z5kQKeyjyRCzcX6Wjg1T8-1742196664-1.2.1.1-Nv50bqjPQLFgqXNYHXX1kvaCkPlhBwMZXNw.Z_0qiUyrkgZWrhbarCerho6zqcs.yIBgugHDK2djymMrE_MjGjuDryo7FbNTqjUuQFtN0Fodr3G1kh6I4kpC_6UO83W0k4vFwSAfg3RJ763.qoHmtfxImxwsLYvnaSdn5LtGSwdb1NV4HLWmtmWIRi87RyGy8C7t45rPNSE6oLY7e6iuks9HZv2orMG8nigEx4bGTMJfHy5hD.FqwheLRAtVnluhMKkuf.5oB8x2trT4ZvK6eAV9WKwpOUYesT0Ic_nc77w.3zmRZjzaBlzT_TdwsQZPVFCEl9V3vMqHxqkvvAkajRC6vzu3UnLig_hiRHDjsmY; __utmb=235335808.21.10.1742194225; _ga_75BBYNYN9J=GS1.1.1742194224.9.1.1742197188.0.0.0; FCNEC=%5B%5B%22AKsRol89kd2ZeAx_2Cz3qHgf94NXS3q6dd8yf3tHc_xGYXVCQwJTrAsleKq8LEP-lYEI55gSuWXaVmjJjxP4WKTsS3OO6aU8wJgs7q9WtdwjzoNwelu54LUcJLNYtncfEalDUXkxPCaGdq_qxdr6Ie0lfuIMWjgzjQ%3D%3D%22%5D%5D'
}