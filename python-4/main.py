import math

def calc_angle_mbc(AB, BC):
    AC = math.hypot(AB, BC)
    MC = AC/2
    BM = MC

    # Divided MBC in 2 triangles, creating a triangle rectangle. The new triangle has the vertices MBX
    BX = BC/2
    return round(math.degrees(math.acos(BX/BM)))

if __name__ == '__main__':
    print(calc_angle_mbc(10, 10))

