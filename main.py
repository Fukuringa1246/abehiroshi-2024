import webbrowser
from datetime import datetime, timedelta
import time

def wait_until_target_time(target_time):
    while datetime.now() < target_time:
        time.sleep(1)  # 1秒ごとにチェック

def open_website_at_specific_time(site_url, target_time):
    wait_until_target_time(target_time)
    webbrowser.open(site_url)

if __name__ == "__main__":
    # 開くサイトのURLと指定の日時を設定
    target_site_url = "http://abehiroshi.la.coocan.jp/"
    target_year, target_month, target_day, target_hour, target_minute = 2024, 1, 1, 0, 0
    target_time = datetime(target_year, target_month, target_day, target_hour, target_minute)

    open_website_at_specific_time(target_site_url, target_time)