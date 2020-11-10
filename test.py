from tornado.concurrent import run_on_executor

from concurrent.futures import ThreadPoolExecutor

import time


class Test():
    executor = ThreadPoolExecutor(10)  # set up a threadpool

    @run_on_executor
    def longTimeTask():

        print("go to sleep")

        time.sleep(20)  # go to sleep

        print("wake up")


if __name__ == "__main__":
    test = Test()

    test.longTimeTask()

    print("print very soon")

