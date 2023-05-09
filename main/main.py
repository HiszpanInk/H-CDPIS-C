from tkinter import *
from kafka import KafkaConsumer
import json
# def importTrainDetailsFromFile():
#     f = open('example_data.json', encoding="utf-8")
#     data = json.load(f)
#     f.close()
#     return data['train_details']['departure_time'], data['train_details']['destination'], data['train_details']['train_number'], data['train_details']['train_name'], data['train_details']['via'], data['train_details']['delay'],

def importConfig():
    f = open('config.json')
    data = json.load(f)
    f.close()
    return data['connection_details']['topic'], data['connection_details']['ip_address']#, data['connection_details']['port']

def createFullscreenMainWindow():
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.attributes("-fullscreen", True)
    return root, width, height

#return deserialized json kafka message
def kafkaJsonMessageDeserialise(message):
    return json.loads(message.decode('ascii'))

#kafka consumer config
topic, ip_address = importConfig()
# consumer = KafkaConsumer(topic, value_deserializer = kafkaJsonMessageDeserialise, bootstrap_servers=[f"{ip_address}:{port}"])
consumer = KafkaConsumer(topic, bootstrap_servers=f"{ip_address}")

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

#preparing the data
#time, destination, train_number, train_name, via, delay = importTrainDetailsFromFile()

#preparing display
# root, width, height = createFullscreenMainWindow()
# defaultBackground = "#0000ff"
# defaultFontColor = "white"
# destination = destination.replace(" ", "\n")
# bigFontSize = int(height / 8) #from what I tested if we now multiply this value by 1.5 we have a height of one line of text
# smallFontSize = int(height / 16) 


# timeFrame = Frame(root, height = bigFontSize*1.5, width=int(width/4))
# timeFrame.configure(background=defaultBackground)
# timeFrame.pack_propagate(0)
# timeFrame.place(x=0, y=0)
# timeDisplay = Label(timeFrame, text = time, font=("Arial", bigFontSize), foreground=defaultFontColor)
# timeDisplay.configure(background=defaultBackground)
# timeDisplay.place(relx=0.5, rely=0.5, anchor=CENTER)

# trainNumberFrame = Frame(root, height=smallFontSize*1.5, width=int(width/4))
# trainNumberFrame.configure(background=defaultBackground)
# trainNumberFrame.pack_propagate(0)
# trainNumberFrame.place(x=0, y=bigFontSize*1.5)

# trainNumber = Label(trainNumberFrame, text = train_number, font=("Arial", smallFontSize), foreground=defaultFontColor)
# trainNumber.configure(background=defaultBackground)
# trainNumber.place(relx=0.5, rely=0.5, anchor=CENTER)

# destinationFrame = Frame(root, height=bigFontSize*4.5, width=(int(width/4)*3))
# destinationFrame.pack_propagate(0)  #this disables frame from getting biggger 
# destinationFrame.configure(background=defaultBackground)
# destinationFrame.place(x=int(width/4), y=0)
# destinationDisplay = Label(destinationFrame, text = destination, font=("Arial", bigFontSize), foreground=defaultFontColor)
# destinationDisplay.configure(background=defaultBackground)
# destinationDisplay.place(relx=0.5, rely=0.5, anchor=CENTER)

# viaFrame = Frame(root, height=height-(bigFontSize*4.5+smallFontSize*1.5), width=(int(width/4)*3))
# viaFrame.pack_propagate(0)  #this disables frame from getting biggger 
# viaFrame.configure(background=defaultBackground)
# viaFrame.place(x=(int(width/4)), y=bigFontSize*4.5)
# viaText = ""
# for station in via:
#     viaText += station
#     viaText += ", "
# viaText = viaText[:-2]
# viaDisplay = Label(viaFrame, text = viaText, font=("Arial", smallFontSize), foreground=defaultFontColor, wraplength=(int(width/4)*3))
# viaDisplay.configure(background=defaultBackground)
# viaDisplay.place(relx=0.5, y=0, anchor="n")

# delayFrame = Frame(root, height=smallFontSize*1.5, width=width)
# delayFrame.configure(background="white")
# delayFrame.pack_propagate(0)
# delayFrame.place(relx=0.5, rely=1, anchor="s")

# bottom_text = ""
# if train_name: 
#     bottom_text += "***"
#     bottom_text += train_name.upper()
#     bottom_text += "*** "
# if delay > 0:
#     bottom_text += str(delay) + " min opóźniony/delayed"
# if bottom_text:
#     delayDisplay = Label(delayFrame, text = bottom_text, font=("Arial", smallFontSize))
#     delayDisplay.configure(background="white")
#     delayDisplay.place(x=0, y=0)

# root.configure(background=defaultBackground)
# root.mainloop()