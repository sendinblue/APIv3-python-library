# CreateAttribute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the attribute. Use only if the attribute&#x27;s category is &#x27;calculated&#x27; or &#x27;global&#x27; | [optional] 
**enumeration** | **list[object]** | List of values and labels that the attribute can take. Use only if the attribute&#x27;s category is \&quot;category\&quot;. For example, &#x60;[{\&quot;value\&quot;:1, \&quot;label\&quot;:\&quot;male\&quot;}, {\&quot;value\&quot;:2, \&quot;label\&quot;:\&quot;female\&quot;}]&#x60; | [optional] 
**type** | **str** | Type of the attribute. Use only if the attribute&#x27;s category is &#x27;normal&#x27;, &#x27;category&#x27; or &#x27;transactional&#x27; ( type &#x27;boolean&#x27; is only available if the category is &#x27;normal&#x27; attribute, type &#x27;id&#x27; is only available if the category is &#x27;transactional&#x27; attribute &amp; type &#x27;category&#x27; is only available if the category is &#x27;category&#x27; attribute ) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

