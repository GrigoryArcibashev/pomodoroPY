import os
import sys
import time
import winsound


def start_timer(seconds: int) -> None:
    print(f'\r>>> {seconds // 60:02} : {seconds % 60:02}', end='')
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
        print(f'\r>>> {seconds // 60:02} : {seconds % 60:02}', end='')


def cycle(rest_in_sec: int) -> None:
    work_time = 25 * 60
    start_timer(work_time)
    signal_timer_to_stop()
    print('\n>>> Rest')
    start_timer(rest_in_sec)
    signal_timer_to_stop()


def signal_timer_to_stop() -> None:
    winsound.Beep(2500, 1000)


def clear_screen() -> None:
    os.system('CLS')


def process_user_input() -> None:
    inp = str()
    while inp not in ('y', 'n'):
        inp = input('\n>>> Do you want to start the timer? (Y/N): ')
        if inp.isalpha():
            inp = inp.lower()
    if inp == 'y':
        clear_screen()
    else:
        shut_down()


def shut_down() -> None:
    input('Нажмите любую кнопку, чтобы завершить программу')
    sys.exit(0)


def main() -> None:
    short_rest_time = 5 * 60
    long_rest_time = 30 * 60
    cycle_count = 1
    while True:
        process_user_input()
        cycle(short_rest_time if cycle_count != 0 else long_rest_time)
        cycle_count = (cycle_count + 1) % 4


if __name__ == '__main__':
    main()
