import sys
import board
import neopixel
import time

if len(sys.argv)!=2:
    print("ファイル名を指定してください")
    sys.exit(1)

file_name = sys.argv[1]
try:
    with open(file_name,'r') as file:
        lines = file.readlines()

    binary_array =[]

    for line in lines:
        values = line.strip().split()
        row = [int(value) for value in values]
        binary_array.append(row)
    file.close()

    pixels = neopixel.NeoPixel(board.D10,n=512,brightness=0.1,auto_write=False)
    while True:
        for i in range(2190):
            for j in range(32):
                for k in range(16):
                    pixels[j*16+k]=(binary_array[i*32+j][k]*128,binary_array[i*32+j][k]*128,50)
            pixels.show()
            time.sleep(0.06)
    #pixels.fill((0,0,0))
    #pixels.show()

except FileNotFoundError:
    print("指定されたファイルは存在しません")

except KeyboardInterrupt:
    pixels.fill((0,0,0))
    pixels.show()