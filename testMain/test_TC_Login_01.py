import time

import main


def test_launch():
    # launching the Orangehrm URL
    main.launch()
    time.sleep(2)


def test_login():
    # login with admin credentials
    main.login()
    time.sleep(2)

