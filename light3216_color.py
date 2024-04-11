import sys
import board
import neopixel
import time

def read_test_file(file_path):
    result=[]
    with open(file_path,'r') as file:
        for line in file:
            elements=line.split('/')
            elements=[element.replace('[','').replace(']','').strip() for element in elements if element]
            row=[int(value) for element in elements for value in element.split()]
            row=[row[i:i+3] for i in range(0,len(row),3)]
            result.append(row)
    return result

if len(sys.argv)!=2:
    print("ファイル名を指定してください")
    sys.exit(1)

file_name = sys.argv[1]
try:
    data = read_test_file(file_name)
    pixels = neopixel.NeoPixel(board.D10,n=512,brightness=0.1,auto_write=False)
    while True:
        for i in range(100):
            for j in range(32):
                for k in range(16):
                    pixels[j*16+k]=(data[i*32+j][k][0],data[i*32+j][k][1],data[i*32+j][k][2])
            pixels.show()
            time.sleep(0.05)
    #pixels.fill((0,0,0))
    #pixels.show()

except FileNotFoundError:
    print("指定されたファイルは存在しません")

except KeyboardInterrupt:
    pixels.fill((0,0,0))
    pixels.show()