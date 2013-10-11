/video/
==============

GET
----

.. http:get:: /video/

    .. admonition:: Action
    
        Query videos.
    
    :param user_id: ID of the video owner.
    :type user_id: :ref:`field-id`

    .. seealso:: The definition of :ref:`Video model <model-video>`
    
    
    **Sample Responses**:

        .. include:: index_response
    


.. _api-video-create:

POST
----

.. http:post:: /video/

    .. admonition:: Action
    
        Create a video.
    
    :param file: Video file contents.
    :type file: :ref:`field-file`
    
    .. seealso:: The definition of :ref:`Video model <model-video>`
    
    **Sample Responses**:
    
        .. include:: object_response
        
