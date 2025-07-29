def hello(name : str) ->str :
    return f"hello, {name}"




#%%
import requests
from bs4 import BeautifulSoup
import re
import typer
import urllib.request
import urllib.parse
import pandas as pd
import json
from datetime import datetime
from typing import Optional

def check_rain( area_code="270000"):
    # 気象庁の天気予報ページ
    
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"

    try:
        response = requests.get(url)
        data = response.json()
        
        # 今日の降水確率を取得
        today_forecast = data[0]['timeSeries'][1]['areas'][0]['pops'][0]
        rain_prob = int(today_forecast) if today_forecast != '' else 0
        #today_temp = data[0]['timeSeries'][2]

        #min_temp = today_temp['tempsMin'][0] if today_temp['tempsMin'][0] != '' else "不明"
        #max_temp = today_temp['tempsMax'][0] if today_temp['tempsMax'][0] != '' else "不明"
            
        
        #print(f"今日の気温: 最低{min_temp}℃ / 最高{max_temp}℃")
    #except (IndexError, KeyError):
        #print("気温データが取得できませんでした")
        
        print(f"今日の降水確率: {rain_prob}%")
        
        if rain_prob > 50:
            print("🌂 傘を持っていきましょう！")
        else:
            print("☀️ 傘は不要です")
            
    except Exception as e:
        print(f"データ取得エラー: {e}")
        # フォールバック: HTMLスクレイピング
        try:
            url = f"https://www.jma.go.jp/bosai/forecast/#area_type=offices&area_code={area_code}"
            
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 降水確率のパターンを検索
            rain_pattern = re.search(r'(\d+)%', str(soup))
            if rain_pattern:
                rain_prob = int(rain_pattern.group(1))
                print(f"今日の降水確率: {rain_prob}%")
                if rain_prob > 50:
                    print("🌂 傘を持っていきましょう！")
                else:
                    print("☀️ 傘は不要です")
            else:
                print("降水確率データが見つかりません")
                
        except Exception as e2:
            print(f"フォールバックも失敗: {e2}")
        
#%%
def rain(area_code: str = "270000"):
    """気象庁から降水確率を取得して傘の必要性を判断"""
    check_rain(area_code)

if __name__ == "__main__":
    check_rain()



# %%
