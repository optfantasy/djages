/registration/check_username
==================================

.. http:get:: /registration/check_username

    .. admonition:: Action
    
        Checks if a username is available to use for new Gulu user accounts.

    :param username: Username to check
    :type username: string

    **Sample Responses**:

        .. code-block:: js

            {
              "response": {
                 "is_available": true
              }, 
              "success": true
            }

        .. code-block:: js

            {
              "response": {
                 "is_available": false
              }, 
              "success": true
            }
       
        .. include:: ../errors/10300

