import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

# SMTP configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'raja88guru@gmail.com'  # TODO replace with sender mail id
SENDER_PASSWORD = 'snqv efsc uhri cwqu'  # TODO Google mail account app password

PDF_FILE = 'D:\\NEURAL NEETWORK PROJECT DS\\Rajaguru_QA_Test_Engineer_Resume.pdf'  # TODO Path to PDF file

# Load recipients from CSV
def load_recipients(csv_file):
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except Exception as e:
        print(f"Error loading recipients: {e}")
        return []

# Create email with PDF attachment
def create_message(to_email):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = 'Enthusiastic Automation Tester with 4+ Years of Experience Interested in Software Testing Position'

    # Email body
    body = """Hi,

I'm thrilled to connect with you regarding the Automation Tester role, which I discovered on Naukri. With over 4+ years of software testing experience, I’m confident that my skills align perfectly with your requirements.

For more information, please find my details below, and my resume is attached for your review.

Total Experience: 4.5 years
Relevant Experience: 4.5 years
Current CTC: 4.4LPA
Expected CTC: 7LPA
Current Location: Chennai
Willing to relocate: Yes
Notice Period: Less than 60 days
Anticipated join date: Less than 60 days
Availability to work from Office: Yes

You can reach me at [], and I am just a phone call away for any discussions or clarifications.

Best regards,
Rajaguru S
"""
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF
    try:
        with open(PDF_FILE, 'rb') as f:
            pdf = MIMEApplication(f.read(), _subtype='pdf')
            pdf.add_header('Content-Disposition', 'attachment', filename=os.path.basename(PDF_FILE))
            msg.attach(pdf)
    except Exception as e:
        print(f"Error attaching PDF: {e}")

    return msg

# Send all emails
def send_bulk_emails(recipients):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            for person in recipients:
                email = person.get('email')
                if not email:
                    print(f"Skipping recipient with missing email: {person}")
                    continue
                msg = create_message(email)
                try:
                    server.send_message(msg)
                    print(f"Sent to: <{email}>")
                except Exception as e:
                    print(f"Failed to send to {email}: {e}")
    except Exception as e:
        print(f"SMTP error: {e}")

if __name__ == '__main__':
    recipients = load_recipients('D:\\NEURAL NEETWORK PROJECT DS\\mail_id_list.csv')  # TODO mail id list file path
    if recipients:
        send_bulk_emails(recipients)
    else:
        print("No recipients loaded.")
