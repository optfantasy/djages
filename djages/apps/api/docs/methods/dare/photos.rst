/dare/(dare_id)/photos/
==============================

POST
-----

.. http:post:: /dare/(dare_id)/photos/
    
    .. admonition:: Action
    
        Create photo. Then submit it to a dare.
    
    :param dare_id: ID of a dare
    :type dare_id: :ref:`field-id`
    
    Other parameters please refer to :ref:`Create Photo API <api-photos-create>`.
    
    .. seealso:: The definition of :ref:`Dare model <model-dare>` and :ref:`Photo model <model-photo>`
    
    **Sample Responses**:

        .. include:: ../photos/object_response

