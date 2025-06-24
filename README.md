# Inbox-Lead-Miner
A Python-based tool that connects to a Gmail inbox using the Gmail API, scans received messages, and extracts sender email addresses. Ideal for building lead lists for email campaigns. Helps automate prospecting by collecting emails of people who contacted you. Designed for ethical and permission-based marketing.

## What It Does
- Connects securely to your Gmail inbox using IMAP  
- Searches messages based on a custom query (e.g., specific sender or keyword)  
- Parses email content to extract email addresses using regex  
- Deduplicates results and exports them to a CSV file  
- Logs progress and supports early stopping for large inboxes  

## Setup Instructions

### 1. Clone the Repo
<pre>bash
git clone https://github.com/your-username/gmail-lead-extractor.git
cd gmail-lead-extractor</pre>

### 2. Install Python Dependencies
No external dependencies required — this script runs entirely on Python 3 and its standard library.

### 3. Enable Gmail IMAP and App Password
- Log in to your Gmail account and go to **Settings > See all settings > Forwarding and POP/IMAP**  
- Enable **IMAP access**  
- If you have 2-Factor Authentication enabled, generate an **App Password** via your Google Account under **Security > App passwords**

### 4. Configure Credentials
Open the script and replace the placeholders with your credentials and desired search criteria:

<pre>pythonEMAIL = "your-email@gmail.com"
PASSWORD = "your-app-password"
SEARCH_QUERY = '(FROM "example@example.com")</pre>

### 5. Run the Script
<pre>python extract_leads.py</pre>

### 6. Output
Extracted, deduplicated emails are saved to: **extracted_leads.csv**

### 7. Ethical Use & Disclaimer
This script is for ethical, permission-based email lead gathering only. Always comply with privacy laws (e.g., GDPR, CAN-SPAM). Do not use this tool to scrape or spam.

### 8. Notes
- The script processes up to 2500 emails by default (adjustable).
- Progress and error handling are included.
- Save interval set to 1000 emails for efficiency.

### License
MIT License

Made by Anoushka Singh

