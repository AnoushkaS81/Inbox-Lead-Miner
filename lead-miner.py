import imaplib
import email
import re
import csv

EMAIL = "you-email"
PASSWORD = "app-password"
IMAP_SERVER = "imap.gmail.com"
FOLDER = "inbox"
SEARCH_QUERY = '(FROM "custom-query")'
OUTPUT_FILE = "extracted_leads.csv"
SAVE_INTERVAL = 1000 

def extract_emails_from_text(text):
    return re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

def connect_and_fetch():
    print("Connecting to email server...")
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select(FOLDER)

    print(f"Searching for emails with query: {SEARCH_QUERY}")
    status, messages = mail.search(None, SEARCH_QUERY)
    if status != "OK":
        print("Error searching inbox.")
        return

    email_ids = messages[0].split()
    print(f"Found {len(email_ids)} emails.")

    seen = set()

    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Email"])
        
        for i, e_id in enumerate(email_ids, 1):
            try:
                status, msg_data = mail.fetch(e_id, '(RFC822)')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        body = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body += part.get_payload(decode=True).decode(errors='ignore')
                        else:
                            body = msg.get_payload(decode=True).decode(errors='ignore')

                        extracted = extract_emails_from_text(body)
                        for em in extracted:
                            if em not in seen:
                                writer.writerow([em])
                                seen.add(em)
            except Exception as e:
                print(f"⚠️ Error processing email {i}: {e}")

            if i % 100 == 0:
                print(f"Processed {i} emails...")

            
            if i >= 2500:
                 print("🚫 Stopping early after 2500 emails.")
                 break

    print(f"✅ Done. Saved {len(seen)} unique emails to {OUTPUT_FILE}")

# === RUN SCRIPT ===
connect_and_fetch()
