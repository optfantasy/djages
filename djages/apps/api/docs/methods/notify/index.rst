/notify/
==============


GET
---

.. http:get:: /notify/

    .. admonition:: Action
    
        Query notifications.
    
    :param user_id: ID of the notify receiver.
    :type user_id: :ref:`field-id`
    
    :param target_id: ID of the target for notify.
    :type target_id: :ref:`field-id`
    
    :param target_type: Type of the target for notify.
    :type target_type: :ref:`field-type`
        
    :param unseen: Boolean value to query seen or unseen notifications.
    :type unseen: :ref:`field-bool`
        
    :param filter_type: The filter type of special query.
    :type filter_type: string
        
    **Special Query**:
    
    Use **filter_type** to perform special query. Options are :ref:`enum-app`.
    The results will be constrained in the realm of specified app. 

    .. seealso:: The definition of :ref:`Notify model <model-notify>`
        
        
    **Sample Responses**:
    
        .. include:: index_response
