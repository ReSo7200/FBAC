# imports
import random
import re
import subprocess
import time
import pyperclip

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from globals import colour, selectors


# methods

# Retrieve line from file
def get_line(filename, line_number):
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if i == line_number:
                return line.strip()


# connect to purevpn
def connect_to_VPN(vpn_method, vpn_number):
    # if the selected method was 1, it will select a random line from the VPN countries list
    if vpn_method == "1":
        vpn_Count = random.randrange(1, 60)
    # if the selected method was 2 (else), it will sort the VPN countries list
    else:
        vpn_Count = vpn_number

    # setting country from  the VPN list file
    country = get_line('vpn.txt', vpn_Count)

    # pureVPN command to connect to the specified country
    command = ['/opt/purevpn-cli/bin/purevpn-cli', '-c', country]

    # getting the result from running the command
    result = subprocess.run(command, capture_output=True, text=True)

    stdout = result.stdout

    # IP address pattern (Regex)
    ip_address_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

    # getting the IP address from the command result
    match = ip_address_pattern.search(stdout)

    ip_address = match.group()

    print(
        colour.BLUE + "    [+]----> " + colour.GREEN + "VPN Connected\n" + colour.PURPLE + "        [*]----> "
        + colour.YELLOW + "IP Address: " + colour.CYAN + ip_address + colour.WHITE + "\n")

    time.sleep(5)


# Disconnect from pureVPN
def disconnect_VPN():
    command = ['/opt/purevpn-cli/bin/purevpn-cli', '-d']

    subprocess.run(command, capture_output=True, text=True)

    print(colour.WHITE + "[|]----> " + colour.RED + "VPN Disconnected\n" + colour.WHITE)

    time.sleep(5)


# clean browser using bleachbit
def clean_browser():
    command = ['/usr/bin/bleachbit', '-c', 'google_chrome.cache',
               'google_chrome.cookies',
               'google_chrome.dom',
               'google_chrome.form_history',
               'google_chrome.history',
               'google_chrome.passwords',
               'google_chrome.search_engines',
               'google_chrome.session',
               'google_chrome.site_preferences',
               'google_chrome.sync',
               'google_chrome.vacuum']

    subprocess.run(command, capture_output=True, text=True)

    print(colour.WHITE + "[-]----> " + colour.GREEN + "Browser Cleaned!\n" + colour.WHITE)


# get a new email from tempmailo.com
def getMail(browser):
    browser.execute_script("window.open('');")

    browser.switch_to.window(browser.window_handles[-1])

    mail_url = "https://tempmailo.com/"

    browser.get(mail_url)

    time.sleep(3)

    copy_email = browser.find_element(By.XPATH, selectors.copy_email_button)

    copy_email.click()

    copy_email = pyperclip.paste()

    print(
        colour.BLUE + "    [+]----> " + colour.GREEN + "Created New Email\n" + colour.PURPLE + "        [*]----> "
        + colour.YELLOW + "Email: " + colour.CYAN + copy_email + colour.WHITE)

    time.sleep(1)

    browser.switch_to.window(browser.window_handles[0])

    return copy_email


# checks if the received mail text has changed
def text_has_changed(current_mail, old_text):
    def check(browser):
        time.sleep(2)
        # clicking on the refresh button
        refresh_button = browser.find_element(By.XPATH, selectors.refresh_button)
        refresh_button.click()
        element = browser.find_element(*current_mail)
        return element if element.text != old_text else False

    return check


# receive the OTP email from facebook
def receiveEmail(browser):
    time.sleep(1)

    # switching to the email tab
    browser.switch_to.window(browser.window_handles[-1])
    browser.switch_to.window(browser.window_handles[-1])

    time.sleep(1)

    current_mail = (By.XPATH, selectors.current_mail)

    old_text = browser.find_element(current_mail).text

    try:
        # Wait up to 50 seconds for the text of the element to change
        WebDriverWait(browser, 50).until(text_has_changed(current_mail, old_text))

        # if the current received mail was changed it will take the OTP
        email_otp = browser.find_element(By.XPATH, selectors.mail_otp).text

        email_otp = email_otp.replace(' is your Facebook confirmation code', '')

        email_otp = email_otp.replace('FB-', '')

        print(colour.PURPLE + "        [*]----> " + colour.YELLOW + "OTP: " + colour.CYAN + email_otp)

    except (TimeoutException, StaleElementReferenceException):
        # otherwise, the email that includes the OTP wasn't received - (Account banned)
        print(colour.WHITE + "\n    [|]----> " + colour.RED + "Account banned/didn't receive OTP\n" + colour.WHITE)

    browser.switch_to.window(browser.window_handles[0])
    return email_otp


