
So the first thing I want to talk about is dictionaries in Python. Now,

dictionaries in Python work kind of similarly to dictionaries in real life,

right? So if you were to look up a word in the dictionary

say the word code, then you might find the definition as something along the

lines of program instructions for the computer. And dictionaries are really

useful because they allow us to group together and tag related pieces of

information.

The way I like to think about dictionaries is in the form of a table.

Every dictionary has two parts to it.

On the left hand side is the key,

and that is the equivalent of the word in the dictionary,

and then it's also got an associated value. That would be the equivalent

of the actual definition of the word.

Now let's say that we took this variation simple table of definitions of

programming words that we've come across so far

and we go ahead and we try to convert it right into a dictionary,

how would we do that? Let me firstly

drop the last two rows and let's just start with the first one.

The first thing we want to do is we want them to create a dictionary. And to do

that in Python, this is what the syntax looks like.

We have a set of curly braces and everything that's inside

the curly brace is the content of our dictionary.

The key goes first followed by a colon and then followed by the value. In our

table we've got this word bug, which is the first key,

so we can replace that over here in our dictionary. And the value that's

associated with this key is the definition for a bug.

So an error in a program that prevents the program from running as expected,

that becomes the value and can be replaced here after the colon.

So now, we've created an actual dictionary using Python code.

What if you wanted to have more than one entry in your dictionary? Well,

you would separate each of the key value pairs using a comma,

and then you can continue adding key and value pairs until you get to the end of

your dictionary. All right,

let's take a look at dictionaries in action.

If you head over to the day nine start code file and go ahead and fork your own

copy to work alongside me, then you can see that in here

I've already added the dictionary that we were defining earlier on,

and I've stored it inside of a variable called programming dictionary. Now,

currently I've only got two entries in this dictionary,

the definition for a bug and the definition for function. Now,

the first thing I want to highlight is when you create a dictionary that has

more than one element such as in this case,

then you want to take care to format it properly so that it's more easily

readable.

So what you'll see Python programmers do by convention is they will start off

the dictionary with the open curly brace at the top

and then every subsequent entry is indented by one indent.

And then at the very end of that entry, there's a comma

and then we hit enter so that the next item goes onto the next line

and finally,

the last curly brace should go at the very beginning in line with the start of

the dictionary.

And another thing that's quite nice to do is to cap off all entries in your

dictionary or list with a comma.

This means that if you needed to add more items into the dictionary

you can simply just hit enter and continue typing the next thing.

And if we wanted to add another entry,

it's a simple as adding in the key, a colon and then the value and to cap it

off again with a comma.

So now our dictionary represents exactly the same data as we saw in our table

over here with a bunch of key value pairs and a total of three entries.

Now,

the next thing I want to do is what if I wanted to retrieve an item from the

dictionary, because we know that if we had a list

what we would do is we would use a set of square brackets

and then we would give the index of the item that we wanted.

So the item at index zero or one or two and so on and so forth. Now for

dictionaries, it's kind of similar in terms of syntax

but the only difference is that dictionaries have elements which are identified

by their key. If we wanted this piece of information, for example,

then all we have to do is tap into the dictionary and then add a set of square

brackets and inside the square brackets, we're going to provide the key.

So here the key is a string and it's the string bug.

So let's go ahead and put bug in here.

And now if I go ahead and print this,

then you can see that it is going to give me the value,

which is 'An error in a program that prevents the program from running as

expected.' Now it's really,

really important that you make sure that when you're fetching something out of a

dictionary by it's key that you actually spell the key correctly.

A really

really common error is when you're trying to retrieve something out of a

dictionary and you've just made a very simple typo. So instead of 'u'

I'm typing 'o' here and you'll see

we get an error. And the error tells us that it's a key error referring to this

particular key and it highlights this line 7 where we're trying to retrieve

something out of this dictionary by this key.

Basically it's telling you that this key doesn't actually exist and it can't be

found. So it doesn't know what it is that you want. Remember how

when we had lists and when we try to retrieve something that was not inside the

list. So for example, this particular list at index 4

doesn't actually exist because this is zero one, two, three,

and four is actually not a piece of data inside of this list.

Similarly with dictionaries, if we try to put in a key that doesn't exist,

then we get this key error.

Now another common pitfall that students fall down into is they don't actually

use the correct data type. So for example,

if we defined this dictionary without putting a string around each of these

keys, then it's going to error out and it won't even let us run.

It's going to tell us undefined named bug because it thinks that this is a

variable that you've declared somewhere,

but it's not. In fact, what you wanted are these strings for keys.

And so when you have a key that is a string,

