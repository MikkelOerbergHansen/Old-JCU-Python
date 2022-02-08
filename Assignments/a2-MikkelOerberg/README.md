# CP1404/5632 Assignment: Songs To Learn by Mikkel Oerberg Hansen

Name: Mikkel Oerberg Hansen
Date: 20 may 2018
Brief Project Description:
GitHub URL: https://github.com/CP1404-2018-51/a2-MikkelOerberg


## 1. How long did the entire project (assignment 2) take you?
I started on Sunday 20/5. I  began  developing the Song class and the SongList class.
I finished the code the night between Monday and Tuesday. At this time all the main functionality of the program
was working and I was only missing the report and README file.
In total I have spent the majority of 3 days on completing this assignment.

## 2. What are you most satisfied with?
Im most satisfied with the kivy app. It works very well and is enjoyable to test.
Im also very satisfied with the relationship between the SongList class and the Song class.
It is satisfying to create classes that utilize other classes in-order to work well.
This way the relationship becomes a kind of hierarchy, which has a very logical
functionality.


## 3. What are you least satisfied with?
There are a few detailed aspects of the program, that i think could have been solved in better ways.
1. first thing was a problem i encountered with the spinner drop-down. By default there is small gaps/spaces between
the labels in the drop-down and when the drop-down menu stretches down over other labels, their colour shines through
the small gaps. this means that sometimes whitespace from the text input could be seen between some dropdown labels
and black space from the labels could be seen between some other dropdown labels.
i mangaed to overcome this by customizing the sizs of different labels, but i feel like there could
have been a better solution. Either setting a background color to the spinner dropdown, or removing the
gap between the dropdown labels.
2. was the implementation of colors on dynamic widgets. I never managed to name the colors as constants.

## 4. What worked well in your development process?
It worked well to breakdown the assignment into smaller sub-problems, and then focusing on finishing
one problem at a time. First creating the Song class which had several sub-problems,
then creating SongList class which also had several sub-problems, and lastly creating the kivy app,
which again could be broken down into several sub-problems.
Each sub-problem could then be implemented and tested before proceeding. Sometimes a problem also required
me to go back and revise my solution for a previous problem.

## 5. What about your process could be improved the next time you do a project like this?
I could have made more git commits, with better messages. Im still getting used to github.
Next time i would try and commit more often and create better
descriptions (use imperative voice) for each commit.


## 6. Describe what resources you used and how you used them.
I used a lot of inspiration from the practical where we learned kivy.
Especially the dynamic widgets and the spinner demo.
That was very helpful when creating the kivy app:
It helped me to create widgets from the main.py file, and to implement the spinner
I also used the files to get inspiration for the app.kv file: how the box-layouts should be
ordered in-order to achieve the required layout.
I also got a lot of inspiration from my previous assignment: this was helpful when
checking user input for errors.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.
First major challenge was to create a proper SongList that actually stored Song objects.
I overcame this problem by first creating a SongList without song objects, so i could see
that it worked, and then i tried to replace certain elements so the items in the list was created
as Song objects. It required a lot of testing, editing and testing again.
the next major challenge was to create the app.kv file to get the desired output.
This was also achieved by scanning through the kv files from the kivy demos, and by testing and
revising the code several times.

