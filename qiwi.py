from urequests import get


class QiwiDonate(object):

    def __init__(self, token):
        self.url = 'https://donate.qiwi.com/api/stream/v1/widgets/{}/events?&limit=1'.format(token)

    def get_donate(self):
        try:
            jo = get(self.url).json()
        except Exception as e:
            return e

        if 'description' in jo:
            return jo['description']

        if 'events' in jo and jo['events']:
            if jo['events'][0]['type'] == 'DONATION':
                return (jo['events'][0]['attributes']['DONATION_SENDER'],
                        jo['events'][0]['attributes']['DONATION_MESSAGE'],
                        jo['events'][0]['attributes']['DONATION_AMOUNT'])
        return None