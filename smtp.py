import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError


def send_transactional_email():
    try:
        # Initialize the client with your API key
        mailchimp = MailchimpTransactional.Client("md-I9eYTDIP1H14GujzTnCG5Q")

        # Define the message parameters
        message = {
            "from_email": "hello@warriortunes.com",
            "subject": "Hello from Mailchimp Transactional",
            "text": "This is a test email sent using Mailchimp Transactional API!",
            "to": [{"email": "terrillo@terrillo.com", "type": "to"}],
        }

        # Send the email
        response = mailchimp.messages.send({"message": message})
        print("Email sent successfully:", response)

    except ApiClientError as error:
        print("An error occurred: {}".format(error.text))


# Call the function to send the email
send_transactional_email()
