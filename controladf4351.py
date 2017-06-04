import subprocess
class controlADF:
   def __init__(self,power_main=0,power_aux=0,freq_main=35,freq_aux=None,app_path='adf4351'):
      self.power_main = power_main
      self.power_aux = power_aux
      self.freq_main = freq_main
      self.freq_aux =  freq_aux
      self.app_path = app_path
      self.run_result = '' 
    def run_app(self):
      try:
         res =  subprocess.check_output("./adf4351","-f",self.freq_main,"-p",power_main)
         print(res.otput)
      except subprocess.CalledProcessError as err:
         print('ERROR:')
         print('return code:',err.returncode) 
         print('details:',err.output) 
       

     
class ADFrontCLI:
   def __init__(self):
     pass

   def build_args(self):
     pass 

   def run(self):
     pass   

class ADFrontNet:
   pass
