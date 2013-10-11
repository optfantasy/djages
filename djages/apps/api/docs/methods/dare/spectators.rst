/dare/(dare_id)/spectators/
===========================

POST
-----

.. http:post:: /dare/(dare_id)/spectators/

    .. admonition:: Action

        Add spectator to a dare.

    :param dare_id: ID of a dare
    :type dare_id: :ref:`field-id`    
    :param attr_value: ID of the new spectator.
    :type attr_value: :ref:`field-id`
    
    **Sample Responses**:

        .. include:: ../null_response

GET
-----

.. http:get:: /dare/(dare_id)/spectators/

    .. admonition:: Action
    
        Get spectators of the dare object.

    :param dare_id: ID of a dare
    :type dare_id: :ref:`field-id`    
    
    .. seealso:: The definition of :ref:`User model <model-user>`
        
    **Sample Responses**:

        .. include:: ../user/index_response
    