import time

print('Press Enter to begin.\n'
      + 'Afterwards,press Enter to "Click" the stopwatch.\n'
      + 'Press Ctrl-c(windows) Command-F2(Mac)to quit')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #{}:{}({})'.format(lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone')
