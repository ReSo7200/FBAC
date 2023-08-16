# colours
class colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    CWHITE = '\33[37m'


class selectors:
    # facebook selectors
    fb_signup_button = '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a'
    fb_first_name_field = ('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div['
                           '1]/div/input')
    fb_last_name_field = ('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div['
                          '2]/div/div[1]/input')
    fb_email_field = '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input'
    fb_confirm_email_field = ('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div['
                              '1]/input')
    fb_password_field = '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input'
    fb_day_field = ('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div['
                    '2]/span/span/select[1]')
    fb_month_filed = ('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div['
                      '2]/span/span/select[2]')
    fb_year_field = ('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div['
                     '2]/span/span/select[3]')
    fb_gender_male = '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input'
    fb_gender_female = '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input'
    fb_signup_button1 = '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button'
    fb_otp_field = '/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input'
    fb_confirm_otp_button = '/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/button'
    fb_add_friend_button = ('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div['
                            '2]/div/div/div/div[4]/div/div/div[1]/div/div/div')
    fb_add_friend_button1 = ('/html/body/div[1]/div/div[1]/div/div[6]/div/div/div[1]/div/div[2]/div/div/div/div['
                             '4]/div[1]/div/div/div[1]/div[2]')

    # tempmailo selectors
    copy_email_button = '/html/body/main/div[2]/div/div[1]/div[1]/div/button'
    refresh_button = '/html/body/main/div[2]/div/div[1]/div[2]/div[2]/button'
    current_mail = '/html/body/main/div[2]/div/div[2]/div[1]/ul/li/div[2]/div'
    mail_otp = '/html/body/main/div[2]/div/div[2]/div[1]/ul/li/div[2]/div'


# Banner
banner = colour.BOLD + colour.BLUE + '''  
  ______ ____          _____ 
 |  ____|  _ \   /\   / ____|
 | |__  | |_) | /  \ | |     
 |  __| |  _ < / /\ \| |     
 | |    | |_) / ____ \ |____ 
 |_|    |____/_/    \_\_____|
                                                   
{0}[{1}-{2}]--> {3}FBAC Facebook account creator {4}Version 0.3
{5}[{6}-{7}]--> {8}coded by {9}ReSo7200{10}
{11}[{12}-{13}]-->{14} Facebook account creator! 

		'''.format(
    colour.RED, colour.CWHITE, colour.RED, colour.BLUE, colour.GREEN, colour.RED, colour.CWHITE, colour.RED,
    colour.GREEN,
    colour.YELLOW,
    colour.GREEN, colour.RED, colour.CWHITE, colour.RED, colour.GREEN)

# website facebook main page url
url = 'https://www.facebook.com/'
