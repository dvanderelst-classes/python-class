import tkinter as tk
import random
import time

def list2str(lst):
    out = ''
    for x in lst: out+=str(x) + ','
    out = out.rstrip(',')
    return out

class ExperimentApp:
    def __init__(self, master,settings):
        # Define widgets
        self.master = master
        self.label = tk.Label(master, text = "Press Enter To Start",background='white',font=("Helvetica", 16))
        # Pack widgets
        self.label.pack(fill=tk.BOTH,expand=1)

        #Bind event
        self.master.bind('<Return>',self.run_experiment)
        
        #Get data
        self.key = None
        self.rt = None
        self.word = None
        self.type = None
        self.length = None
        self.subject = settings['subject']
        self.present_time = time.time()
        self.current_index = 0
        self.settings = settings
        self.stimuli = settings['stimuli']
    
    def set_stimulus(self):
        stimulus = self.stimuli[self.current_index]
        self.word = stimulus[0]
        self.length = stimulus[1]
        self.type = stimulus[2]
        self.label['text'] = self.word
        self.present_time = time.time()
        self.master.update_idletasks()
        
    def get_response_button(self,event):
        self.rt = int((time.time() - self.present_time)*1000)
        self.key = event.keysym
    
        color = 'green'
        if self.key == 'l' and self.type == 'negative': color = 'red'
        if self.key == 'a' and self.type == 'positive': color = 'red'

        data = [time.asctime(), self.subject, self.word, self.length, self.type, self.key, self.rt, color]
        line = list2str(data)
        #f = open('data_'+self.subject+'.txt','a')
        f = open('data.txt','a')
        f.write(line+'\n')
        f.close()
        
        self.label['background'] = color
        self.master.update_idletasks()
        time.sleep(1)
        self.label['background'] = 'white'
        self.master.update_idletasks()
        
        self.current_index = self.current_index + 1
        if self.current_index < len(self.stimuli):
            self.set_stimulus()
        else:
            self.label['text'] = 'END OF EXPERIMENT'
            self.master.unbind('<a>')
            self.master.unbind('<l>')
    
          
    def run_experiment(self,event):
        print('Starting experiment')
        self.master.unbind('<Return>')
        self.master.bind('<a>',self.get_response_button)
        self.master.bind('<l>',self.get_response_button)
        self.set_stimulus()
        
#Get some infor from the user
settings = {}
settings['subject'] = 'TEST'
settings['subject'] = input('Subject:')
 
#Read stimuli
f = open('stimuli.txt')
txt = f.readlines()
f.close()
stimuli = []
for x in txt:
    x = x.replace('\n','')
    x = x.split(' ')
    stimuli.append(x)
random.shuffle(stimuli)
print(stimuli)
settings['stimuli'] = stimuli

root = tk.Tk()
w = 500
h = 250 
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

app = ExperimentApp(root,settings)
root.mainloop()