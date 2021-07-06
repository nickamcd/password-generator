# Password Generator

A simple password generator that works via the command line.

## Table of Contents

- [General info](#general-info)
- [Technologies](#technologies)

## General info

This project is a simple command line tool to generate passwords. The user may optionally save the password to a text file. If this is the case, an encryption key is generated (if one does not already exist on the local machine) saved to a key file. Then that key is used to encrypt the keys to the passwords.txt file and decrypt them later.

This project was inspired by [this](https://www.youtube.com/watch?v=3Xx83JAktXk) video by Traversy Media. I decided to try building it in python instead of Node.js and add more features.

## Technologies

Project is created with:

- Python Version: 3.9
- colorama Version: 0.4.4
- pyperclip Version: 1.8.2
- cryptography Version: 3.4.7
