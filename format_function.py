lan1 = 10
lan2 = 9
lan3 = 11
print("lan = {} {} {}".format(lan1, lan2, lan3))

import cv2

image = cv2.imread("format().PNG", cv2.IMREAD_COLOR)
cv2.imshow("format()", image)
cv2.waitKey(0)
cv2.destroyAllWindows()