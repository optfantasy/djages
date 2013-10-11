/contact/(contact_id)/
==============================

GET
---

.. http:get:: /contact/(contact_id)/

    .. admonition:: Action
    
        Get a contact with specific contact_id.
    
    :param contact_id: ID of a contact
    :type contact_id: :ref:`field-id`
    
    .. seealso:: The definition of :ref:`Contact model <model-contact>`
    
    **Sample Responses**:

        .. include:: object_response

POST
------

.. http:post:: /contact/(contact_id)/
    
    .. admonition:: Action
    
        Update a contact object with specific contact_id.
    
    :param contact_id: ID of the contact
    :type contact_id: :ref:`field-id`
    
    :param photo_id: ID of the profile photo for the contact
    :type photo_id: :ref:`field-id`
    
    :param nickname: Nickname.
    :type nickname: string
    
    :param is_favorited: Flag for favorited contact.
    :type is_favorited: :ref:`field-bool`
    
    .. seealso:: The definition of :ref:`Contact model <model-contact>`
    
    **Sample Responses**:
    
        .. code-block:: js
        
            {
                "response": "profile_pic",
                "success": true
            }

DELETE
------
Delete a contact object with specified contact_id.

.. http:delete:: /contact/(contact_id)/
    
    :param contact_id: ID of a contact
    :type contact_id: :ref:`field-id`
    
    **Sample Responses**:
    
        .. include:: ../null_response