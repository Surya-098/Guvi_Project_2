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


def test_search_user():
    # search the added user
    main.search_user_PIM()
    time.sleep(2)


def test_edit_user():
    #edit the user details
    main.edit_user_PIM()
    time.sleep(2)

