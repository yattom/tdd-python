#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from fitsbooze import generate_booze, get_alcohol_name, get_fitsbooze_output

class TestBooze部分を生成する:
    @pytest.mark.parametrize("number, expected", [
        (5, "Bze"),
        (15, "Boze"),
        (25, "Booze"),
        (35, "Boooze"),

    ])
    def test_10の位に合わせてoが増える_1の位が5(self, number, expected):
        assert generate_booze(number) == expected

    @pytest.mark.parametrize("number, expected", [
        (10, "Boze"),
        (20, "Booze"),
        (30, "Boooze"),
        (40, "Booooze"),
        (50, "Boooooze"),
        (90, "Boooooooooze"),
    ])
    def test_10の位に合わせてoが増える_1の位が0(self, number, expected):
        # 10の位の数字が変わる場合
        assert generate_booze(number) == expected

    def test_5の倍数以外が渡されても動く(self):
        assert generate_booze(1) == "Bze"

class Test度数に対応する名称を取得する:
    def test_beer_range(self):
        # ビール範囲（1-10）
        assert get_alcohol_name(1) == "ビール"
        assert get_alcohol_name(5) == "ビール"
        assert get_alcohol_name(10) == "ビール"
    
    def test_wine_range(self):
        # ワイン範囲（11-20）
        assert get_alcohol_name(11) == "ワイン"
        assert get_alcohol_name(15) == "ワイン"
        assert get_alcohol_name(20) == "ワイン"
    
    def test_shochu_range(self):
        # 焼酎範囲（21-40）
        assert get_alcohol_name(21) == "焼酎"
        assert get_alcohol_name(30) == "焼酎"
        assert get_alcohol_name(40) == "焼酎"
    
    def test_vodka_range(self):
        # ウォッカ範囲（41-60）
        assert get_alcohol_name(41) == "ウォッカ"
        assert get_alcohol_name(50) == "ウォッカ"
        assert get_alcohol_name(60) == "ウォッカ"
    
    def test_spirytus_range(self):
        # スピリタス範囲（61-100）
        assert get_alcohol_name(61) == "スピリタス"
        assert get_alcohol_name(80) == "スピリタス"
        assert get_alcohol_name(100) == "スピリタス"
    
    def test_範囲外_100を超える(self):
        assert get_alcohol_name(101) == ""

    def test_範囲外_アルコールなし(self):
        assert get_alcohol_name(0) == ""

    def test_範囲外_マイナスの不正値(self):
        assert get_alcohol_name(-1) == ""

class TestGetFitsBoozeOutput:
    def test_normal_numbers(self):
        # 通常の数字（3の倍数でも1の位が5でもない）
        assert get_fitsbooze_output(1) == "1 (ビール)"
        assert get_fitsbooze_output(2) == "2 (ビール)"
        assert get_fitsbooze_output(4) == "4 (ビール)"
        assert get_fitsbooze_output(11) == "11 (ワイン)"
    
    def test_multiple_of_three(self):
        # 3の倍数
        assert get_fitsbooze_output(3) == "Fits (ビール)"
        assert get_fitsbooze_output(6) == "Fits (ビール)"
        assert get_fitsbooze_output(9) == "Fits (ビール)"
        assert get_fitsbooze_output(12) == "Fits (ワイン)"
    
    def test_ends_with_five(self):
        # 1の位が5
        assert get_fitsbooze_output(5) == "Bze (ビール)"
        assert get_fitsbooze_output(25) == "Booze (焼酎)"
        assert get_fitsbooze_output(55) == "Boooooze (ウォッカ)"
        assert get_fitsbooze_output(95) == "Boooooooooze (スピリタス)"
    
    def test_multiple_of_three_and_ends_with_five(self):
        # 3の倍数かつ1の位が5
        assert get_fitsbooze_output(15) == "FitsBooze (ワイン)"
        assert get_fitsbooze_output(45) == "FitsBooze (ウォッカ)"
        assert get_fitsbooze_output(75) == "FitsBooze (スピリタス)"

