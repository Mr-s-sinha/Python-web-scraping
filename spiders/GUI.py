from tkinter import *
from spiders import amazon

from spiders import ML


class GUI1:
    def __init__(self):
        window = Tk()
        window.title("Search Window")

        self.searchFrame = Frame(window)
        self.searchFrame.pack()

        self.next = Button(self.searchFrame, text = "Predict", command = self.predictions)
        self.next.pack()

        self.searchLabel =Label(self.searchFrame, text = "Enter topic to search:")
        self.searchLabel.pack()

        self.pred = Label(self.searchFrame, text = "Make your Predictions")

        self.searchString = StringVar()
        self.searchEntry = Entry(self.searchFrame, textvariable = self.searchString)
        self.searchEntry.pack()

        self.searchButton = Button(self.searchFrame, text = "Click to Search", command = self.searchTopic)
        self.searchButton.pack()

        self.left_outer = Frame(self.searchFrame, bd =5)
        self.left_outer.pack(side = TOP, fill = Y, pady = 10, padx = 30)

        self.amazonblock = Text(self.left_outer,width=400,height=400,wrap=NONE)
        self.amazonblock.pack(side=TOP, fill=Y)

        self.scroll2 = Scrollbar(self.left_outer, orient = HORIZONTAL,command=self.amazonblock.xview())
        self.scroll1 = Scrollbar(self.left_outer, orient = VERTICAL,command=self.amazonblock.yview())

        self.amazonblock.configure(xscrollcommand=self.scroll2.set)
        self.amazonblock.configure(yscrollcommand=self.scroll1.set)

        self.scroll1.pack(side=RIGHT,fill=Y)
        self.scroll2.pack(side=BOTTOM,fill=X)

        self.closeButton = Button(text = "Close", command = window.destroy)
        self.closeButton.pack()

        window.geometry("700x700")
        window.mainloop()

    def predictions(self):
        next()

    def searchTopic(self):

        searchQuery = self.searchString.get()
        AmazonQuery = amazon.search1(searchQuery)

        if AmazonQuery == None:
            self.amazonblock.insert(END,"TRY AGAIN")
        else:
            self.amazonblock.insert(END,AmazonQuery)
            self.amazonblock.config(state=DISABLED)

class next:
    def __init__(self):
        window = Tk()
        window.title("Search Window")

        self.searchFrame = Frame(window)
        self.searchFrame.pack()

        self.processor = Label(self.searchFrame, text = "Enter your Processor..(for i3 = 0, i5 = 1, i7= 2)")
        self.processor.pack()

        self.process = IntVar()
        self.searchEntry = Entry(self.searchFrame, textvariable = self.process)
        self.searchEntry.pack()

        self.screen = Label(self.searchFrame, text = "Enter screen size 15.6 or 14")
        self.screen.pack()

        self.screensize = IntVar()
        self.searchEntry1 = Entry(self.searchFrame, textvariable = self.screensize)
        self.searchEntry1.pack()

        self.gen = Label(self.searchFrame, text = "Enter Generation 6,7,or 8")
        self.gen.pack()

        self.generation = IntVar()
        self.searchEntry2 = Entry(self.searchFrame, textvariable = self.generation)
        self.searchEntry2.pack()

        self.ram = Label(self.searchFrame, text = "Enter ram 4 or 8")
        self.ram.pack()

        self.RAM = IntVar()
        self.searchEntry3 = Entry(self.searchFrame, textvariable = self.RAM)
        self.searchEntry3.pack()

        self.hd = Label(self.searchFrame, text = "Enter Harddisk")
        self.hd.pack()

        self.HD = IntVar()
        self.searchEntry4 = Entry(self.searchFrame, textvariable = self.HD)
        self.searchEntry4.pack()


        self.finalButton = Button(self.searchFrame, text= 'search', command = self.searchFinal)
        self.finalButton.pack()

        self.show = Text(self.searchFrame,wrap=NONE)
        self.show.pack()

        window.geometry("700x700")
        window.mainloop()

    def searchFinal(self):
        processor = self.process.get()
        screensize = self.screensize.get()
        generation = self.generation.get()
        ram = self.RAM.get()
        hd= self.HD.get()

        list1 = [processor, screensize, generation, ram, hd]
        answer = ML.run(list1)

        if answer == None:
            self.show.insert(END,"TRY AGAIN")
        else:
            self.show.insert(END,answer)

if __name__ == "__main__":
    obj = GUI1()
