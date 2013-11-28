#!/usr/bin/python

def print_list(my_list):
   print "";
   for x in my_list: print x;
   print "";

undone = [];
done = [];

print "To-do list";
string = raw_input("Want to read the instructions for this? Hit 'y' for 'Yes'.  Hit anything else to skip the instructions and proceed to the list. ");

print "";
if (string.lower() == 'y'):
  print "For each thing you want to do, type it in, then hit 'Enter' if you want to add more items."
  print "When you're done listing, hit 'Enter' twice in a row to move on to the check-off phase."
  print "For the check-off phase, the program will ask: 'What have you just finished?'  List all the items in the list that you have finished (case-insensitive); hit 'Enter' twice in a row when you're done, just like how you added the items onto the list in the first place."
  print "Have fun!";

print "";
print "Good day!  What would you like to do today?";
string = raw_input();
while (len(string) != 0):
  undone.append(string.lower());
  string = raw_input();

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
   print "Here's what you've completed so far:";
   print_list(done);

print "";
print "Congratulations!  You've finished everything that you wanted to do today!";
