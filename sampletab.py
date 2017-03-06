import tkinter as tk

class SampleTab(tk.Frame):
    """

    """
    def __init__(self, master):
        super().__init__(master, session)
        self.master = master
        self.session = session
        self.sampleListFrame = tk.Frame(self)
        self.sampleList = tk.Listbox(self.sampleListFrame)
        self.sampleList.pack()
        #self.sampleButtons = tk.Frame(self)
        self.addSampleButton = tk.Button(self.sampleListFrame,
            text='Add Sample')
        self.addSampleButton.pack(fill='x')
        self.renameSampleButton = tk.Button(self.sampleListFrame,
            text='Rename Sample')
        self.renameSampleButton.pack(fill='x')
        self.removeSampleButton = tk.Button(self.sampleListFrame,
            text='Remove Sample')
        self.removeSampleButton.pack(fill='x')
        self.sampleListFrame.pack(side='left')
        return None

        def update(self):
            """

            """
            return None

