"""
OUCI Automation Project: Data gathering

Pull information from emails sent to ouci@ou.edu

Separate emails into categories:
    Tuition
    Transportation
    Registration Payment
    Form Entry:
        
"""
def getEmailData(recipient):
    import win32com.client
 
    # Access Outlook application
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    
    # Define recipient. In this case, I needed to access a folder other than
    # the default (which is my personal email). 
    recip = outlook.CreateRecipient(recipient)
    
    # Access the Inbox of recip. 6 refers to the inbox
    inbox = outlook.GetSharedDefaultFolder(recip, 6)
    
    # read in raw emails (comes in as a list)
    messages = inbox.Items
    dataArray = []

    # Iterate through emails and gather pertinent information
    for i in range(0,len(messages)):
        try:
            #
            if str(messages[i].Sender) == "ouci@ou.edu":
                time = str(messages[i].CreationTime)
                cat = "Payment"
                sub = str(messages[i].Subject)
                body = str(messages[i].body)
        
                dataArray.append([time,cat,sub,body])
                
            elif str(messages[i].Sender) == "forms@formbldr.com":
                time = str(messages[i].CreationTime)
                cat = "Registration"
                sub = str(messages[i].Subject)
                body = str(messages[i].body)
        
                dataArray.append([time,cat,sub,body])
            else:
                continue
        except AttributeError:
            continue
        
    dataArray.sort(reverse=True)
    return dataArray