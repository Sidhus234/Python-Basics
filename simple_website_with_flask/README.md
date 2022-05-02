<h2>Hereko</h2>


# How to create a Virtual Environment in Visual Studio
1. Need to create virutal environment using virtual env package. First install the package (pip install virtualenv).
2. Then open a python terminal, and run (python -m venv virtual) command. This will create a virtual environment with only required libraries to execute the code.
3. Then run the comman "virtual\Scripts\python" to run the create virtual python environment.
4. Get out of python(ctrl + Z) and install flask in virtual environment using (virtual\Scripts\pip install flask)
5. To run the python wensite on virtual environment (virtual\Scripts\python script1.py)

# How to host website on Python anywhere: https://www.pythonanywhere.com/
1. Sign-up for Pythonanywhere (Beginner: Free acount)
2. Go to Console, and click on Bash Console. Using "pwd" you can see where you are.
3. Go to "web" section and create a new web app. Press next. Select Flask and python version. Press next. App is created.
4. Go to files. On the left side there will mysite option. Click there. Open the file "flask_app.py". Delete everything in that file and copy paste everything from script1.py in that file. 
5. In mysite, create a new template folder. Upload templates files there.
6. Similarly create a static folder. Upload static files there.
7. Edit flask_app.py code (change app.run(debug=True) to app.run(debug=False))
8. Go to web section and click on Reload. It will provide a url. Click on the url and the website should be online.
9. In case the website is not online, look at error log.
 

