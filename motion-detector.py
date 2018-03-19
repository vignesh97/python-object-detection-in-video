import cv2, time

first_frame = None


video = cv2.VideoCapture(0)



a=1
while True:
    a=a+1
    check, frame = video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GuassianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame.gray)

    cv2.imshow("Capturing",gray)
    cv2.imshow("Capturing Delta",delta_frame)

    key =cv2.waitKey(1)
    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
