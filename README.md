# Name of Project: easyhtml
HTML is easy but is filled with too much unnecessary syntax.So here's an alternative.

#Pre-requisites:Python3 and pip3

#note:It is suggested to use a linux enviornment but it may pose no problem on an other operating system as well.

#Project By: Apoorv Bedmutha
initial commit on:13 sept 2020
Contact:bedmuthapoorv@gmail.com

What is the use of easyhtml?

html is a fairly easy language but the fact that it has too much of un necessary syntax load on developer makesd it really annoying and time consuming.
I mean who doesn't hate tags.
So what easy html does is it takes simpler commands and converts them into an HTML file and CSS File with autogenerated code,So that you as a developer does not 
have to waste time on the syntax and rather just edit the code as per your requirements.
easyhtml saves time amd effort which you you can rather invest in more crucial stuff rather than HTML.

How to setup easyhtml?

step 1:
open https://github.com/apoorvbedmuthaprojects/easyhtml in your browser

step 2:
click the green "Code" icon

step 3:
click download ZIP

step 4:
now you may find the easyhtml-master.zip file in your downloads folder.Extract the zip file

step 5:
now you will find a easyhtml-master folder.

step 6:
now move over to the terminal and type 
pip3 install html5print

step 7:
Setup complete.

How to use easyhtml?

let's start with basic stuff,that will give you an idea about how the tool works.
we will create a simple hello world HTML file.

so open your terminal
and move into your easyhtml-master using cd
now type 

python3 easyhtml.py

this will start the program,you may see a blinking cursor on your terminal.
now type 

Hello World

press enter

and then type

###
and press enter
That's it,it's that simple.You may have noticed that the program has exited,that means we should have our HTML file ready.

open your easyhtml-master file
open the index.html file in a text editor like notepad or gedit.
you must see the html code now.
that's how you use this tool.
You may also have noticed as soon as we typed 

###

the program exited.So whenever you are done with your commands just type ### and the program will convert your commands to html and css.

okay, moving forward I want you to open the Commands List file.
You may see several words on each line
each line shows different commands that can be used in the program.
Now basically there are 3 types of commands that the program supports
1. commands starting with add
2. commands starting with end
3. commands that start directly
Now to simplify stuff,
commands starting with add are equivalent to adding new component in the code

example:
add img image_name.png

this command will add an image named image_name.png into the html code

similarly commands starting with end are equivalent to closing tags in html

example:
end div

this line is equivalent to </div>

third are the commands that start directly these commands are equivalent to the openung tags of wrappers in html5

example:
div

this command is equivalent to <div> in html
It should be noted that each line must have only 1 command

nesting of commands in easyhtml is also similar to nesting of tags in html5
example:
div
this is Outer division
div
this is Inner division
end div
end div

the above set of commands are equivalent to the below code in html5:
<div>
this is Outer division
<div>
this is Inner division
</div>
</div>

so check aroud all the commands in Command List,play around with them.I'll be adding more core commands to make your easier with time.
below are some points that you may or may not have observed:

1.the program automatically gives an id to every component you create in order to simplify your job
2.whenever an html file is updated so is the css file.
3.It is advised to different copies of easyhtml-master folder while working with multiple projects as you may end up over-writing on an index.html of another project.
