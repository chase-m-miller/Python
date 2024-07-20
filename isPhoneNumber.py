import re  # import regular expression functionality


def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    match = phoneNumRegex.match(text)
    return bool(match)


phoneNum = '123-425-1231'
ssNum = '123-51-5231'
print('Is ' + phoneNum + ' a phone number?')
print(isPhoneNumber(phoneNum))
print('Is ' + ssNum + ' a phone number?')
print(isPhoneNumber(ssNum))
