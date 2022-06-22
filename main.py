import cv2 as cv


def filter(image):
    blurred = cv.GaussianBlur(image, (3,3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    x_grad = cv.convertScaleAbs(grad_x)
    y_grad = cv.convertScaleAbs(grad_y)
    src1 = cv.addWeighted(x_grad, 0.5, y_grad, 0.5, 0)
    edge = cv.Canny(src1, 50, 100)
    cv.imshow("Canny_edge_1", edge)

src = cv.imread("picture.png")
cv.imshow("picture", src)
filter(src)
cv.waitKey(0)
cv.destroyAllWindows()
