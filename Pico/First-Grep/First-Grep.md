# First Grep

**Category**: General Skills
**Difficulty**: Easy

## PicoCTF Description
Can you find the flag in file? This would be really tedious to look through manually, 
something tells me there is a better way.

## Tools Used
- command line
- 'cat'
- 'grep'

## Solution
1. After downloading the given file I decided to run 'cat' command on the file to see if 
    there was any human readable code and it looked like a bunch of gibberish.
![Output](./cat-file.png)

2. I then decided to use the 'grep' command as that was stated in the challenge and maybe
    I had to use it somnehow but I also realized I can run
    - 'grep "picoCTF{" file' since this is the format of the flags for picoCTF
![Output](./grep.png)