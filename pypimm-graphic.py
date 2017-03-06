import tkinter as tk
import tkinter.ttk as ttk
import sampletab
import analysistab
import characterizationtab

def main():
    root = tk.Tk()
    root.title('PyPIMM')
    app = PyPimmApplication(root)
    app.mainloop()

class PyPimmApplication(tk.Frame):
    """

    """
    def __init__(self, master):
        # establish self in root
        super().__init__(master)
        self.master = master
        self.pack()
        # establish notebook panels
        self.notebook = ttk.Notebook(self)
        self.sampleTab = sampletab.SampleTab(self.notebook)
        self.analysisTab = tk.Frame(self.notebook)
        self.characterizationTab = tk.Frame(self.notebook)
        self.notebook.add(self.sampleTab, text='Manage Samples')
        self.notebook.add(self.analysisTab, text='Analyze Waveforms')
        self.notebook.add(self.characterizationTab,
            text='Characterize samples')
        self.notebook.pack()

        self.b=tk.Button(self,text='blern')
        self.b.pack()

if __name__ == '__main__':
    main()
