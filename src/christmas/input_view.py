class InputView():
    def read_date(self) :
        print("12월 중 식당 예상 방문 날짜는 언제인가요?(숫자만 입력해 주세요!)")
        date = input ()
        if not date.isdigit() :
            raise ValueError("[ERROR] 숫자를 입력하세요요")
        
        date=int(date)
        if date<1 or date>31 :
            raise ValueError("[ERROR] 유효하지 않은 날짜입니다. 다시 입력해주세요")
