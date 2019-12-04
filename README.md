# Me command line utility

The *me* command line utility is a set of commands that simplify everyday tasks whilst working in the office

# Requirements

* Python 3 
* Pip for installing dependencies (see `requirements.txt`)
    
# Installation
    
* Create a virtual environment using python 3.6 or above:
     
        cd ~/.virtualenv
        python3 -m venv me

* Activate the virtual environment
    - On Mac: 
    
            source ~/.virtualenv/me/bin/activate
            
    - To make your life easier in the future you can add this as an alias to your .profile (in Mac):
    
            alias me_activate='source ~/.virtualenv/me/bin/activate'
        
     This way you will only need to type `me_activate` instead of remembering the full path to your environment each time

* Install the dependencies using pip:
            
        cd me-cli
        pip install -r requirements.txt

* Make "me" available on the command line.
    
        pip install -e <full_path_to_src_main>
        
    An example the <full_path_to_src_main> would be: `/Users/myUser/dev/me-cli/src/main`

# Command usage

Usage: 

    me [OPTIONS] COMMAND [ARGS]...

  Me

Options:
  --help  Show this message and exit.

Commands:
- files     local file utilities  


