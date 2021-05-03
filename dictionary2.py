import pickle


def main():
    address_book = {}  # 공백 딕셔너리를 생성한다.
    try:
        with open('./phoneData.bin', 'rb') as f:
            address_book = pickle.load(f)
    except FileNotFoundError as e:
        print("파일 존재 하지 않다.")

    while True:
        user = display_menu();
        if user == 1:
            name, number = get_contact()
            address_book[name] = number  # name과 number를 추가한다.
        elif user == 2:
            name = get_name_conteat()
            address_book.pop(name)  # name을 키로 가지고 항목을 삭제한다.
            print("{} deleted".format(name))
        elif user == 3:
            name = get_name_conteat()
            print(name, "의 전화번호 검색 :", address_book[name])
        elif user == 4:
            for key in sorted(address_book):
                print(key, "의 전화 번호 :", address_book[key])
        else:
            with open('./phoneData.bin', 'wb') as f:
                pickle.dump(address_book, f)
                print("파일 저장 완료")
            break


# 이름과 전화 번호를 입력 받아서 반환한다.
def get_contact():
    user = input("이름 :")
    number = input("전화 번호 :")
    return user, number  # 튜플로 반환한다.


def get_name_conteat():
    user = input("이름 : ")
    return user


# 메뉴를 화면에 출력한다.
def display_menu():
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    select = int(input("메뉴 항목을 선택하시오 :"))
    return select



main()
