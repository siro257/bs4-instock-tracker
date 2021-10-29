import os
import smtplib
from datetime import datetime

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


def send_mail(product_name, product_price, product_url):

    now = datetime.now().strftime('%H:%M:%S %D')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = f'{product_name} ::: INSTOCK!'
        body = f'{product_name} is instock! ({now})\nPrice: {product_price}\nURL: {product_url}'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
