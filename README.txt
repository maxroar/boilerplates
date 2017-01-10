This directory is a collection of boilerplates to use for web development. I have also included instructions to create aliases for the boilerplates and example alias code.

----------------------------------------------

Note: The path in the script should be changed to wherever you store the template files. The files can be edited to reflect your preferences.

Installing the bash.rc file:
1. navigate to your home directory: 'cd ~'
2. check to see if you have a bash alias file already
  a. 'ls -a'
  b. Linux/Unix: look for a file called '.bashrc'
  c. Mac: look for a file called '.bash_profile'
  d. if the file does not exist create it (include the dot before the file name)
  e. copy the text at the bottom of this file into the hidden file
    -NOTE: be sure to change the file path to the location of your template files!
    -NOTE: be sure to change "atom" to the name of your text editor. If you prefer not to open the directory after copying over the files, delete everything from "&&" on for that line.
Use: the alias on the left can be set to anything. The right side is the actions executed by the terminal when the alias is typed

Alias examples
-----------------------------------------------------
#HTML: copies a linked index.html, style.css, and script.js. jQuery is also included in the HTML head
alias html="cp ~/gitHub/snips/index.html . && cp ~/gitHub/snips/style.css . && cp ~/gitHub/snips/script.js ."
#Python/Flask: copies index.py, static dir, and templates/index.html. Static contains css/style.css, js/script.js, and img dir. All files are properly linked in index.html and index.py
alias pyflask="cp -r ~/boilers/python/flask/* . && atom ."
