# Password Coach

## The client and the problem
This is to help people who use passwords/passphrases.
The problem is that passwords are too easy to guess with computers.

## Why it matters 
Passwords are too easy for a computer to crack.  This may result in people losing money, data, etc.

NIST SP 800-63B-4: Passwords
AARP: FBI Report Shows Older Adults Hit Hardest by Internet Crime in 2025
https://pages.nist.gov/800-63-4/sp800-63b/passwords
https://journals.ala.org/ltr/article/viewFile/4550/5345

- Use atleast two facts from credible sources here.

## What this tool does
This tool will:
 - Verify that your password passes NIST muster.
 - that it isn't one of the popular 50 passwords
 - that the password doesn't contain repeated characters
 - hasn't been exposed to a breach
 - hold a FAQ
 - suggest a passphrase based on virtual dice throws and a word list of easy to remember and spell words from the EFF.

 ## About the data
  - This tool uses a word list based of of Seclists.
  - This tool uses a word list from the EFF.
  - This tool uses qualifiers based off NIST recommendations.
  - When looking up data from an API it changes a password into a hash and only uses the first few characters of that hash.
  - This tool does not store any user information.

  ## How to run
  python app.py
    - insert a sample of running the program and it's output


  Make sure the the word lists are in the same directory as the python script.
