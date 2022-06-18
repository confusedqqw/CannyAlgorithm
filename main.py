import cv2 as cv


def filter(image):
    blurred = cv.GaussianBlur(image, (3,3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # Находим градиент по X
    grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # Находим градиент по y
    grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # Преобразуем значение градиента в 8 бит
    x_grad = cv.convertScaleAbs(grad_x)
    y_grad = cv.convertScaleAbs(grad_y)
    # Объединяем два градиента
    src1 = cv.addWeighted(x_grad, 0.5, y_grad, 0.5, 0)
    # Объединяем градиенты, используя алгоритм, где 50 и 100 - пороги
    edge = cv.Canny(src1, 50, 100)
    cv.imshow("Canny_edge_1", edge)


src = cv.imread("picture.png")
cv.imshow("picture", src)
filter(src)
cv.waitKey(0)
cv.destroyAllWindows()