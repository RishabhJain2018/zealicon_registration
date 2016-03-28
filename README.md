#Registration_Module

A new registration module for the Zealicon.

#Installation

The development of the Registration_Module server is running on Ubuntu, So this is the easiest environment to work with,
but other distros of linux will work well.

#Linux Based Setup For Registration_Module development
Note: Ubuntu 14.04 LTS is recommended to be used.

1. After installing Ubuntu 14.04, refresh your apt package index
    
   sudo apt-get update

2. Now, install pip using Python Version 2
   
   sudo apt-get install python-pip

3. After installing pip , install the dependencies

   pip install -r requirements.txt

4. Now, run the following git clone(specify a directory)
   
  https://github.com/ncs-jss/Registration.git registration

5. Move to the directory in which you cloned the git repository.

   cd registration

6. You are all set to run the development server

   python manage.py runserver

7. Visit [http://localhost:8000][localhost] in your browser & you are all set.
   [localhost]: http://localhost:8000/

