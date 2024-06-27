# fastapi-clean-arquitecture
How to implement fastapi with clean architecture using python and mongo or another database.
## Development
### - Virtual environment with venv
You need to create a local virtual environment every time you are going to work with python. It is good practice.
You can use the command:
#### $ python -m venv env
### - Activate the environment
now activate the new environment with:
#### $ env\Scripts\activate
or
#### Move to the directory where the activate file is located (env/Scripts) and type activate
## NOTE
If you try to activate your env, and you can't, and
you see a console error with the name Unauthotizedaccess,
you will need to log into your PowerShell terminal with administrator permissions.
#### $ Get-ExecutionPolicy -list
you will see the local machine undefined 
#### $ Set-ExecutionPolicy RemoteSigned -Force
and give permissions to the powershell to run scripts in gpedit.msc
## End of the note
Now you can start installing the dependencies in your environment or if you are working on a team project, normally the dependencies will be in the requirements.txt file, you can use the following command:
#### $ pip install -r requirements.txt
If you need to general or update the requirements.txt use the following command:
#### $ pip freeze > requirements.txt
## FastAPI
### - Installation
#### $ pip install fastapi
You can install all the dependencies you need, and update your requirements.txt
### - Code
Code your application in the main.py file and run:

#### $ python -m uvicorn main:app --reload
You will start the server with uvicorn, you will be able to use your end points. Find your methods in the path 127.0.0.1:8000/docs


