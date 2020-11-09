# phone search to get the place which phone belongs to
from phone import Phone


class PhoneSearch(object):
    def __init__(self, number):
        self.number = number

    def search(self):
        ph = Phone()
        city = ph.find(self.number)

        print(city)  # 所有信息
        print('手机号：' + self.number)
        print('所属省份：' + city['province'])
        print('所属市区：' + city['city'])
        print('邮    编：' + city['zip_code'])
        print('电话区号：' + city['area_code'])
        print('运 营 商：' + city['phone_type'])

        return city
