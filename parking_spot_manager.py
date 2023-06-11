class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    # 생성자로 매개변수를 받아 객체의 속성을 초기화합니다.
    #  __item 속성은 딕셔너리로 초기화하고, 매개변수로 전달받은 값들을 딕셔너리의 키와 값으로 설정합니다.
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {
            'name': name,
            'city': city,
            'district': district,
            'ptype': ptype,
            'longitude': longitude,
            'latitude': latitude
        }

    # 매개변수 'keyword'에 해당하는 값을 반환합니다. 기본인수는 'name'입니다.
    def get(self, keyword='name'):
        return self.__item.get(keyword)

    
    # 객체를 문자열로 표현하는 메서드로, 주차장 정보를 포맷에 맞게 출력합니다.
    def __str__(self):
        item = self.__item
        s = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
'''
주차장 정보를 담고 있는 문자열 리스트 'str_list'를 매개변수로 받아, 
parking_spot 객체의 리스트로 변환하여 반환합니다.
각 문자열은 순번, 자원명, 시도, 시군구, 주차장 유형, 경도, 위도 데이터를
저장하고 있으며, 각 데이터는 쉼표로 구분됩니다.
주차장 객체(spot)를 생성하고 'class_list'에 추가합니다.
'''
def str_list_to_class_list(str_list):
    class_list = []
    for string in str_list:
        data = string.split(',')
        index = data[0].strip()
        name = data[1].strip() # 문자열 값
        city = data[2].strip() # 문자열 값
        district = data[3].strip() # 문자열 값
        ptype = data[4].strip() # 문자열 값
        longitude = float(data[5].strip()) # 실수 값
        latitude = float(data[6].strip()) # 실수 값

        spot = parking_spot(name, city, district, ptype, longitude, latitude)
        class_list.append(spot)

    return class_list

'''
매개변수로 'parking_spot' 클래스 객체의 리스트 spots을 받습니다.
리스트의 길이(spots 원소의 개수)와 리스트 내용(모든 객체의 값)을 출력합니다.
'''
def print_spots(spots):
    length = len(spots)
    print(f"---print elements({length})---")
    for spot in spots:
        print(spot)

# version 3
'''
주어진 spots 리스트에서 각 키워드를 포함하는 spot 객체를 필터링하여 새로운 리스트를 반환합니다.
filter_by_location의 경우 튜플을 매개변수로 받아 spot 객체를 필터링하여 새로운 리스트를 반환합니다.
list 함축: list = [ 출력식 for 변수 in 범위 if 조건 ]
'''
def filter_by_name(spots, name):
    list_filter_by_name = [spot for spot in spots if name in spot.get('name')]
    return list_filter_by_name

def filter_by_city(spots, city):
    list_filter_by_city = [spot for spot in spots if city in spot.get('city')]
    return list_filter_by_city

def filter_by_district(spots, district):
    list_filter_by_district = [spot for spot in spots if district in spot.get('district')]
    return list_filter_by_district

def filter_by_ptype(spots, ptype):
    list_filter_by_ptype = [spot for spot in spots if ptype in spot.get('ptype')]
    return list_filter_by_ptype

def filter_by_location(spots, locations):
    min_lat, max_lat, min_long, max_long = locations
    list_filter_by_location = [spot for spot in spots if min_lat < spot.get('latitude') and\
                                                         max_lat > spot.get('latitude') and\
                                                         min_long < spot.get('longitude') and\
                                                         max_long > spot.get('longitude')]
    return list_filter_by_location

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)