when you're trying to retrieve the data from that key,

you also have to make sure that you provide the key in its actual data type.

So for example, if this was just a number, say one, two, three,

then, of course, all you have to write in here is just one, two, three,

and it would know that this piece of data is what you wanted.

So that's how you retrieve items from a dictionary by adding a square bracket

and then giving it the key.

And it will look for the key inside the dictionary and give you back the

value. Now,

what if you wanted to add a piece of data such as that loop that we had earlier

on, but you want to do it programmatically.

So instead of doing it

when you were defining the dictionary at the beginning,

what if at some later stage in your program you needed to add a new entry?

Well, to do this, it's also really simple.

All you have to do is to tap into the dictionary,

which is called programming dictionary in our case and again,

using square brackets, we define the key.

The key I'm going to add is our loop.

And then after a equal sign, I get to assign the value.

So in my case, the value is going to be the definition for a loop.

And now when this line of code is executed and we go ahead and just print the

programming dictionary after this has happened,

then we'll see that it's actually different from what we had before.

So let's hit run and you can see that previously we had a programming dictionary

that had only two items, bug and function.

And after this line 10, where we print our programming dictionary again,

you can see it's now got three items, bug, function, and loop.

Now very often when you're writing code,

it can be really helpful to start out with a empty dictionary. Just as you saw

previously,

you create an empty list by simply having a set of square brackets with nothing

inside.

You can also create an empty dictionary by simply creating a set of curly braces

with nothing inside. And then at a later stage,

you can add to your dictionary by using this method that you saw here.

Now, on the other hand,

you might actually want to wipe an entire dictionary. Here,

I'm creating a new empty dictionary by creating this pair of curly braces with

nothing inside.

But I can also wipe an existing dictionary by simply doing the same thing.

We know that this dictionary, programming_dictionary, has three items in it.

But on line 17,

I'm going to say programming dictionary equals empty dictionary.

And now if I move this print statement down here,

then you can see that when it prints out,

it's actually going to be completely empty.

That can be really useful if you wanted to clear out a user's progress

or for example, if a game restarts,

then all the scores and stats will probably have to be wiped empty.

So this is one way that you could do that.

Now this method of tapping into a dictionary,

using the key to fetch the relevant item from it

and then doing something with it goes beyond just adding.

You can also use this to edit an item in a dictionary.

For example, let me go ahead and comment out these two lines of code

so we don't wipe our programming dictionary and instead I'm going to tap into

the programming dictionary and I'm going to fetch the item that has a key of bug

and I'm going to redefine its value.

So currently it should be an error in a program that prevents the program from

running as expected.

And I can prove that if I just wrap this around a print statement.

If instead I wanted this to be a different value,

then I can simply use the same syntax as I did for adding new items

but in this case

I'm actually editing this entry because it's going to look through the

dictionary,

find a value with this key and then assign it to whatever I put on the right

hand side of the equal sign. Now, on the other hand,

if it finds nothing with that key,

then it's going to create a new entry with the value again

on the right hand side of the equal sign.

Now let's say that a bug is instead 'A moth in your computer.'

Now, if I go and print my programming dictionary once more,

then you can see that the definition for our bug has now just been changed.

The final thing with regards to dictionaries that I think is really,

really useful is how you loop through a dictionary. And using your knowledge from

lists you might think that to loop through a dictionary, you would,

let's say we are using a for loop. And we say for, um,

thing in programming dictionary,

let's go ahead and print this thing each time.

Here's a good moment to play computer and think,

what do you expect to be printed?

So let's comment out all of the other print statements

so we don't get confused. And when I click run,

what do you think will be printed?

Right?

All right. Is that what you expected? Because it certainly

wasn't what I expected when I first learned Python.

I thought it would give me each of the items in the dictionary with this key and

its value.

But instead this code actually just gives you the keys.

Now, of course, once you do have access to the key, instead of thing,

I should actually really say for key in programming_dictionary.

If I wanted to print the key, then of course I could just write print key.

But if I wanted to get hold of the value,

I could equally just as easily tap into my dictionary,

use the square brackets and pass in that key.

So now when I hit run, you can see it's giving me first

the key from this line and then secondly

the value based on this line.

I'm using that retrieval code in order to get the value.

Of course,

remember that you can get access to all the code that I'm writing here by

looking at the end code of the day

that you'll find on the course resources list.

And if you want to, have a quick review of everything that we've gone through so

far,

because a lot of this knowledge is going to be tested in the next lesson where

we do a coding exercise that will really solidify everything you've learned in

this lesson so far. So for all of that, and more, I'll see on the next lesson.

