/auth/signin
==================

.. http:post:: /auth/signin

    .. admonition:: Action
    
        Authenticates a user and returns a session key.

    :param username: Authenticating user's username (or email)
    :type username: string
    :param password: Authenticating user's password
    :type password: string
      
    **Sample Responses:**
   
        .. include:: ../null_response
        .. include:: ../errors/10101
   
   
   
   
