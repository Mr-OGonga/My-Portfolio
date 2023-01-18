# Python Mini-App

This is a Python mini-app that takes the order of the user and then collates a bill with all the items and the price total at the end.

It displays five menus in turn - drinks, starters, pizzas, pastas and desserts - and then gives the user a choice of one, none or multiple orders from each menu. It will then read the users order back to them and confirm everything they have ordered so far in a list. This will continue until the user confirms they are done. There is built-in error-handling so that the user can type "y" or "n" for "yes" on "no" or any phrase containing each of these answers to get the same result. Capitals do do not affect the code and if a number or letter is given when the other is expected or an invalid choice is given, the user is asked to choose again. This code is unbreakable. At the end there is an option to add on a tip or run out on your bill. Following this your total bill is calculated and displyed in a formatted receipt with all of your items listed and a grand total at the end.

The data is pulled from multiple CSV files which are read so that each item can be used individually along with all of its corresponding data such as name, price etc.

This was wirtten during the first week of the Python section of our Data Engineering course although I had some prveious experience with Python.
