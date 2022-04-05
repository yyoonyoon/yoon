test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height=test_h, width=test_w, cover=coverage):
    amount = int(height) * int(width) / cover
    print("You will need {0} cans of paint.".format(round(amount)))

paint_calc(test_h,test_w,coverage)