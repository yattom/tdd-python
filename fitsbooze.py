#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def generate_booze(number):
    """
    10の位の数と同じ数の「o」を含む「B[o...]ze」文字列を生成する
    
    例:
    - 一桁の数字(10の位は0): "Bze"
    - 10の位が1の数字(例: 10, 15): "Boze"
    - 10の位が2の数字(例: 20, 25): "Booze"
    - 10の位が3の数字(例: 30, 35): "Boooze"
    - 10の位が9の数字(例: 90): "Boooooooooze"
    
    数値の1の位が5または0でなくても、10の位に応じた「o」の数で文字列を生成する。
    
    Args:
        number: 対象の数値
    
    Returns:
        生成された「B[o...]ze」文字列
    """
    tens_digit = (number // 10) % 10
    base = "B"
    o_part = "o" * tens_digit
    return f"{base}{o_part}ze"

ALCOHOL_NAMES = {
    range(1, 11): "ビール",
    range(11, 21): "ワイン",
    range(21, 41): "焼酎",
    range(41, 61): "ウォッカ",
    range(61, 101): "スピリタス"
}

def get_alcohol_name(number):
    """
    数値に対応する度数の名称を返す
    
    Args:
        number: 対象の数値
    
    Returns:
        度数に対応する名称
    """
    for key in ALCOHOL_NAMES:
        if number in key:
            return ALCOHOL_NAMES[key]
    return ""

def get_fitsbooze_output(number):
    """
    数値に対応するFitsBooze出力を生成する
    
    Args:
        number: 対象の数値
    
    Returns:
        FitsBoozeルールに従った出力文字列
    """
    is_multiple_of_three = number % 3 == 0
    ends_with_five = number % 10 == 5
    
    if is_multiple_of_three and ends_with_five:
        return f"FitsBooze ({get_alcohol_name(number)})"
    elif is_multiple_of_three:
        return f"Fits ({get_alcohol_name(number)})"
    elif ends_with_five:
        booze = generate_booze(number)
        return f"{booze} ({get_alcohol_name(number)})"
    else:
        return f"{number} ({get_alcohol_name(number)})"

def print_fitsbooze(start=1, end=100):
    """
    指定された範囲の数値に対してFitsBoozeルールを適用して出力する
    
    Args:
        start: 開始数値(デフォルト: 1)
        end: 終了数値(デフォルト: 100)
    """
    for number in range(start, end + 1):
        print(get_fitsbooze_output(number))

if __name__ == "__main__":
    print_fitsbooze()
