import pywhatkit as kit
from datetime import datetime, timedelta

# === CONFIGURATION ===
phone_number = "+918122840059"  # Replace with recipient's WhatsApp number
message = "Hi, this is an automated reminder of the tasks due week."

# === TIME SETTINGS ===
# Send message 2 minutes from now (so you have time to log in to WhatsApp Web)
now = datetime.now() + timedelta(minutes=1)
hour = now.hour
minute = now.minute

# === SEND MESSAGE ===
try:
    kit.sendwhatmsg(phone_number, message, hour, minute)
    print(f"Message scheduled to {phone_number} at {hour}:{minute}")
except Exception as e:
    print(f"Failed to send message: {e}")
