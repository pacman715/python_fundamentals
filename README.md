##### Return to [About Me](https://pacman715.github.io/pcabano-portfolio/)

Through the first six weeks of IT0075 - Python for many uses, which makes up Unit 1, we developed a foundation for programming in Python.  In this section, I have included a chronological representation of the skills learned.  Because the material covered each week is used to build off of in subsequent weeks, it seemed to be the most logical format.  Below, you will find a high level synopsis of the lessons covered for the week along with a link to the project(s) completed.  Each project is developed to demonstrate the techniques learned.  All of the projects culminate into the Week 6 project in which we created a password manager.  

While the program is rudementary, it utilizes all of the skills that were taught throughout the first section of the class and is what I am most proud of thus far.  The single most important take-away from this section of the portfolio is the evolution of coding techniques and practices from week to week.  Through my experience in software development, demonstrating the ability to take one idea or skill and continuously develop and grow it is how we as software developers evolve, as demonstrated below.

### Week 1

As one might imagine, the first week of the class discussed how to develop your first program.  As in most programming classes, one of the first programs developed is 'Hello World', in which you print the words Hello World.  In Python, this is achieved througn the 'print' statement.  The Week 1 project called for the use of the Turtle graphic system.  While reviewing the code, you might notice that each line  appears to be redundant of the next.  This being said, I would like to most improve this program with techniques learned in week two, namely the use of for and while loops.

Week 1 program(s) found in repository below:
- Turtle.py

### Week 2

In this week, we continued to build upon our simple print statements and stared adding logic and conditional statements buy studying flow control.  Understanding flow control is very important because this is when you start to think like a program would, per se. Flow control is displayed in "if - then" statements as well as "for" and "while" loops.  As mentioned before, these techniques would have certainly improved the Turtle.py project. Learning flow control at this stage was very important because nearly all of our future projects would utilize this skill.

Week 2 program(s) found in repository below:
- Tree exercise.py

### Week 3

Here is where everything starts coming together.  The programs we developed implemented techniques that accepted input from the user and, depending on the input, the program made decisions as to how it would behave.  The 

Week 3 program(s) found in repository below:
- Rock_Paper_Scissors.py
- pwd_generator.py

### Week 4

Week 4 program(s) found in repository below:
- Comma_code.py
- collatz.py

### Week 5

Week 5 program(s) found in repository below:
- part_1.py
- part_2.py
- part_3.py
- part_4.py
- part_5.py
- part_6.py

### Week 6

The last week of Unit 1 allowed the class to pull all of their newly attained knowledge together into one program.  Here, we built a password manager, which because of the utilization of all of the techniques in my toolbox and the utility of the program would be my best piece and the one I am most proud of.  

When building this, my partner and I mapped out the requirements and built each function seperately.  It was very important to chunk out the work and complete it incrementally becasue it allowed us to build code and reuse some funtions as needed.  As we completed each, we tested different scenarios and fixed any errors that we found.  Below is a sample of code (functions) that we were able to build once and reuse multiple times:

```python
# encrypts passwords
def encrypt(string):
    result = ""
    for letter in string:
        if letter in alphabet:
            index = alphabet.index(letter)
            result = result + key[index]
    return result

# decrypts passwords copied to clipboard
def decrypt (string):
    result = ""
    for i in string:
        if i in key:
            index = key.index(i)
            result = result + alphabet[index]
    return result
```

There really was not one single problem that we encountered because if we were unsure as to how to complete or develop an idea, we were able to find help on the internet.  Our password manager was extremely important because we were able to implement all of the different things we had learned previously.  I would hope that when reviewing this code and comparing it to my Turtle.py program, it would be easy to see the evolution from my weakest to strongest pieces.

Week 6 program(s) found in repository below:
- pw.py


#### [Unit 1 Repository](https://github.com/pacman715/python_fundamentals/tree/master/Unit%201)
