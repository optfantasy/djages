/contact/
==============


GET
---

.. http:get:: /contact/

    .. admonition:: Action
    
        Query contacts.
    
    :param user_id: Id of the owner. 
    :type user_id: :ref:`field-id`
    :param is_favorited: is_favorited attribute of contacts.
    :type is_favorited: :ref:`field-bool`
    
    .. seealso:: The definition of :ref:`Contact model <model-contact>`
    
    **Sample Responses**:
    
        .. include:: index_response
        .. include:: ../errors/10004
        

POST
----

.. http:post:: /contact/

    .. admonition:: Action
    
        Create contact.
    
    :param email: Email.
    :type email: :ref:`field-email`
    :param nickname: **[opt]** Nickname. If not specified then it will be the prefix of email.
    :type nickname: string
    :param is_favorited: **[opt]** Flag for favorited contact. Default: *false*.
    :type is_favorited: :ref:`field-bool`
    :param photo_id: **[opt]** Main photo id of the contact.
    :type photo_id: :ref:`field-id`
    
    .. seealso:: The definition of :ref:`Contact model <model-contact>`
    
    **Sample Responses**:
    
        .. include:: object_response

