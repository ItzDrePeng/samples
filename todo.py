#!/usr/bin/python

def print_list(my_list):
   print "";
   for x in my_list: print x;
   print "";

undone = [];
done = [];

"""
Prelude 
"""
print "To-do list";
string = raw_input("Want to read the instructions for this? Hit 'y' for 'Yes'.  Hit anything else to skip the instructions and proceed to the list. ");

print "";
if (string.lower() == 'y'):
  print "For each thing you want to do, type it in, then hit 'Enter' if you want to add more items."
  print "When you're done listing, hit 'Enter' twice in a row to move on to the check-off phase."
  print "For the check-off phase, the program will ask: 'What have you just finished?'"  
  print "Type in whatever you have finished (case-insensitive)." 
  print "The program will then ask if there's anything else you'd like to do."
  print "This is just like the beginning; list new stuff, then hit 'Enter' twice in a row to continue."
  print "The program will repeat with asking what you've finished and what else you'd like to do until you've finished everything."
  print "Have fun!";

"""
Begin adding items onto the list
"""
print "";
print "Good day!  What would you like to do today?";
string = raw_input();
while (len(string) != 0):
  undone.append(string.lower());
  string = raw_input();

"""
Start checking off things you have accomplished throughout
"""
print "";
while(len(undone) > 0):
   print "Here's what left to do:";
   print_list(undone);
   while (True):
      try:
         string = raw_input("What have you just finished? ");
         undone.index(string.lower());
         done.append(string.lower());
         undone.remove(string.lower());
         break;
      except:
         print "Invalid input.  Must be something that's currently in the to-do list.  Try again.";
   string = raw_input("Oh...is there anything else you'd like to do today? ");
   while (len(string) > 0):
      undone.append(string);
      string = raw_input();
   print "Here's what you've completed so far:";
   print_list(done);

"""
FINISH!!!
"""
print "";
print "Congratulations!  You've finished everything that you wanted to do today!";
