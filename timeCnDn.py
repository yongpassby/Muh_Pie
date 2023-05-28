import time
import sys


def main():
    print('[main] doing things...')


if __name__ == '__main__':
    cd = 10
    total_run_cnt = 0
    try:
        while True:
            total_run_cnt += 1
            print('run {:04} | msg >>>>'.format(total_run_cnt))
            for i in range(cd):
                print(">> {:03} <<".format(cd - i), sep=' ', end='\r', flush=True)
                time.sleep(1)
            main()

    except KeyboardInterrupt:
        print('ctrl+c, quit')
        sys.exit()
