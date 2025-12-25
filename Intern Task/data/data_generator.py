import random
import string
import requests

#generating random values to the input field 
#email
def random_email():
    domain="gmail.com"
    email_length=5
    random_string=''.join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email=random_string+"@"+domain
    return email
#name
def random_fname():
    return ''.join(random.choices(string.ascii_letters, k=6))
def random_lname():
    return ''.join(random.choices(string.ascii_letters, k=8))
#phone number
def random_number():
    return "98" + ''.join(random.choices(string.digits, k=8))

def random_password(length=10):
    specials = "!@#"
    all_chars = string.ascii_letters + string.digits + specials
    password = ''.join(random.choices(all_chars, k=length - 1))
    password += random.choice(specials)
    return ''.join(random.sample(password, len(password)))

#for detail page
role=["QA", "Developer", "Cyber security", "Trainer", "SEO"]
def random_role():
    return random.choice(role)
#random website
def random_website():
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{name}.com"
#random address
def random_address():
    street = ''.join(random.choices(string.ascii_lowercase, k=6))
    number = random.randint(1, 999)
    return f"{street} {number}"

def get_otp_from_guerrillamail(email):
    api_url = f"https://api.guerrillamail.com/ajax.php?f=fetch_email&email_address={email}&domain=sharklasers.com"
    
    # Make a GET request to fetch the emails
    response = requests.get(api_url)
    
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # Print the raw response content to help debug the issue
    
    if response.status_code == 200:
        try:
            data = response.json()  # Try parsing JSON
            emails = data.get('emails', [])
            
            if emails:
                latest_email = emails[0]  # Get the latest email
                email_id = latest_email['mail_id']
                
                # Get the content of the latest email
                email_content_url = f"https://api.guerrillamail.com/ajax.php?f=view_mail&mail_id={email_id}"
                email_content = requests.get(email_content_url).json()
                
                body = email_content.get('body', '')
                otp = extract_otp(body)
                return otp
            else:
                print("No emails found.")
                return None
        except ValueError as e:
            print(f"Error parsing JSON: {e}")
            return None
    else:
        print(f"Error fetching email: {response.status_code}")
        return None

def extract_otp(body):
    match = re.search(r"\b\d{6}\b", body)  # Regex for a 6-digit OTP
    if match:
        return match.group(0)
    else:
        print("OTP not found.")
        return None