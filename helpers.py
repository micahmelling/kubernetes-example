import yagmail
import ast

from ds_helpers import aws


def send_prediction_email():
    """
    Sends email report with prediction information.
    """
    email_dict = aws.get_secrets_manager_secret('churn-email')
    username = email_dict.get('username')
    password = email_dict.get('password')
    yag = yagmail.SMTP(username, password)
    recipients = email_dict.get('recipients')
    recipients = ast.literal_eval(recipients)
    subject = 'Redis Test'
    contents = ':-)'
    yag.send(to=recipients, subject=subject, contents=contents)
