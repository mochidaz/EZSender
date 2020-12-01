from main import *
from config_parser import *

parser = ParseConfig("EZConfig/config")

mailist = parser.get_mailist() # Set Mailist File

subject = parser.get_subject() # Set Subject

from_name = parser.get_name() # Set From Name Sender

from_email = parser.get_email() # Set From Email Sender

letter = parser.get_letter() # Set HTML Letter File

random_link = eval(parser.get_random_link()) # Set random link

setDelay = parser.get_delay() # Set delay

ezsettings = {

 "smtpHost":parser.get_smtp_host(), # your server/host smtp
 "smtpPort":parser.get_smtp_port(), # your port smtp (ex:587)
 "smtpUser":parser.get_smtp_user(), # your smtp Username
 "smtpPass":parser.get_smtp_pass(), # your smtp Password

}

app = EZSender(mailist, subject, from_email, from_name, letter, random_link, ezsettings, setDelay)
app.EZSend()


