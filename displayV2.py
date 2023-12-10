#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from readAPI import readAPI
import threading
import time

def read():
	while True:
		print(raadAPI)
		time.sleep(10)

test = "PM2.5:         PM10:        SOX:        NOX:     "

def dataPro(l):
    print("in dataPro")
    global test
    pm2_5 = l[0]
    pm10 = l[1]
    sox = l[2]
    nox = l[3]
    test = "PM2.5: " + str(pm2_5) + " PPM  PM10: "+ str(pm10) + " PPM  SOX: " + str(sox) + " mg/m3  NOX: " + str(nox) + " mg/m3"

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/8x13B.bdf")
        textColor = graphics.Color(50, 255, 100)
        pos = offscreen_canvas.width
        my_text = test #self.args.text
        count = 0
        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 12, textColor, test)
            pos -= 1
            if (pos + len < 0):
                count += 1
                print(count)
                pos = offscreen_canvas.width
                if(count > 1):
                    count = 0
                    try:
                        dataPro(readAPI())
                    except:
                        print("NO INTERNET CONNECTION ..!")

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

#t1 = threading.Thread(read)

# Main function
if __name__ == "__main__":
 #   t1.start()
#    dataPro(readAPI)
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
