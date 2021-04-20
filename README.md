Section 0: Notebook Structure and Dependencies
In order to view this notebook, jupyter notebook and python should be installed on the computer. Installing python via anaconda or miniconda is recommended (miniconda is the minimalist version of anaconda).

https://www.anaconda.com/products/individual
https://docs.conda.io/en/latest/miniconda.html
After either is installed, make sure Jupyter Notebooks is also installed. Use conda install jupyter in the terminal if needed.

Some code in the notebook depend on files such as CSVs that were previously provided to us. If you pulled everything from the GitHub repository, these files will already be in the directory the notebook is in:

published_locations.json
publisher_list.csv
You may wish to edit these files if new locations and publishers are added to the database. Information in these files are from around March 2021.

Please separately create a file called passwords.csv that stores access credentials to CouchDB. For security reasons this was not placed in GitHub. It just needs the username and password for accessing CouchDB in this format: username,password
