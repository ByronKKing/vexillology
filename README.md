# Vexillology

This is a simple project pertaining to the vexillology subreddit (https://www.reddit.com/r/vexillology/). I grew frustated at visiting the subreddit and looking at all the interesting flags I'd never see again. I decided to write a python script to fix this. This project has two parts.

## API Call
The api-call.py script retrieves the 25 most up-voted flags (whether they are jpg or png files) and saves them to my computer. It also takes information about each post and logs it to a csv.

## Flag Generator
I create a dynamic ipython notebook (flag-generator.ipynb) that generates a random flag from those saved to my computer. I then have a script, random-flag.py, that generates an html page from the ipynb. The html page opens up in my browser when I run the script from the command line.

