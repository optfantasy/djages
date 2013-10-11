/user/(actor_id)/friends/(target_id)/
======================================

GET
---

.. http:get:: /user/(actor_id)/friends/(target_id)/

    .. admonition:: Action
    
        Check the friend status between actor and target user.
    
    :param actor_id: ID of the actor
    :type actor_id: :ref:`field-id`
    :param target_id: ID of the target user
    :type target_id: :ref:`field-id`
    
    Return **friend_status** (*int*) to stand for the friend status between actor and target user.
    
    **friend_status** (*int*):
        * 0: No request has been made
        * 1: Pending
        * 2: Accepted (already friends)
        * 3: Reject
        
    **Sample Responses**:

        .. code-block:: js
        
            {
                "response": {
                    "friend_status": 2
                },
                "success": true
            }


POST
-----

.. http:post:: /user/(actor_id)/friends/(target_id)/

    .. admonition:: Action
    
        This method provides two functions:

        1. Make a friend request from actor to target user.
        2. Make a friend response from actor to target user. In this case, there must be a friend request from target user to actor.

    
    :param actor_id: ID of the actor
    :type actor_id: :ref:`field-id`
    :param target_id: ID of the target user
    :type target_id: :ref:`field-id`
    :param respond: Respond of the friending request. It might be *"accept", "deny"*
    :type respond: string
    
    **Sample Responses**:

        .. include:: ../null_response
        .. include:: ../errors/10007
        .. include:: ../errors/10102
        
