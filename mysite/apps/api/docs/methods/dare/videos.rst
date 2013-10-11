/dare/(dare_id)/videos/
==============================

POST
-----

.. http:post:: /dare/(dare_id)/videos/
    
    .. admonition:: Action
    
        Create video. Then submit it to a dare.
    
    :param dare_id: ID of a dare
    :type dare_id: :ref:`field-id`
    
    Other parameters please refer to :ref:`Create Video API <api-video-create>`.
    
    .. seealso:: The definition of :ref:`Dare model <model-dare>` and :ref:`Video model <model-video>`
    
    **Sample Responses**:

        .. include:: ../video/object_response

