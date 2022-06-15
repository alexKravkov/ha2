import argparse
import sys


def check_triangle_type(a: int, b: int, c: int) -> dict:
    res = {
        "code": 0,
        "triangle_type": "",
        "error_message": ""
    }
    if type(a) == type(b) == type(c) == int:
        if a > 0 and b > 0 and c > 0:
            if a == b == c:
                res["triangle_type"] = "Equilateral Triangle"
                print("Equilateral Triangle")
            elif a == b or a == c or b == c:
                res["triangle_type"] = "Isosceles Triangle"
                print("Isosceles Triangle")
            else:
                res["triangle_type"] = "Scalene Triangle"
                print("Scalene Triangle")
            return res

    res["code"] = 1
    res["error_message"] = "Invalid value"
    return res


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("Side A", help="First side of the triangle",
                            type=int)
        parser.add_argument("Side B", help="Second side of the triangle",
                            type=int)
        parser.add_argument("Side C", help="Third side of the triangle",
                            type=int)
        args = parser.parse_args()
        print(check_triangle_type(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
    except:
        e = sys.exc_info()[0]
