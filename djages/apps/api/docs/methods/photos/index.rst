/photos/
==============


GET
---

.. http:get:: /photos/
    
    .. admonition:: Action
    
        Query photos.
    
    :param target_id: ID of the target for photo.
    :type target_id: :ref:`field-id`
    
    :param user_id: ID of the photo creator.
    :type user_id: :ref:`field-id`
    
    :param place_id: ID of the place.
    :type place_id: :ref:`field-id`
        
    .. seealso:: The definition of :ref:`Photo model <model-photo>`
        
        
    **Sample Responses**:
    
        .. include:: index_response
        

.. _api-photos-create:

POST
----

.. http:post:: /photos/

    .. admonition:: Action
    
        Create photo.

    :param file: Photo file contents.  Can be either *.png* or *.jpeg* formatted file, maximum of *512Kb*.
    :type file: :ref:`field-file`
    
    :param title: **[opt]** Photo title.
    :type title: string
    
    :param description: **[opt]** Brief photo description.
    :type description: string

    .. seealso:: The definition of :ref:`Photo model <model-photo>`
    
    **Sample Responses**:
    
        .. include:: object_response
        
        .. include:: ../errors/10500
        
        .. include:: ../errors/10501

