/dare/(dare_id)/photos/(photo_id)/share
==========================================

POST
------

.. http:post:: /dare/(dare_id)/photos/(photo_id)/share
    
    .. admonition:: Action
    
        Share photo to social networks.
    
    :param dare_id: ID of a dare
    :type dare_id: :ref:`field-id`
    
    :param photo_id: ID of the dare photo
    :type photo_id: :ref:`field-id`
    
    :param share_to: The social networks to share. Options are :ref:`enum-social`.
    :type share_to: :ref:`field-string-list`
    
    .. seealso:: The definition of :ref:`Dare model <model-dare>` and :ref:`Photo model <model-photo>`
    
    **Sample Responses**:

        .. include:: ../null_response

