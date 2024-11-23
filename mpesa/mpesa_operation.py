# import requests
# import base64
# from datetime import datetime
# from requests.auth import HTTPBasicAuth

# # Credentials
# shortcode = '601426'
# shortcode_password = 'Chocolatefresher@006'
# shortcode_key = 'YourShortcodeKey'
# access_token = 'YourAccessToken'

# # API endpoint for STK Push
# url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

# # Headers
# headers = {
#     'Authorization': 'Bearer ' + access_token,
#     'Content-Type': 'application/json'
# }

# # Request Payload
# payload = {
#     "BusinessShortcode": shortcode,
#     "LipaNaMpesaOnlineShortcode": shortcode,
#     "LipaNaMpesaOnlineShortcodePassword": shortcode_password,
#     "PhoneNumber": 'YourCustomerPhoneNumber',  # e.g., 2547XXXXXXXX
#     "Amount": 100,  # Amount to pay
#     "AccountReference": 'YourAccountReference',
#     "TransactionDesc": 'Payment for products/services'
# }

# # Send the request to M-Pesa API
# response = requests.post(url, json=payload, headers=headers)


# print(response.text)
