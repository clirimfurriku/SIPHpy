try:
    import requests
    import fake_useragent
    import subprocess
    import re
    import time
except:
    print('\n\nTo run is Required Termux:API')
    print('pkg install termux-api\n'
          'https://play.google.com/store/apps/details?id=com.termux.api&hl=en\n')
    print('To run is Required python')
    print('pkg install python\n')
    print('To run is Required requests library')
    print('pip install requests\n')
    print('To run is Required fake_useragent library')
    print('pip install fake_useragent\n')
    print('Please make sure you have everything set up')
    exit(404)

print('\n\nYou have to have phone number active on your phone\n'
      'Phone number format: 35569XXXXXXX')
phone_num = str(input('Enter your phone number: '))

url = 'https://api-mobile-vfal.vodafone.com/enterprise-resources/' \
      'public/identity/change-authentication-credentials/' + phone_num


def create_header(user_agent):
    header = {
        'Expect': '100-continue',
        'X-Unity-Version': '2018.3.0f2',
        'X-Application-OS': 'android',
        'X-Source-System': 'youth',
        'X-Source-Operator': 'youth',
        'Content-Type': 'application/json',
        'Accept-Language': 'al',
        'User-Agent': user_agent,
        'Host': 'api-mobile-vfal.vodafone.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    return header


def send_sms(header):
    global data, phone_num
    data = '{"details":{"credential-type":{"$":"pin","@list-agency-name":"Vodafone"}' \
           ',"username-text":{"$":"' + phone_num + '"},"pins":[{"$":""}]}}'
    the_result = requests.post(url, headers=header, data=data)
    print('Sending The SMS')
    print('Status: {} '.format(the_result.status_code))
    if str(the_result.status_code) != '200':
        print('Error while sending SMS')
        print('Trying again in 30 seconds')
        time.sleep(30)
        send_sms(header)



def read_sms():
    sms = subprocess.check_output('termux-sms-list', shell=True)
    pin = re.findall(r'(?:http://app.juth.al/pin/)([1-9A-Z]{5})', str(sms))[-1]
    print('Pin is {}'.format(pin))
    return pin


def send_pin(pin, header):
    global phone_num
    pin_url = 'https://api-mobile-vfal.vodafone.com/enterprise-resources/' \
              'public/identity/check-authentication-credentials'
    pin_data = '{"details":{"credential-type":{"$":"pin","@list-agency-name":"Vodafone"},' \
               '"username-text":{"$":"' + phone_num + '"},"pins":[{"$":"' + pin + '"}]}}'
    pin_result = requests.post(pin_url, headers=header, data=pin_data)
    print('Sending the PIN')
    print('Status: {} '.format(pin_result.status_code))


def check_success(pin, header):
    check_url = 'https://api-mobile-vfal.vodafone.com/public/' \
                'changeAuthenticationCredentialAPI/v2/authenticationCredential/check'
    check_data = '{"details":{"passwordText":"","usernameText":"' + phone_num + '","pin":[{"typeCode":"token","status":"","value":"' + pin + '"}],"validateCredentialResponse":"success/fail","credentialType":"social"},"parts":{"specification":{"characteristicsValue":[{"characteristicName":"clientId","value":"d2f86e561ef4f4cd96223134d671b1ef3c502349ac8b32e1c86927538a42edd0","type":""},{"characteristicName":"clientSecret","value": "3a9ef30ec7679273a7427455464d752d7be33d1da6a1425d1191ca614a8923db","type":""},{"characteristicName":"socialToken","value":"","type":"facebook"},{"characteristicName":"firstname","value":"John","type":""},{"characteristicName":"lastname","value":"Doe","type":""},{"characteristicName":"birthday","value":"20/02/1994","type":""}]}}}'
    success = requests.post(check_url, data=check_data, headers=header)
    print('Expecting status 400')
    print('Response of login was {} '.format(success.status_code))


if __name__ == '__main__':
    ua = fake_useragent.UserAgent()
    # proxy_list = [{'http': 'http://36.67.41.125:8080'},
    #               {'http': 'http://43.241.28.201:8080'},
    #               {'http': 'http://41.60.216.43:8080'}]
    i = 1
    # j = 0
    while True:
        # proxy = proxy_list[j]
        print('Sending SMS {} time'.format(i))
        useragent = ua.random
        header = create_header(useragent)
        send_sms(header)
        time.sleep(5)
        pin = read_sms()
        send_pin(pin, header)
        time.sleep(3)
        check_success(pin, header)
        time.sleep(30)
        i +=1
        # j +=1
        # if j == len(proxy_list):
        #     j = 0


# https://www.proxynova.com/proxy-server-list/elite-proxies/
# ([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})\s+([0-9]{1,4})

