/facebook/connect
=======================

.. http:post:: /facebook/connect

    .. admonition:: Action
    
        Connects a facebook user to a Gulu user.  Takes a valid access token and facebook id
        pair and returns an authenticated Gulu user.  If a matching Gulu user does not exist, it
        will be created.

        You will likely be using this method for several purposes:

        1. Authentication
        2. New user creation
   
    :param facebook_id: Authenticating user's facebook id
    :type facebook_id: string
    :param access_token: Authenticating user's facebook access token
    :type access_token: string

    **Sample Responses**

    .. code-block:: js

       {
          "response": {
             "user_created": false, 
          }, 
          "success": true
       }

    .. code-block:: js

       {
          "response": {
             "user_created": true, 
          }, 
          "success": true
       }
   
    .. include:: ../errors/10400

    .. include:: ../errors/10401

    .. include:: ../errors/10402
