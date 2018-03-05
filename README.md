# sikuli-scripts
Miscellaneous sikuli scripts to click through games and other desktop apps

1. [What is this?](#section1)
2. [Why is this?](#section2)
3. [What's left to do?](#section3)
4. [What could be done instead?](#section4)


# <a name="section1">1. What is this</a>

A collection of Python scripts powered by Sikuli, an open source framework for recognizing images on the screen.  The initial batch of scripts here are written with the purpose of clicking through the mundane portions of a few flash games

# <a name="section2">2. Why is this</a>

Well, why isn't this?  This was done as motivation to wean myself off spending too much time doing mundane things in games so that I could focus on other things.  Additionally, this could really help those who are attached to the games but tired of the grind

# <a name="section3">3. What's left to do?</a>

A lot.  This is not even close to the point where you can press a button and it'll do everything you want for you.

# <a name="section4">4. What could be done instead?</a>

There are a few options that I have considered:

i. AutoHotKey:
    I have already tried this, but it's a tedious effort to maintain ahk scripts. Having separate functions to click the various UI elements is a cumbersome task and breaks down in the case UI changes or even an accidental scrolling of a page.  Sikuli is a definite step up from having to hard code element locations.
    
ii. Machine learning:
    This would be a more long term solution to the UI interaction route but it is a large time investment. A self learning approach is viable but it is hard to accumulate data in instances where a simulated test environment isn't available (as is the case with a lot of server-sided games) without having the AI do an undoable action, e.g. non-trivially dismantling player progress via exhausting premium currency or selling hard to obtain objects.  Hence, it would have to be a community driven effort to provide and tag data.
    For non games, machine learning is simply overkill
    
iii. Fiddler2 (or similar packet capturing routes):
    Ideally, this route is the best for server-connected applications.  Why burden your interaction with the cumbersome limitations of the client UI?  Capturing and spoofing packets reduces the approach to making "API" calls to the server
    I have explored this route but require some assistance in learning to do it.
    

    
