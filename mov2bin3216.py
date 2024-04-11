import cv2
import numpy as np
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py input_video output_file")
    sys.exit()

input_video = sys.argv[1]
output_file = sys.argv[2]

# 動画を読み込む
cap = cv2.VideoCapture(input_video)

# ファイル名
file_name = output_file

frame_number = 0

# フレームごとのループ
while True:
    ret, frame = cap.read()

    # 動画の終わりに達した場合、ループを終了
    if not ret:
        break

    # 3フレームごとに処理
    if frame_number % 3 == 0:
        g_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #crop_frame = g_frame[:, 200:-200]
        resized_frame = cv2.resize(g_frame, (32, 16))
        # 二値化
        _, binary_frame = cv2.threshold(resized_frame, 128, 1, cv2.THRESH_BINARY)

        # テキストファイルに書き込み
        with open(file_name, 'a') as file:
            #binary_frame[0::2, :] = binary_frame[0::2, ::-1]
            for i in range(16):
                if i%2==0:
                    row = binary_frame[i][::-1]
                    for j in range(16):
                        pixel = row[16+j]
                        file.write(str(pixel) + ' ')
                else:
                    row=binary_frame[i]
                    for j in range(16):
                        pixel = row[j]
                        file.write(str(pixel) + ' ')
                file.write('\n')
            for i in range(16):
                if i%2==0:
                    row = binary_frame[i][::-1]
                    for j in range(16):
                        pixel = row[j]
                        file.write(str(pixel) + ' ')
                else:
                    row=binary_frame[i]
                    for j in range(16):
                        pixel = row[16+j]
                        file.write(str(pixel) + ' ')
                file.write('\n')
            print(frame_number)

    frame_number += 1

# ファイルを閉じる
cap.release()
cv2.destroyAllWindows()
