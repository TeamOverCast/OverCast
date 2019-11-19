from Tkinter import *
def window():
   OCWindow = Tk()
   OCWindow.title("Over Cast")
   sampleText = Label(OCWindow, text="This is just some sample text")
   sampleText.pack()
   sizeSettings = Canvas(OCWindow, bg="grey", height=900, width=900)
   sizeSettings.pack()
   OCWindow.mainloop()