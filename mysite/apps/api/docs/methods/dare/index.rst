/dare/
==============


GET
---

.. http:get:: /dare/
    
    .. admonition:: Action
    
        Query dares.
    
    :param creator_id: ID of the creator.
    :type creator_id: :ref:`field-id`
    
    :param challenger_id: ID of the challenger.
    :type challenger_id: :ref:`field-id`
    
    :param city_id: ID of the searchcity.
    :type city_id: :ref:`field-id`
    
    :param place_id: ID of the place.
    :type place_id: :ref:`field-id`
    
    :param filter_type: The filter type of special query.
    :type filter_type: string
        
    **Special Query**:
    
    ``filter_type: ["owned", "watching"]``
    
    * **"owned"**:
        Use an additional parameter **user_id** (:ref:`field-id`) to query the dares owned by the user. 
        
        *pseudo query*: 
            ``Q(creator=user_id)|Q(challenger=user_id)``
    
    * **"watching"**:
        Use an additional parameter **user_id** (:ref:`field-id`) to query the dares watched by the user. 
        
        *pseudo query*: 
            ``~Q(creator=user_id), ~Q(challenger=user_id), Q(spectator=user_id)``

    .. seealso:: The definition of :ref:`Dare model <model-dare>`
        
        
    **Sample Responses**:
    
        .. include:: index_response
        

POST
----

.. http:post:: /dare/
    
    .. admonition:: Action
    
        Create dare.
    
    :param title: Title.
    :type title: string
    
    :param city_id: The searchcity ID for the dare.
    :type city_id: :ref:`field-id`
    
    :param challenge_contact_id: The contact ID of the dare challenger.
    :type challenge_contact_id: :ref:`field-id`
    
    :param place_id: **[opt]** The place ID for the dare.
    :type place_id: :ref:`field-id`
    
    :param share_to: **[opt]** Share the dare to social network. Options are :ref:`enum-social`.
    :type share_to: :ref:`field-string-list`
    
    :param spectator_ids: **[opt]** The contact IDs of the dare spectator.
    :type spectator_ids: :ref:`field-id-list`

    .. seealso:: The definition of :ref:`Dare model <model-dare>`
    
    **Sample Responses**:
    
        .. include:: object_response

