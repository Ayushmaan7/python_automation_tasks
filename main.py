# Import required libraries
from twilio.rest import Client
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

# -----------------------------------------
# 1. Send SMS using Twilio API
# -----------------------------------------

def send_sms():
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello! This is a test message sent via Python.",
        from_='+1234567890',  # Twilio phone number
        to='+0987654321'  # Your phone number
    )

    print(f"SMS sent: {message.sid}")

# -----------------------------------------
# 2. Send WhatsApp Message using Twilio API
# -----------------------------------------

def send_whatsapp():
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello! This is a test WhatsApp message sent via Python.",
        from_='whatsapp:+14155238886',  # Twilio WhatsApp sandbox number
        to='whatsapp:+0987654321'  # Your WhatsApp number
    )

    print(f"WhatsApp message sent: {message.sid}")

# -----------------------------------------
# 3. Send Email using SMTP (via Gmail)
# -----------------------------------------

def send_email():
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    password = "your_email_password"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Test Email from Python"

    body = "Hello! This is a test email sent via Python."
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

    print("Email sent successfully!")

# -----------------------------------------
# 4. Post on Instagram using Instagram Graph API
# -----------------------------------------

def post_on_instagram():
    access_token = 'your_access_token'
    instagram_user_id = 'your_instagram_user_id'
    image_url = 'https://example.com/path-to-your-image.jpg'
    caption = 'Hello! This is a test post from Python.'

    # Step 1: Upload Image to Instagram
    upload_url = f'https://graph.facebook.com/v16.0/{instagram_user_id}/media'
    image_upload_params = {
        'image_url': image_url,
        'caption': caption,
        'access_token': access_token
    }

    upload_response = requests.post(upload_url, data=image_upload_params)
    media_id = upload_response.json().get('id')

    # Step 2: Publish the uploaded media
    publish_url = f'https://graph.facebook.com/v16.0/{instagram_user_id}/media_publish'
    publish_params = {
        'creation_id': media_id,
        'access_token': access_token
    }

    publish_response = requests.post(publish_url, data=publish_params)
    print(f"Instagram post published: {publish_response.json()}")

# -----------------------------------------
# Run all tasks
# -----------------------------------------

if __name__ == "__main__":
    print("Sending SMS...")
    send_sms()
    
    print("\nSending WhatsApp message...")
    send_whatsapp()
    
    print("\nSending Email...")
    send_email()
    
    print("\nPosting on Instagram...")
    post_on_instagram()
