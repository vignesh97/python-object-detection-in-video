import cv2, time

first_frame = None

statusList=[None,None]
video = cv2.VideoCapture(0)

times=[]
a=1
while True:
    a=a+1
    check, frame = video.read()
    status = 0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)

    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]

    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (_,cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    statusList.append(status)

    if statusList[-1]==1 and statusList[-2]==0:
        times.append(datetime.now())
    if statusList[-1]==0 and statusList[-2]==1:
        times.append(datetime.now())


    cv2.imshow("Capturing",gray)
    cv2.imshow("Capturing Delta",delta_frame)
    cv2.imshow("Capturing threshold",thresh_frame)
    cv2.imshow("Capturing Motion Objects",frame)

    key =cv2.waitKey(1)
    if key==ord('q'):
        break

print(a)
print(statusList)
print(times)
video.release()
cv2.destroyAllWindows()
