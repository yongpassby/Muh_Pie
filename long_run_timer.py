import datetime
import time


def main():
    time.sleep(1.5)


if __name__ == '__main__':
    st = time.time()
    print('run start at', time.strftime('%Y%m%d-%H%M%S', time.localtime(st)))

    main()

    ed = time.time()
    print('run finish at', time.strftime('%Y%m%d-%H%M%S', time.localtime(ed)))
    print('Total runtime -->', str(datetime.timedelta(seconds=ed-st)))
