class State:
    def __init__(self):
        self.z = 0
    def __str__(self):
        return '%.4f' % self.z

def computeControl(self,od,z,time=0.0):
    if z == None:
        z = State()
    #calculate control
    err_sig = 1000*(od-self.cparams['setpoint'])
    z.z = z.z+err_sig*self.cparams['ki']
    if z.z<0:
        z.z = 0
    if z.z>self.cparams['maxdilution']:
        z.z = self.cparams['maxdilution']
    
    u = z.z+err_sig*self.cparams['kp']
    if u < self.cparams['mindilution']:
        u = self.cparams['mindilution']
    if u > self.cparams['maxdilution']:
        u = self.cparams['maxdilution']
    u = int(u) # make sure u is an int
    
    return (u,z)
