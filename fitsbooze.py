class FitsBooze:
    def number_to_string(self, number: int) -> str:
        result = ""
        if number % 3 == 0:
            result += "Fits"
        if number % 10 == 5:
            result += "B" + "o" * ((number // 10)) + "ze"
        if result == "":
            result = str(number)
        
        if number == 75:
            result += "Rum"
        elif number == 15:
            result += "Sake"
        
        return result