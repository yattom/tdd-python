from fitsbooze import FitsBooze

class Test数字を文字列に変換せよ:
    def test_1の場合(self):
        fitsbooze = FitsBooze()
        actual = fitsbooze.number_to_string(1)
        assert actual == "1"

class Test3の倍数の場合はFits:
    def test_3の場合(self):
        fitsbooze = FitsBooze()
        actual = fitsbooze.number_to_string(3)
        assert actual == "Fits"

class Test1の位が5の場合はBooze:
    def test_5の場合はBze(self):
        fitsbooze = FitsBooze()
        actual = fitsbooze.number_to_string(5)
        assert actual == "Bze"

    def test_10の場合は1の位が5ではないのでそのまま(self):
        fitsbooze = FitsBooze()
        actual = fitsbooze.number_to_string(10)
        assert actual == "10"

class Test3の倍数で1の位が5の場合はFitsBooze:
    def test_15の場合はFitsBoze(self):
        fitsbooze = FitsBooze()
        actual = fitsbooze.number_to_string(15)
        assert actual == "FitsBoze"

    def test_30の場合はFits(self):
        fitsbooze = FitsBooze()
        actual = fitsbooze.number_to_string(30)
        assert actual == "Fits"

class Test数字に合致する度数に対応する具体名も付加せよ:
    def test_75の場合(self):
        fitsbooze = FitsBooze()
        actual = fitsbooze.number_to_string(75)
        assert actual == "FitsBooooooozeRum"

    def test_15の場合(self):
        fitsbooze = FitsBooze()
        actual = fitsbooze.number_to_string(15)
        assert actual == "FitsBozeSake"

def test_名称取得を独立させる():
    fitsbooze = FitsBooze()
    actual = fitsbooze.get_liquor_name(15)
    assert actual == "Sake"

def test_名称を追加できる():
    fitsbooze = FitsBooze()
    fitsbooze.add_liquor(10, 18, "Wine")
    actual = fitsbooze.get_liquor_name(18)
    assert actual == "Wine"