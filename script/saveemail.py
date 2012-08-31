import email, getpass, imaplib, os
import datetime
import unicodedata
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "../settings")
import sys
cmd_folder = os.path.realpath("../")
sys.path.append(cmd_folder)
from emails.models import Email






exist = True


detach_dir = '' # directory where to save attachments (default: current)
#put your username here
user = "toto"
#put your password here
pwd = "titi"

# connecting to the gmail imap server
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)
m.select("[Gmail]/All Mail") # here you a can choose a mail box like INBOX instead
# use m.list() to get all the mailboxes

resp, items = m.search(None, "ALL") # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
items = items[0].split() # getting the mails id
i = 0
for emailid in items:
    i += 1
    if i > 25911:

      
        resp, data = m.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
        email_body = data[0][1] # getting the mail content
        mail = email.message_from_string(email_body) # parsing the mail content to get a mail object
        print i
        try :
            print "["+mail["From"]+"] :" + mail["Subject"]

        except :
            try :
                print "["+mail["From"]+"] :"
            except :
                pass

        content =  unicode(mail.__str__(),errors='ignore')
        mailsave =  Email()
        mailsave.Sender = mail["From"]
        mailsave.Content = content
        mailsave.Title = mail["Subject"]
        mailsave.save()
        if mail.get_content_maintype() != 'multipart':
            continue

        
        # we use walk to creatone a generator so we can iterate on the parts and forget about the recursive headach
        j = 0
        for part in mail.walk():
            # multipart are just containers, so we skip them
            if part.get_content_maintype() == 'multipart':
                continue

            # is this part an attachment ?
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            counter = 1

            # if there is no filename, we create one with a counter to avoid duplicates
            if not filename:
                filename = 'part-%03d%s' % (counter, '.bin')
                counter += 1

            att_path = os.path.join(detach_dir, filename)

            #Check if its already there
            att_path = att_path.replace("?","")
            att_path = att_path.replace("=","")
            att_path = att_path.replace(" ","")
            att_path = att_path.replace(".\\\\","")
            att_path = att_path.replace("\\","")
            att_path = att_path.replace("/","")
            att_path = att_path.replace("bin",".bin")
            
            #att_path = ".\\\\"+att_path
            try :
                # if not os.path.isfile(att_path) :
                    # finally write the stuff
                filee = "__%d_%d__"%(i,j)
                emailcouch.put_attachment(part.get_payload(decode=True),att_path+filee+att_path[3:])
            except :
                pass