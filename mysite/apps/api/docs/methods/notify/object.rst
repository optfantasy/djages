/notify/(notify_id)/
==============================

GET
----

.. http:get:: /notify/(notify_id)/
    
    .. admonition:: Action
    
        Get a notification.
    
    :param notify_id: ID of a notify
    :type notify_id: :ref:`field-id`
    
    .. seealso:: The definition of :ref:`Notify model <model-notify>`
    
    **Sample Responses**:

        .. include:: object_response



POST
------

.. http:post:: /notify/(notify_id)/
    
    .. admonition:: Action
    
        Change a notification.
    
    :param unseen: Set this field to manipulate the "unseen" attribute of a notification. 
    :type unseen: :ref:`field-bool`
    
    .. seealso:: The definition of :ref:`Notify model <model-notify>`
    
    **Sample Responses**:

        .. include:: ../null_response
