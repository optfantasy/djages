/registration/check_email
===============================

.. http:get:: /registration/check_email

    .. admonition:: Action
    
        Checks if an email address is available for use, i.e. valid format and not associated
        with another Gulu user's account.

    :param email: Email address to check
    :type email: :ref:`field-email`


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
       
        .. include:: ../errors/10303
