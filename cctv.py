import cv2
import time
import os
import win32gui
import win32con

def minimize_window():
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window, win32con.SW_MINIMIZE)

def cctv():
    video = cv2.VideoCapture(0)
    video.set(3, 640)  # Set video width
    video.set(4, 480)  # Set video height
    width = video.get(3)
    height = video.get(4)
    print("Video resolution is set to", width, 'x', height)
    print("Help -- \n1. Press the ESC key to exit.\n2. Press 'm' to minimize the window.")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    date_time = time.strftime("recording-%H-%M-%d-%m-%y")
    output_directory = "footages"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output = cv2.VideoWriter(os.path.join(output_directory, date_time + '.avi'), fourcc, 20.0, (640, 480))

    while True:
        check, frame = video.read()
        if check:
            frame = cv2.flip(frame, 1)

            t = time.ctime()
            cv2.rectangle(frame, (5, 5, 120, 20), (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, "Camera 1", (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)
            cv2.imshow('CCTV Camera', frame)
            output.write(frame)

            key = cv2.waitKey(1)
            if key == 27:  # ESC key
                print("Video footage saved in the 'footages' directory.")
                break
            elif key == ord('m'):
                minimize_window()
        else:
            print("Can't open the camera, check configuration.")
            break

    video.release()
    output.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("*" * 80 + "\n" + " " * 30 + "Welcome To CCTV Software\n" + "*" * 80)
    ask = int(input("Do you want to open the CCTV?\n1. Yes\n2. No\n>>>"))

    if ask == 1:
        cctv()
    elif ask == 2:
        print("Goodbye!")
