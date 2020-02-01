## QLCM - Quick Least Common Multiple

Author: Johannes Neumann

QLCM is a small app for calculating the least common multiple of two integers, made with Python Flask and some Javascript. 

### Installed Packages:
* pip install flask
* pip install config
* pip install python-dotenv
* pip install numpy
* pip install flask-wtf
* pip install flask-bootstrap
### Web sourced:
https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js

### Working environment:
* Python 3.7.6
* Created Virtual Environment:
  * python3 -m venv venv
  * venv\Scripts\activate (Windows)

### Design decisions:

#### Flask
 * Lightweight
 * Built-in develoment server
 * Templating Engine 
 * WTForms Support (QuickForms are very helpful for a prototype)
 * Good Documentation

##### Bootstrap:
* Good base css infrastructure
* Brings jQuery with it
* Quickly able to make app scalable to different screen sizes and resolutions

### Visual Design:
* I aimed for clear cut simplicity, with minimal clicks and user assistance through field validation 
 * *widget=html5.NumberInput()*, since IntegerField unintuitively doenst do that)

### Possible next steps:
* Obviously this is just a foundation. With a bigger focus on shinyness and more time I'd have:
 * Maybe implemented "Calculate as you type" => get rid of submit button and get a Javascript on *("keyup",function(...){})* for dynamic user experience (has to be weighed up agains more traffic/server load)
 * Got some corporate colors in there (Our corporate brand portal is a good guideline for front end design)
* The base structure of the app is clean and allows for a good deal of expansion, thanks to templates and the basic file structure, although this is a very tiny seed to grow an application from...
* Alternatively it's not hard to transfer the app to another Flask application, which should only take a couple of adjustments
