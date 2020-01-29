## QLCM - Quick Least Common Multiple

Author: Johannes Neumann

QLCM is a small app for calculating the least common multiple of two integers, made with Python Flask. 

### Installed Packages:
* pip install flask
* pip install config
* pip install python-dotenv
* pip install numpy
* pip install flask-wtf
* pip install flask-bootstrap

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

#### Visual Design:
* I aimed for clear cut simplicity, with minimal clicks and user assistance through field validation
* I intentionally kept the Javascript on a low level, to not inhibit the lightness of the app

#### What was omitted
* Ajax would obviously be a more elegant solution for getting the calculation result, but that was not the focus of the exercise
