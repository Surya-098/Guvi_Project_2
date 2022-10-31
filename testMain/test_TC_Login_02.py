import time

import main


def test_launch():
    # launching the Orangehrm URL
    main.launch()
    time.sleep(2)


def test_invalid_login():
    # login with admin credentials
    main.invalid_login()
    time.sleep(2)