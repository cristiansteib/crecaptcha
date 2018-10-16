# crecaptcha
###### A simple python module for  Google Recaptcha V3
A pure python module, don't requires requests library
## Installation
- from latest version on PyPi:
    ```bash
    pip install crecaptcha
    ```
    
## how to use?
```python
from crecatpcha.crecaptcha import crecaptcha
SECRET_KEY = 'Your secret key'

def some_function():
    response_token = 'the response token from the client'
    
    if crecaptcha(SECRET_KEY, response_token, 'action_name'):
        # safe action
        pass
    else:
        # is a bot, take your custom action.
        pass
 ```
 
      
## how to use with django?
### Configuration:
In the settings.py define the following values:  
 **CRECAPTCHA_SECRET_KEY**: the recaptcha secret key.   
 **CRECAPTCHA_KEY_NAME**: the name of the var in the POST request, by default is 'recaptcha_token'.    
 Example:
 ```python
CRECAPTCHA_SECRET_KEY = "jgjdnvurmfj3nrfo3nrlksjf" # Mandatory
CRECAPTCHA_KEY_NAME = "grecatpcha" # by default is 'recaptcha_token'
 ```
 
### Usage:
#### Simple way:
In the following example if the recaptcha validation fails, it will raise an HttpResponseForbidden
```python
from crecatpcha.django_crecatpcha import crecaptcha

@crecaptcha('login')
def login_user(request):
    pass
    
@crecaptcha('register', threshold=0.6)
def register_user(request):
    pass
    
```

#### Advance way:
You can define your custom callback when the validations fails, an optionally you can send args & kwargs.

```python
from crecatpcha.django_crecatpcha import crecaptcha

def register_user_on_crecaptcha_error(request, *args, **kwargs):
    pass
    
@crecaptcha('register', register_user_on_crecaptcha_error, args_on_error=[], kwargs_on_error={})    
def register_user(request):
    pass
```
