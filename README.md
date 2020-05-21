# Coronavirus(Covid-19) Detection Using Deep Learning

A deep learning Convolution Neural Network (CNN) model used for predicting whether a patient has covid-19 using the X-RAY scans.

This model is built on top of tensorflow using its keras API. This model is capable of predicting upto an accuracy of 97%.
 
WEBSITE LINK : http://covid19detector-xray.herokuapp.com

## Installation Documentation

	$ sudo apt install git

	$ git clone https://github.com/adityagupta24/Covid19Detection.git

	$ cd Covid19Detection

	$ sudo apt-get install virtualenv

	$ virtualenv env

	$ source env/bin/activate
	
	$ sudo apt-get install python3.7

	$ sudo apt-get install python3-pip

	$ pip3 install -r requirements.txt
	
To launch the server execute the following command, 

	$ python3 app.py

Go to the browser and open the localhost server as : https://127.0.0.1:5000
	
## Website Demo
After opening the localhost server, you will see a project website in your browser.

Now click on the Get Started or Try here button. It will take you to the prediction part of the website.

Now upload and submit the X-RAY Scan which is to be tested for covid-19 and the ML model will show you the coresponding result.

( You can also use the sample images included inside the repository )
