#this script launches an html webpage in my browser for a random flag

import os

os.system("jupyter nbconvert --execute flag-generator.ipynb")

os.system("open flag-generator.html")


###send email with html attachment here!!!