# checks if the current url has been changed
def url_changes(browser):
    current_url = browser.current_url
    return WebDriverWait(browser, 25).until(lambda browser: browser.current_url != current_url)


# checks if an account needs a verification (banned)
def check_url(browser):
    current_url = browser.current_url
    return "https://www.facebook.com/checkpoint/" in current_url


# choose a random gender
def gen_gender(browser):
    male_element = browser.find_element(By.XPATH, selectors.fb_gender_male)

    female_element = browser.find_element(By.XPATH, selectors.fb_gender_female)

    gender = [male_element, female_element]

    return random.choice(gender)


# choose a random year
def gen_year():
    # random year from 1980 to 2002
    yearINT = random.randrange(1980, 2002)

    year = str(yearINT)

    return year


# choose a random month
def gen_month():
    monthINDIX = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    month = random.choice(monthINDIX)

    return month


# choose a random day
def gen_day():
    dayINT = random.randrange(1, 28)

    day = str(dayINT)

    return day


# add successfully created account to a txt file
def success_account(email, password):
    with open('success.txt', 'a') as f:
        # Write the new email with the password to the success text file
        f.write(email + ":" + password + "\n")

        print(
            colour.BLUE + "\n    [+]----> " + colour.GREEN + "Account created: " + colour.CYAN + email + "\n"
            + colour.WHITE)


# add need verification accounts to a txt file
def hold_account(email, password):
    with open('hold.txt', 'a') as f:
        # Write the new email with the password to the hold text file
        f.write(email + ":" + password + "\n")

        print(
            colour.BLUE + "\n    [+]----> " + colour.GREEN + "Account created, Need verification: "
            + colour.RED + email + "\n" + colour.WHITE)


# select the number of accounts to be created
def choose_num_of_account():
    try:
        num_of_accounts = int(input(
            colour.WHITE + "[^]-- " + colour.GREEN + "How many accounts would you like to create? " + colour.WHITE))
        return num_of_accounts

    except:
        print(colour.RED + "Wrong input!" + colour.WHITE)
        return choose_num_of_account()  # Ensure that the result of the recursive call is returned


def choose_accounts_password():
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]).{6,}$'

    try:
        password = input(
            colour.WHITE + "[^]-- " + colour.GREEN + "Input the desired password for the accounts " + colour.WHITE)

        # Check if the password matches the regex pattern
        if re.match(password_pattern, password):
            print("\n")
            return password
        else:
            raise ValueError  # Raise a ValueError to trigger the exception block for invalid input

    except ValueError:  # Catch the ValueError for invalid input
        print(colour.RED + "Please input a password that facebook accepts!" + colour.WHITE)
        print("\n" + colour.PURPLE + "The password must be at least six characters and should be a mix of uppercase "
                                     "and lowercase characters, numbers and punctuation." + colour.WHITE)
        return choose_accounts_password()  # Ensure that the result of the recursive call is returned


# select the vpn method (1. Random from the countries list | 2. Sorted from the countries list)
def choose_vpn_method():
    vpn_method = input(
        colour.WHITE + "[^]-- " + colour.GREEN + "Choose VPN Method:\n1. Random\n2. Sorted\nSelect: ")
    print("\n")

    if vpn_method != "1" and vpn_method != "2":
        return choose_vpn_method()

    else:
        return vpn_method


# make the created facebook account add a specific profile as a friend
def add_as_friend(browser, option, profile_link):
    if option == "1":

        browser.get(profile_link)
        try:

            add_friend_button = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, selectors.fb_add_friend_button))
            )

            add_friend_button.click()

            try:

                time.sleep(3)

                add_friend_button1 = browser.find_element(By.XPATH, selectors.fb_add_friend_button1)

                add_friend_button1.click()
            except NoSuchElementException:
                pass
        except Exception as a:
            print(a)

    else:
        pass
