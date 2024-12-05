## SMTP Server Using Gmail

This project demonstrates how to set up an SMTP server using Gmail to send emails with Python. The project uses Flask for the web interface and smtplib for email sending.

## Prerequisites
Python 3.x

Flask

pyotp

Gmail account with "Less secure app access" enabled or an App Password

## Installation
### 1. Clone the Repository:


```sh

git clone https://github.com/Kingisline/SMTP-Server-Using-Gmail.git

```
## 

### 2. Create and Activate Virtual Environment (optional but recommended):


```sh

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```
##

### 3. Install Required Packages:


```sh

pip install flask pyotp
```
##

### Configuration
Update the app.py file with your SMTP server details:

```sh
python
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'

# 
```

## Usage
### 1.Run the Flask Application:


```sh
python app.py
```

### 2.Access the Web Interface: Open your browser and navigate to http://127.0.0.1:5000/.


### 3.Send OTP:

Enter your email address and click "Send OTP".

Check your email for the OTP.

### 4.Verify OTP:

Enter the OTP you received in your email and click "Verify OTP".

##

### Contributing
Feel free to fork this repository, make your changes, and submit a pull request.

##

### License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to adapt this README to better fit your project and preferences! If you have any questions or need further assistance, just let me know.

### Youtube Link
[How To Set Up Gmail SMTP Server](https://youtu.be/iMIKWFP4tRg)

