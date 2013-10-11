/email/invite
=======================

.. http:post:: /email/invite

    .. admonition:: Action
    
        Send invitation emails for request user. Users can use this function to invite their 
        friends to use gulu app.
   
    :param app: The app name. For detail, please see :ref:`enum-app`
    :type app: string
    :param emails: Email list.
    :type emails: :ref:`field-email-list`

    **Sample Responses**
    
        .. include:: ../null_response

