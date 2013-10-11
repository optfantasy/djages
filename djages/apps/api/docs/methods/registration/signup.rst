/registration/signup
==========================

.. http:post:: /registration/signup

    .. admonition:: Action
    
        Creates a new gulu user.

    :param username: New user's desired username
    :type username: string
    :param email: New user's email address.
    :type email: :ref:`field-email`
    :param password: New user's password
    :type password: string

    **Sample Responses**:

        .. code-block:: js

            {
              "response": {
                 "user_id": "4e9bc7370218230b9d00057f"
              }, 
              "success": true
            }

        .. include:: ../errors/10300

        .. include:: ../errors/10301

        .. include:: ../errors/10302

        .. include:: ../errors/10303
