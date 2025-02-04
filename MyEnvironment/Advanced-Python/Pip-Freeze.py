# pip freeze Command :-   The pip freeze command is used to generate a list of all installed Python packages in the current environment along with their respective versions. This is especially useful for creating a requirements.txt file, which is often used to replicate the same environment in another system or project.



# Syntax :-   pip freeze [options]



# Common Options :- 

'''

   1) pip freeze > requirements.txt: Redirects the output to a file named requirements.txt.

   2) pip freeze --all: Includes all packages, including those managed by pip and others (e.g., setuptools).

   3) pip freeze --exclude <package>: Excludes specific packages from the output (introduced in pip 22.1).

'''




# How It Works :- 

'''

   1) Fetches Installed Packages :-  pip freeze scans the Python environment and identifies all installed packages.

   2) Displays Package Versions :-  The output lists the package names and versions in the format package==version.

   3) Redirects to a File (Optional) :-  Using >, the output can be redirected to a requirements.txt file, which can later be used with pip install -r requirements.txt to recreate the same environment.

'''



# Usage Examples :- 


#  1) Display All Installed Packages :-  pip freeze

'''

Output :- 

flask==2.1.2
numpy==1.23.4
pandas==1.5.0
requests==2.28.1


'''




# 2) Save Installed Packages to requirements.txt :-   pip freeze > requirements.txt


'''

Output :- 

# This creates a file requirements.txt with the following content :- 


flask==2.1.2
numpy==1.23.4
pandas==1.5.0
requests==2.28.1


'''




# 3)  Exclude Specific Packages :- Exclude a package (e.g., numpy) from the list.


# Syntax :-   pip freeze --exclude numpy





# 4) Include All Packages :-   To include all packages, including those not managed by pip. 


# Syntax :-   pip freeze --all

