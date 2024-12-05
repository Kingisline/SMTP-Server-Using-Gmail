from flask import Flask, request, render_template_string
import pyotp
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  #465 or 587
EMAIL_ADDRESS = 'callmeasgooduser@gmail.com'
EMAIL_PASSWORD = 'cult zzvv gijt lxgz'

# Generate OTP
totp = pyotp.TOTP(pyotp.random_base32())

# Send OTP via email
def send_otp_via_email(recipient, otp):
    msg = MIMEText(f'Your OTP is: {otp}')
    msg['Subject'] = 'Your OTP Code'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

@app.route('/')
def home():
    return render_template_string('''
        <form method="post" action="/send-otp">
            Email: <input type="email" name="email" required>
            <input type="submit" value="Send OTP">
        </form>
    ''')

@app.route('/send-otp', methods=['POST'])
def send_otp():
    email = request.form['email']
    otp = totp.now()
    send_otp_via_email(email, otp)
    return render_template_string('''
        <p>OTP sent to your email. Please check your inbox.</p>
        <form method="post" action="/verify-otp">
            Enter OTP: <input type="text" name="otp" required>
            <input type="submit" value="Verify OTP">
        </form>
    ''')

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    otp = request.form['otp']
    print(otp)
    if totp.verify(otp):
        return 'OTP verified successfully!'
    else:
        return 'Invalid OTP. Please try again.', 401

if __name__ == '__main__':
    app.run(debug=True)
