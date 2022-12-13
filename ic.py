import cv2

cap = cv2.VideoCapture("dataset/posVideo2.871.avi")
length = int(cap. get(cv2. CAP_PROP_FRAME_COUNT))

while True:
    ret, frame = cap.read()
    height, width, channels = frame.shape
    counter = 0
    # r_mean = 0
    
    # for i in range(height):
    #     for j in range(width):
    #         r_mean += frame[i][j][2]

    # r_mean /= (height * width)

    for i in range(height):
        for j in range(width):
            if frame[i][j][2] > 200:
                if frame[i][j][2] > frame[i][j][1] > frame[i][j][0]:
                    counter += 1
                else:
                    frame[i][j] = 0
            else:
                frame[i][j] = 0

    cv2.imshow("frame", frame)
    porcentage = (counter / (width * height)) * 100
    print(f"burning degree = {porcentage:.3f}")

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
