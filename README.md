# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## Project Reflection

### Project Overview

**What is this project? What does it do?**
Bookbot is a Python command-line tool that processes a `.txt` file. The script counts the total number of words and the frequency of each character. This project is part of [Boot.dev](https://www.boot.dev) curriculum and emphasizes text processing, function modularity, and Git version control. 

**Core Concepts Practiced**
- FileI/O: Reading and processing text files in Python.
- String Manipulation: cleaning and analyzing text data.
- Data Structures: Using dictionaries to track character frequencies.
- Modular Programming: Organizing codes into functions.
- Version Control: Implement Git for tracking changes

**What I Learned**
- I learned how to properly manage my project using Git.
- How to break down tasks into smaller, manageable functions for code redability.
- I learned the importance of normalizing text before processing. I had to convert each character to lower case to avoid duplicates in the dictionary.

**How I Solved Problems**
I encounteres challenges in allowing users to specify the input file via command line arguments. This is my first encounter with the `sys` module, especially `sys.argv`. I used the [Python doc](https://docs.python.org/3/library/sys.html) to kinda figure out what to do. Even then, I was unsure what the `sys.argv` did. Prior to using the `sys` module, I had hard-coded the filepath. This was good for testing my code, but not very useful for end-users. I found some helpful information in [stackoverflow](https://stackoverflow.com/questions/4117530/what-does-sys-argv1-mean-what-is-sys-argv-and-where-does-it-come-from) and was able to resolve the issue.

**Next Steps / Improvements**
I will redo this project without being guided. I will do it using only my brain and Python docs (a little hard to read those:)) Watch this space for a link to the "bookbot_redo" repo.

**Final Takeaway**
It was a fun experience building this project. It is a reminder to myslef to stick to things when it starts getting a little hard. By completing this project, I've just proven to myself that the only thing that can hold me back is doubt. 

