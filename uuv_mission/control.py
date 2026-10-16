class Controller:
    
    def __init__(self, Kp: float = 0.15, Kd: float = 0.6,init_error: float = 0.0):
        #This shall outline the proportional and derivative gains for the controller
        self.Kp = Kp
        self.Kd = Kd
        self.prev_error = init_error

    def __call__ (self, observation: float, reference: float) -> float:
        #This function will calculate the control output based on the current error and time step
        
        e_Curr = reference - observation #Calculate the current error based on the reference and observation

        output = self.Kp * e_Curr + self.Kd * (e_Curr - self.prev_error) #Calculate the control output based on the proportional and derivative gains
        self.prev_error = e_Curr
        return output

    