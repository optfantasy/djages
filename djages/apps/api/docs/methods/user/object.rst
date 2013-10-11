/user/(user_id)/
==============================

GET
---

.. http:get:: /user/(user_id)/

    .. admonition:: Action
    
        Get a user info.
    
    :param user_id: ID of a user
    :type user_id: :ref:`field-id`
    
    .. seealso:: The definition of :ref:`User model <model-user>`
    
    **Sample Responses**:

        .. include:: object_response


POST
-----

.. http:post:: /user/(user_id)/

    .. admonition:: Action
    
        Update a user info.
    
    :param photo_id: ID of the photo used as the user's main profile picture.
    :type photo_id: :ref:`field-id`
    
    :param nickname: Nickname of the user.
    :type nickname: string
    
    :param old_password: The origin password of the user.
    :type old_password: string
    
    :param new_password: New password to set.
    :type new_password: string
        
    :param allow_activity_email: Allow activity email.
    :type allow_activity_email: :ref:`field-bool`

    :param allow_event_email: Allow event email.
    :type allow_event_email: :ref:`field-bool`

    :param iphone_device_token: iphone device token.
    :type iphone_device_token: string

    
    .. seealso:: The definition of :ref:`User model <model-user>`
    
    **Sample Responses**:

        .. code-block:: js
        
            {
                "response": "main_profile_pic,nickname",
                "success": true
            }
