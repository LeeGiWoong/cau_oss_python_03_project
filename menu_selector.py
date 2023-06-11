# 'read_file' 함수를 사용하기 위해 file_manager 모듈을 import합니다.
# 'str_list_to_class_list'와 'print_spots' 함수를 사용하기 위해
#  parking_spot_manger 모듈을 import합니다.
import file_manager
import parking_spot_manager

def start_process(path):
    # 주어진 'path' 경로의 파일을 읽고, 그 결과를 'str_list'에 할당합니다.
    # str_list_to_class_list 함수를 사용하여 'str_list'를 주차 공간 객체의 리스트인 spots로 변환합니다.
    str_list = file_manager.read_file(path)
    spots = parking_spot_manager.str_list_to_class_list(str_list)
    
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            # 'print_spots' 함수를 호출합니다.
            parking_spot_manager.print_spots(spots)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            # 입력 숫자에 따라 그에 맞는 함수를 호출합니다.
            # 모듈의 함수를 호출하기 전 사용자에게 키워드를 입력받아 함수의 인수로 사용합니다.
            if select == 1:
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                # 튜플[locations]은 순서대로 최소위도, 최대위도, 최소경도, 최대경도를 포함합니다.
                locations = (min_lat, max_lat, min_lon, max_lon)
                spots = parking_spot_manager.filter_by_location(spots, locations)
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                # 'sort_by_keyword' 함수를 호출합니다.
                spots = parking_spot_manager.sort_by_keyword(spots, keyword)
            else: print("invalid input")
        elif select == 4:
            # 'Exit'를 출력하고 while문을 빠져나와 프로그램을 종료합니다.
            print("Exit")
            break
        else:
            print("invalid input")