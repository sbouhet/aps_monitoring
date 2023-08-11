import argparse
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import os
from aps_api import apsMonitoring

def send_notification(key,text_subject,text_body,color):

    url = 'https://www.pushsafer.com/api'
    post_fields = {
        "t": text_subject,
        "m": text_body,
        "i": 1,
        "c": color,
        "d": 'a',
        "u": 'https://www.apsema.com/ema/index.action',
        "ut": 'AP Systems',
        "k": key,
    }

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()

    print('Notification sent: '+json)

if __name__ == '__main__':

    parser = argparse.ArgumentParser("aps monitoring")
    parser.add_argument(
        '--action',
        default='check',
        action='store',
        choices=['check'],
        help='Define action'
    )

    parser.add_argument('--notification', action='store_true')
    parser.add_argument('--no-notification', dest='notification', action='store_false')
    parser.set_defaults(notification=True)

    parser.add_argument(
        '--username',
        default='',
        help='The APS username'
    )

    parser.add_argument(
        '--pwd',
        default='',
        help='The APS password'
    )

    parser.add_argument(
        '--notifier_key',
        default='',
        help='The notifier key'
    )

    args = parser.parse_args()

    print("Action:"+args.action)
    print("Username:"+args.username)
    print("Password:"+args.pwd)
    print("Notifier key:"+args.notifier_key)
    print("Notification:"+str(args.notification))

    aps = apsMonitoring()

    if args.action == 'check':
        power_data = aps.get_power_values(args.username, args.pwd)
        if power_data['lastPower'] == 0 and power_data['today'] == 0:
            print("No power data retrieve")
            if (args.notification):
                send_notification(args.notifier_key,'APS monitoring FAILED', 'No power data', '#FF0000')
        else:
            output = "last power=" + power_data['lastPower'] + " today=" + power_data['today']
            print(output)
            if (args.notification):
                send_notification(args.notifier_key,'APS monitoring OK',output,'#00FF00')
