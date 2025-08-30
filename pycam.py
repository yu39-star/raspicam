import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
x = 0
while True:
    x = x + 1
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("title", frame)
    key = cv2.waitKey(1)
    print(x)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
