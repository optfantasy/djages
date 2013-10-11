/wantto/
==============

GET
---

.. http:get:: /wantto/
    
    .. admonition:: Action
    
        Query wanttos.
    
    :param user_id: ID of the wantto creator.
    :type user_id: :ref:`field-id`

    :param city_id: ID of the searchcity.
    :type city_id: :ref:`field-id`

    :param place_id: ID of the place.
    :type place_id: :ref:`field-id`

    :param category: The category of wantto.
    :type category: string

    :param liker_id: The liker's (metoo user's) ID.
    :type liker_id: :ref:`field-id`

    :param filter_type: The filter type of special query.
    :type filter_type: string
    
    **Special Query**:

    ``filter_type: ["feed", "fname", "location"]``

    * **"feed"**:
        Use an additional parameter **time_identifier** (*string*) to query the wantto viewable by the request user.
        The return wantto will be those in between *now -> time_identifier*.
        
        **time_identifier** options: 
            ["any_time", "now", "today", "tomorrow", "this_week", "this_weekend"]
    
    * **"fname"**:
        Use an additional parameter **friend_name** (*string*) to query the wantto viewable by the request user.
        First server matches the *friend_name* with the prefix of request user's contact list and find the gulu users
        whose name match *friend_name*. Then we query out the wantto post by these users.
    
        e.g. If the client user parameter ``friend_name="saint"``, then he can get wantto post by ``sainteye, sainto...`` 
        and so on.

    * **"location"**:
        Use an additional parameter **location** (:ref:`field-location`) to query the wantto viewable by the request user.
        In short, it queries wantto nearby (within 100km) the location specified by the request user.

        
    .. seealso:: The definition of :ref:`WantTo model <model-wantto>`
        
        
    **Sample Responses**:
    
        .. include:: index_response
        

POST
----

.. http:post:: /wantto/
    
    .. admonition:: Action
    
        Create a wantto.
    
    :param category: The category of the wantto. It might be *"eat", "shop", "show", "sports", "hangout", "party"*.
    :type category: string
    
    :param time_identifier: The time of the wantto. It might be *"any_time", "now", "today", "tomorrow", "this_week", "this_weekend", "specific"*
    :type time_identifier: string
    
    :param city_id: The city ID for the wantto.
    :type city_id: :ref:`field-id`
    
    :param place_id: **[opt]** The place ID for the wantto.
    :type place_id: :ref:`field-id`
    
    :param photo_id: **[opt]** The photo ID for the wantto.
    :type photo_id: :ref:`field-id`
    
    :param share_to: **[opt]** Share the wantto to social network. Options are :ref:`enum-social`.
    :type share_to: :ref:`field-string-list`
        
    :param contact_ids: **[opt]** The contact IDs of the wantto creator. Server will notify these users by email and notification.
    :type contact_ids: :ref:`field-id-list`
    
    :param emails: **[opt]** Server will send email to these addresses.
    :type emails: :ref:`field-email-list`
    
    :param expiry: **[opt]** When the parameter **time_identifier** is *"specific"*, the client must specify expiry.
    :type expiry: :ref:`field-date`
    

    .. seealso:: The definition of :ref:`WantTo model <model-wantto>`
    
    **Sample Responses**:
    
        .. include:: object_response

