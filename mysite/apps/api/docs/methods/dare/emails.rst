/dare/(dare_id)/emails/
===========================

POST
-----

.. http:post:: /dare/(dare_id)/emails/

    .. admonition:: Action

        Send email to spectator for a dare.

    :param dare_id: ID of a dare
    :type dare_id: :ref:`field-id`    
    :param attr_value: ID of the new spectator email.
    :type attr_value: :ref:`field-email`
    
    **Sample Responses**:

        .. include:: ../null_response

GET
-----

.. http:get:: /dare/(dare_id)/emails/

    .. admonition:: Action
    
        Get spectator emails of the dare object.

    :param dare_id: ID of a dare
    :type dare_id: :ref:`field-id`
        
    **Sample Responses**:

        .. code-block:: js
        
            {
                "response": ["eric@gmail.com", "sainteye.x.deatheye@gmail.com"],
                "success": true
            }
