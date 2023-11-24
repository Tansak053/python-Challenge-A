from area import rectangle_area, circle_area, prism_volume, sphere_volume
from cube import rectangle_volume as cube_rectangle_volume, sphere_volume as cube_sphere_volume

def main():
    print("************************************************ AREA & CUBE ************************************************")
    print("1. พื้นที่สี่เหลี่ยม  2. พื้นที่วงกลม  3. ปริมาตรทรงสี่เหลี่ยม  4. ปริมาตรทรงกลม  0. ออกจากการทำงาน")
    
    while True:
        try:
            choice = int(input("**************************************\nเลือกเมนู : "))
            print("**************************************")

            if choice == 0:
                print("**************************************\nทำความรู้จบ\n**************************************")
                break
            elif choice in [1, 2, 3, 4]:
                if choice == 1:
                    width = float(input("ป้อนความกว้าง: "))
                    length = float(input("ป้อนความยาว: "))
                    print(f"พื้นที่สี่เหลี่ยม: {rectangle_area(width, length)}")
                elif choice == 2:
                    radius = float(input("ป้อนรัศมี: "))
                    print(f"พื้นที่วงกลม: {circle_area(radius)}")
                elif choice == 3:
                    width = float(input("ป้อนความกว้าง: "))
                    length = float(input("ป้อนความยาว: "))
                    height = float(input("ป้อนความสูง: "))
                    print(f"ปริมาตรทรงสี่เหลี่ยม: {prism_volume(width, length, height)}")
                elif choice == 4:
                    radius = float(input("ป้อนรัศมี: "))
                    print(f"ปริมาตรทรงกลม: {sphere_volume(radius)}")
            else:
                print("**************************************\nกรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น\n**************************************")
        except ValueError:
            print("**************************************\nกรุณาป้อนตัวเลขเท่านั้น\n**************************************")

if __name__ == "__main__":
    main()