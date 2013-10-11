Responses
=========

Each response will contain a JSON dictionary (excluding internal server errors)
with at least a 'success' field containing true or false, indicating whether
or not the request was successful.  If false, an additional error dictionary 
will be present containing 'code' and 'message' fields.  For example, a valid
request will return:

.. code-block:: js
   
   {
      'success': true,
      'response': ... // response body
   }
   
and a failed request will return:

.. code-block:: js

   {
      'success': false,
      'error': {
         'code': 10101,
         'message': "This method requires authentication."
      }
   }
   
The server will always respond with a 200 OK HTTP status code, even if errors 
occured during the request.  It's up to the client ot test for 'success' and 
determine how to handle any errors present.

Error Handling for API Developers
---------------------------------

In an effort to standardize error handling as much as possible, each unique
error condition will return a unique code and error message.  From an API 
developer's perspective, the easiest way to report an error to the client
is to raise a GuluAPIException with the correct error code.  Error codes
are defined in newapi/errors.py.  For example:

.. code-block:: python

   from newapi.errors import ERROR_AUTH_NOT_AUTHENTICATED, GuluAPIException
   
   if error_condition:
      raise GuluAPIException(ERROR_AUTH_NOT_AUTHENTICATED)
      
This will generate a response with the proper success state, error code,
and error message.

Application Error Codes
-----------------------

API error codes are defined in newapi/errors.py and their function should be
clear from the attached error message and constant name.  Error codes are 5
digits starting with a 1.  The first 3 digits identify the module for
module-specific error codes, and general errors always start with 100.  For
instance, a general unknown error has code 10000, while an auth-related 'not
authenticated' error will have code 10100.  Other auth-related messages should
follow the pattern 10101, 10102, etc.  

Each error code also has an associated python constant.  For consistency, try
to use a descriptive constant, and identify the module for module-specific
errors.  For instance, auth-related constants will all follow the format
ERROR_AUTH_<description>, while general errors follow the format 
ERROR_GENERAL_<description>.