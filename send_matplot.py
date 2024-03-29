from blade.api_send import SendMsg, factory_send
import matplotlib.pyplot as plt


class SendMatplot(SendMsg):
    def __init__(self, args):
        self.title = args[0]
        self.x_lable = args[1]
        self.y_lable = args[2]
        self.path = args[3]
        self.last_x=0
        self.last_y=0

    def Initialization(self) -> bool:
        self.fig, self.axes = plt.subplots()
        self.axes.set_title(self.title)
        self.axes.set_xlabel(self.x_lable)
        self.axes.set_ylabel(self.y_lable)

    def Send(self, msg):
        if not (self.last_x == 0 and self.last_y == 0):
            self.axes.plot([self.last_x, msg['x']], [self.last_y, msg['y']] ,c='black')
        self.last_x = msg['x']
        self.last_y = msg['y']
        self.axes.scatter(msg['p_x'], msg['p_y'], c=msg['p_c'])
        self.fig.savefig(self.path+'/'+self.title)

    def DeInitialization(self): pass


factory_send['matplot'] = SendMatplot
