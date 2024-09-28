class FitsBooze:
    def translate(self, number: int) -> str:
        result = ""
        if number % 3 == 0:
            result += "Fits"
        if number % 10 == 5:
            result += f"B{'o' * (number // 10)}ze"
        if not result:
            result = str(number)
        
        liquor_name = self.get_liquor_name(number)
        if liquor_name:
            result += liquor_name
        
        return result

    def get_liquor_name(self, number: int) -> str:
        if 45 <= number <= 74:
            return "アブサン"
        return ""
