from input_view import InputView


def date_verification(date) :
    if not date.isdigit() :
            raise ValueError("[ERROR] 숫자를 입력하세요")
        
    date=int(date)
    if date<1 or date>31 :
        raise ValueError("[ERROR] 유효하지 않은 날짜입니다. 다시 입력해주세요")


def menu_verification(menu) :
    menu_list = [
    "양송이수프",
    "타파스",
    "시저샐러드",
    "티본스테이크",
    "바비큐립",
    "해산물파스타",
    "크리스마스파스타",
    "초코케이크",
    "아이스크림",
    "제로콜라",
    "레드와인",
    "샴페인"
    ]
    for i in range(len(menu)) :
        a = menu[i]
        a= a.split('-')
        menu[i]=a
        
        if menu[i][0] not in menu_list :
            raise ValueError("[ERROR] 유효하지 않은 주문입니다. 다시 입력해 주세요.")
        if not menu[i][1].isdigit() :
            raise ValueError("[ERROR] 유효하지 않은 주문입니다. 다시 입력해 주세요.")

    return menu



def main():
    menu = InputView.menu_ask()
    menu_verification(menu)
    print(menu)
    pass

if __name__ == "__main__":
    main()
