
@service
def test_notify():
    notify.mobile_app_oneplus_a6003(
       message = "Something happened at home!",
       data = { "actions": [
          {'action': 'ALARM', 'title': 'Sound Alarm'},
          {'action': 'URI', 'title': 'Open Url', 'uri': 'https://google.com'},
       ]}
    )