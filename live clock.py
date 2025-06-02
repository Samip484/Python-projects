import time

while True:
    Hr = int(time.strftime('%I'))
    min = int(time.strftime('%M'))
    sec = int(time.strftime('%S'))
    ap = time.strftime('%p')
    
    print(f"\rCurrent Time: {Hr:02}:{min:02}:{sec:02} {ap}", end="")  # \r to overwrite previous time and :02 to replace 3 wih 03 
    time.sleep(1)