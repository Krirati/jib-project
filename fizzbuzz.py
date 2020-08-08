# ถ้า input ที่เข้ามาหาร 3 ลงตัว ให้ return fizz
# ถ้า input ที่เข้ามาหาร 5 ลงตัว ให้ return buzz
# ถ้า input ที่เข้ามาหาร 3 และ  5ลงตัว ให้ return fizzbuzz
#ถ้าไม่ตรงส่ง เลขนั้น
#python fizzbuzz.py การรันตรงๆ ตัวแปล __name__ จะโดนเซตเป็น __main__
#import fizz ubzz จะมีตัวแปลที่ชื่อ__name__ โดนเซตเป็น fizzbuzz

import unittest


def fizzbuzz(number):
    if number == 1:
        return 1
    elif number == 3:
        return 'Fizz'

class TestFizzBuzz(unittest.TestCase): 
    def test_input_1_should_get_1(self):
        result = fizzbuzz(1)
        self.assertEqual(result, 1)

    def test_input_3_should_get_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'Fizz')
if __name__ == '__main__':
    unittest.main()