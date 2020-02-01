## QLCM - Quick Least Common Multiple

Author: Johannes Neumann

QLCM is a small app for calculating the least common multiple of two integers, made with Python Flask and Javascript. 

### Setup Instructions:

There is a **requirements.txt** with all installed packages. Leave it in the main folder, and create a virtual environment:

   * $ virtualenv venv *OR* python3 -m venv venv
   * $ source venv/bin/activate *OR* venv\Scripts\activate on Windows
   * (venv) $ pip install -r requirements.txt
   * (venv) $ flask run
   * The app will run on localhost (127.0.0.1:5000)

### Working environment:
* Python 3.7.6
* jQuery 3.4.1 (web sourced from https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js)
  * Should maybe be static for corporate app => internet independency

### Design decisions:

#### Flask
 * Lightweight
 * Built-in develoment server
 * Templating Engine 
 * WTForms Support (QuickForms are very helpful for a prototype)
 * Good Tutorials & Documentation

#### Bootstrap:
* Good base css infrastructure
* Quickly able to make app scalable to different screens and resolutions (or a small browser window)
  * Note: Seems to bring jQuery 1.12 along with it, but the ajax didn't work with that.
  
#### AJAX:
* Although a POST-to-self-function would have been quicker and less complex to set up this is the elegant way.

#### Visual Design:
* I aimed for clear cut simplicity, with minimal clicks and user assistance through input validation 
    * added *widget=html5.NumberInput()* in forms.py, since wtform validators don't catch everything

### Possible next steps:
* Obviously this is just a foundation. With a larger time scope i'd 
  * Maybe implemented "Calculate as you type" => get rid of submit button and get a Javascript "on-keyup-function" for dynamic user experience (has to be weighed up against more traffic/server load)
  * Thought about comfort function like copying result to clipboard for further processing (depending on typical user workflow)
  * Accentuated with some corporate colors in there (Our company brand portal is a good guideline for visual design)
* The base structure of the app is relatively clean and allows for a good deal of expansion, thanks to templates. Although this is a very tiny seed to grow an application from...
* Alternatively it's not hard to transfer the app to another Flask application, which should only take a couple of adjustments
