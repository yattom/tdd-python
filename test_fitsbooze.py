from fitsbooze import FitsBooze

def test_数1を文字列に変換する():
    # arrange
    sut = FitsBooze()
    # act
    actual = sut.translate(1)
    # assert
    assert actual == "1"


def test_3の場合はFitsに変換する():
    # arrange
    sut = FitsBooze()
    # act
    actual = sut.translate(3)
    # assert
    assert actual == "Fits"


def test_6の場合はFitsに変換する():
    # arrange
    sut = FitsBooze()
    # act
    actual = sut.translate(6)
    # assert
    assert actual == "Fits"


class Test1の位が5の場合はBoozeに変換する:
    def test_25の場合はBoozeに変換する(self):
        # arrange
        sut = FitsBooze()
        # act
        actual = sut.translate(25)
        # assert
        assert actual == "Booze"

class Test3の倍数で1の位が5の場合はFitsBoozeに変換する:
    def test_15の場合はFitsBozeに変換する_10の位が1なのでoが1つ(self):
        # arrange
        sut = FitsBooze()
        # act
        actual = sut.translate(15)
        # assert
        assert actual == "FitsBoze"

class TestBoozeとは10の位の数とoの数が等しい文字列である:
    def test_5の場合はBzeに変換する(self):
        # arrange
        sut = FitsBooze()
        # act
        actual = sut.translate(5)
        # assert
        assert actual == "Bze"

    def test_25の場合はBoozeに変換する(self):
        # arrange
        sut = FitsBooze()
        # act
        actual = sut.translate(25)
        # assert
        assert actual == "Booze"

    def test_55の場合はBooooozeに変換する(self):
        # arrange
        sut = FitsBooze()
        # act
        actual = sut.translate(55)
        # assert
        assert actual == "Boooooze"


class Test数に合致する度数に対応する名称を取得:
    def test_45の場合はアブサン(self):
        # arrange
        sut = FitsBooze()
        # act
        actual = sut.get_liquor_name(45)
        # assert
        assert actual == "アブサン"
