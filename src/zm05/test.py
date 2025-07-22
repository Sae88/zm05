def hello(name : str) ->str :
    return f"hello, {name}"

import typer

import urllib.request
import urllib.parse

import json
import re
from datetime import datetime
from typing import Optional

app = typer.Typer()

class NoAPIUmbrellaChecker:
    def __init__(self):
        pass
    
    def get_weather_from_demo(self, city="大阪"):
        """デモ用の天気データ"""
        import random


#%%
import requests
from bs4 import BeautifulSoup
import re
import typer
import urllib.request
import urllib.parse
import pandas as pd
import json

def check_rain( area_code="270000"):
    # 気象庁の東京地方の天気予報ページ
    #url = "https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"

    try:
        response = requests.get(url)
        data = response.json()
        
        # 今日の降水確率を取得
        today_forecast = data[0]['timeSeries'][1]['areas'][0]['pops'][0]
        rain_prob = int(today_forecast) if today_forecast != '' else 0
        
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
