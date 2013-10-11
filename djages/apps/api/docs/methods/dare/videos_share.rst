/dare/(dare_id)/videos/(video_id)/share
==========================================

POST
------

.. http:post:: /dare/(dare_id)/videos/(video_id)/share
    
    .. admonition:: Action
    
        Share the dare video to social network.
    
    :param dare_id: ID of a dare
    :type dare_id: :ref:`field-id`
    
    :param video_id: ID of the dare video
    :type video_id: :ref:`field-id`
    
    :param share_to: The social networks to share. Options are :ref:`enum-social`.
    :type share_to: :ref:`field-string-list`
    
    .. seealso:: The definition of :ref:`Dare model <model-dare>` and :ref:`Video model <model-video>`
    
    **Sample Responses**:

        .. include:: ../null_response

