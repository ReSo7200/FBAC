# imports
from globals import *
from methods import *

from selenium import webdriver


# printing banner
print(banner)


def main():
    count = 1
    vpn_number = 1
    # chrome options
    chrome_options = webdriver.ChromeOptions()
    # add extensions
    chrome_options.add_extension('ad.crx')
    chrome_options.add_extension('co.crx')
    # add arguments
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--log-level=2")

    time.sleep(1)

    num_of_accounts = choose_num_of_account()
    password = choose_accounts_password()
    vpn_method = choose_vpn_method()
    option = input(
        colour.WHITE + "[^]-- " + colour.GREEN + "Add bot accounts to your account?\n1.Yes\n2.No\nSelect: "
        + colour.WHITE)

    if option == "1":
        profile_link = input(colour.WHITE + "[^]-- " + colour.GREEN + "Input facebook profile link: " + colour.WHITE)
    else:
        pass

    while count < num_of_accounts:
        # loading user agents randomly from the user_agents text file
        user_agent = get_line('user_agents.txt', random.randrange(1, 100))

        chrome_options.add_argument(f'--user-agent={user_agent}')  # set the user agent
        try:
            print(
                colour.WHITE + "[-]----> " + colour.GREEN + "Creating new account " + colour.PURPLE + "[" + colour.BLUE
                + str(count) + colour.PURPLE + "]\n")

            browser = webdriver.Chrome(options=chrome_options)

            connect_to_VPN(vpn_method, vpn_number)

            if vpn_method == "2":
                vpn_number += 1

                if vpn_number == 68:
                    vpn_number = 1

            # facebook.com
            browser.get(url)

            # get new email from tempMail
            new_email = getMail(browser)

            time.sleep(2)

            # click on the sign-up button
            signup_button = browser.find_element(By.XPATH,
                                                 selectors.fb_signup_button)

            signup_button.click()

            WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, selectors.fb_first_name_field)))

            # fill the information randomly
            # first name
            fb_firstname_field = browser.find_element(By.XPATH, selectors.fb_first_name_field)

            fb_firstname_field.send_keys(get_line('firstname.txt', random.randrange(1, 30)))
            # last name
            fb_lastname_field = browser.find_element(By.XPATH, selectors.fb_last_name_field)

            fb_lastname_field.send_keys(get_line('lastname.txt', random.randrange(1, 30)))
            # email
            fb_email_field = browser.find_element(By.XPATH, selectors.fb_email_field)

            fb_email_field.send_keys(new_email)

            fb_confirm_email = browser.find_element(By.XPATH, selectors.fb_confirm_email_field)

            fb_confirm_email.send_keys(new_email)
            # password
            fb_password_field = browser.find_element(By.XPATH, selectors.fb_password_field)

            fb_password_field.send_keys(password)

            # date of birth
            # day
            fb_day = browser.find_element(By.XPATH, selectors.fb_day_field)
            fb_day.send_keys(gen_day())
            # month
            fb_month = browser.find_element(By.XPATH, selectors.fb_month_filed)

            fb_month.send_keys(gen_month())
            # year
            fb_year = browser.find_element(By.XPATH, selectors.fb_year_field)
            fb_year.send_keys(gen_year())
            # gender
            fb_gender = gen_gender(browser)

            fb_gender.click()

            time.sleep(2)

            fb_signup = browser.find_element(By.XPATH, selectors.fb_signup_button1)

            fb_signup.click()

            url_changes(browser)

            if check_url(browser):
                print(colour.WHITE + "\n[|]----> " + colour.RED + "Account banned/didn't receive OTP\n" + colour.WHITE)
                browser.quit()
                clean_browser()
                disconnect_VPN()
                continue

            otp = receiveEmail(browser)

            fb_put_otp = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, selectors.fb_otp_field)))

            fb_put_otp.send_keys(otp)

            fb_next = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, selectors.fb_confirm_otp_button)))

            fb_next.click()

            time.sleep(12)

            browser.get(url)

            time.sleep(3)

            if check_url(browser):
                hold_account(new_email, password)
                browser.quit()
                clean_browser()
                disconnect_VPN()
                continue

            add_as_friend(browser, option, profile_link)

            success_account(new_email, password)
            count += 1

        except NoSuchElementException:
            print(colour.WHITE + "\n[|]----> " + colour.RED + "Unsupported user-agent!, Switching..." + colour.WHITE)
            pass

        except Exception as e:
            print(e)
            pass

        browser.quit()

        disconnect_VPN()

        clean_browser()


if __name__ == '__main__':
    main()
