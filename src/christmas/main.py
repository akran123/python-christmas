from input_view import InputView
from datetime import datetime


def int_verification(x) :
    if not x.isdigit() :
        raise ValueError("[ERROR] 숫자를 입력하세요")
    return int(x)
    
def date_verification(date) :
    int_verification(date)
    date=int(date)
    if date<1 or date>31 :
        raise ValueError("[ERROR] 유효하지 않은 날짜입니다. 다시 입력해주세요")

def menu_list_verification(menu) :
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

    if menu not in menu_list :
        raise ValueError("[ERROR] 유효하지 않은 주문입니다. 다시 입력해 주세요.")

    
def menucount(count) :
    if count>20 :
        raise ValueError("[ERROR] 20개 이상 주문할 수 없습니다")

        
def menu_verification(menu) :
    menu_set = set()
    count=0
    menu = [item.split('-') for item in menu]
    for i in range(len(menu)) :
        menu_list_verification(menu[i][0])
        menu_set.add(menu[i][0])
        menu[i][1]=int_verification(menu[i][1])
        count+=menu[i][1]
        if menu[i][1]<1 :
            raise ValueError("[ERROR] 유효하지 않은 주문입니다. 다시 입력해 주세요.")
    if len(menu_set)!=len(menu) :
            raise ValueError("[ERROR] 유효하지 않은 주문입니다. 다시 입력해 주세요.")
    menucount(count)
    return menu

def price_count(menu) :
    menu_dict = {
        "양송이수프": 6000, "타파스": 5500, "시저샐러드": 8000,
        "티본스테이크": 55000, "바비큐립": 54000, "해산물파스타": 35000,
        "크리스마스파스타": 25000, "초코케이크": 15000, "아이스크림": 5000,
        "제로콜라": 3000, "레드와인": 60000, "샴페인": 25000
    }
    price = 0
    for i in range(len(menu)):
        price+=int(menu[i][1])*menu_dict[menu[i][0]]

    return price
    

def event_available(price,menu):
    drink = ["제로콜라","레드와인","샴페인"]
    
    if price <10000 :
        return False
    count = 0
    for i in range(len(menu)) :
        if menu[i][0] in drink :
            count+=1
    
    if count ==len(menu) :
        raise ValueError(123)
    

def christmas_discount(day):
    if 1 <= day <= 25 :
        return day*100
    if day>25 :
        return 0


def weekday_discount(menu):
    discount = 0
    for i in range (len(menu)):
        if menu[i][0] in ["초코케이크", "아이스크림"]:
            discount += menu[i][1] * 2023
    return discount

def weekend_discount(menu):
    discount = 0
    for i in range (len(menu)):
        if menu[i][0] in ["티본스테이크", "바비큐립", "해산물파스타", "크리스마스파스타"]:
            discount += menu[i][1] * 2023
    return discount


def main():
    day = InputView.read_date()
    int_verification(day)
    day=int(day)
    menu = InputView.menu_ask()
    a=menu_verification(menu)
    price =price_count(a)
    discount = weekday_discount(a)
    print(discount)
    #event_available(price,a)
    print(price)
    print(a)

if __name__ == "__main__":
    main()
