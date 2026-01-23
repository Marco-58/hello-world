import time
import datetime
import inspect
from arduino.app_utils import App

print("TROVAMI")
print("----------------Prove Python -----------------------")
now = datetime.datetime.now()
print(now)
print (time.localtime())
# for name, data in inspect.getmembers(datetime):
   # print( name)
   # print(data)
#     if name.startswith("__"):
#         continue
#     #if 'class' in str(data):


App.run()
