import cv2 as cv

img = cv.imread("tutorial/line2.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv, (95, 25, 25), (125, 255, 255))
height, width = mask.shape
top = 0
bottom = 0
for i in range(width - 1):
    if (mask[0][i] == 0 and mask[0][i + 1] == 255) or (
        mask[0][i] == 255 and mask[0][i + 1] == 0
    ):
        top = top + i
    if (mask[height - 1][i] == 0 and mask[height - 1][i + 1] == 255) or (
        mask[height - 1][i] == 255 and mask[height - 1][i + 1] == 0
    ):
        bottom = bottom + i

y = 0 + (height - 1)
x = int((top / 2) - (bottom / 2))
if x != 0:
    m = y / x
else:
    m = 10000

c = -int(top / 2)

height_center = int(height / 2)
width_center = int(width / 2)
center_line = int((-height_center / m) - c)

cv.line(img, (int(top / 2), 0), (int(bottom / 2), height - 1), (0, 0, 255), 5)
cv.circle(img, (center_line, height_center), 5, (255, 0, 0), -1)

cv.imshow("image line", img)
cv.waitKey(0)
