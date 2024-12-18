# Ans 1)   
print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
''')


# Ans 2) done 


# Ans 3)  https://pypi.org/project/pyttsx3/

import pyttsx3
engine = pyttsx3.init()
engine.say(" saale ")
engine.runAndWait()


# Ans 4 :- 
import os


# Specify the directory you want to list 
directory_path = '/'  # shows e drive folders 
directory_path = 'E:\\'
directory_path = '/Python Tutorial'


#  List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name 
for item in contents:
    print(item)

# Select the directory whose content you want to list
directory_path  = '/'
# Use the os module  to list the directory content 
contents = os.listdir(directory_path)


# Print the contents of the directory 
print(contents)



# Ans 5 :- done 