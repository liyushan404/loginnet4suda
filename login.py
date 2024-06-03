import socket
import urllib.request
import urllib.parse


def login(username, password, userip):

    url_4 = 'http://10.9.1.3:801/eportal/?c=Portal&a=login&callback=dr1004&login_method=1&user_account=%2Cb%2C{0}&user_password={1}&wlan_user_ip={2}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.3&v=8766'.format(username, password, userip)
    
    urllib.request.urlopen(url_4).read()



if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    # 账户，密码
    login('20235227130@cucc', "072464li", ip)
