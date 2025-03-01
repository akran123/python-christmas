from input_view import InputView


def date_verification(date) :
    if not date.isdigit() :
            raise ValueError("[ERROR] 숫자를 입력하세요")
        
    date=int(date)
    if date<1 or date>31 :
        raise ValueError("[ERROR] 유효하지 않은 날짜입니다. 다시 입력해주세요")

def main():
    pass

if __name__ == "__main__":
    main()
