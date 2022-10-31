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


def test_add_button():
    # clicking on the Add button in PIM page
    main.addButton()
    time.sleep(2)


def test_add_user():
    # Add Employee details
    main.PIM_Add_Employee()
    time.sleep(2)
