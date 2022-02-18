# Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_contact** | [**Contact**](Contact.md) |  | [optional] 
**id** | **str** | Unique task id | [optional] 
**task_type_id** | **str** | Id for type of task e.g Call / Email / Meeting etc. | 
**name** | **str** | Name of task | 
**contacts_ids** | **list[int]** | Contact ids for contacts linked to this task | [optional] 
**contacts** | [**list[Contact]**](Contact.md) | Contact details for contacts linked to this task | [optional] 
**deals_ids** | **list[str]** | Deal ids for deals a task is linked to | [optional] 
**companies_ids** | **list[str]** | Companies ids for companies a task is linked to | [optional] 
**assign_to_id** | **str** | User id to whom task is assigned | [optional] 
**_date** | **datetime** | Task date/time | 
**duration** | **int** | Duration of task | [optional] 
**notes** | **str** | Notes added to a task | [optional] 
**done** | **bool** | Task marked as done | [optional] 
**reminder** | [**TaskReminder**](TaskReminder.md) | Task reminder date/time for a task | [optional] 
**created_at** | **datetime** | Task created date/time | [optional] 
**updated_at** | **datetime** | Task update date/time | [optional] 
**refs** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


