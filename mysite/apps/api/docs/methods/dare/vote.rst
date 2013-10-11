/dare/(dare_id)/vote
==========================

GET
---

.. http:get:: /dare/(dare_id)/vote
    
    .. admonition:: Action
    
        Get the vote status of the request user for the dare object.
    
    :param dare_id: ID of a dare
    :type dare_id: :ref:`field-id`
    
    Return a string - **vote_type**. The vote status. It might be *'yes','no','ttu','ef'*.
    
    .. seealso:: The definition of :ref:`Dare model <model-dare>`

    **Sample Responses**:

        .. code-block:: js
        
            {
               "response": {
                  "vote_type": "yes"
               },
               "success": true
            }

POST
----

.. http:post:: /dare/(dare_id)/vote
    
    .. admonition:: Action
    
        Vote a dare.
    
    :param dare_id: ID of a dare
    :type dare_id: :ref:`field-id`
    
    :param vote_type: Vote type. The choices are *'yes','no','ttu','ef'*.
    :type vote_type: string
    
    
    .. seealso:: The definition of :ref:`Dare model <model-dare>`
    
    **Sample Responses**:
    
        .. include:: ../null_response

