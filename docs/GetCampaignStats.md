# GetCampaignStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **int** | List Id of email campaign (only in case of get email campaign(s)(not for global stats)) | [optional] 
**unique_clicks** | **int** | Number of unique clicks for the campaign | 
**clickers** | **int** | Number of total clicks for the campaign | 
**complaints** | **int** | Number of complaints (Spam reports) for the campaign | 
**delivered** | **int** | Number of delivered emails for the campaign | 
**sent** | **int** | Number of sent emails for the campaign | 
**soft_bounces** | **int** | Number of softbounce for the campaign | 
**hard_bounces** | **int** | Number of harbounce for the campaign | 
**unique_views** | **int** | Number of unique openings for the campaign | 
**trackable_views** | **int** | Recipients without any privacy protection option enabled in their email client | 
**trackable_views_rate** | **float** | Rate of recipients without any privacy protection option enabled in their email client | [optional] 
**estimated_views** | **int** | Rate of recipients without any privacy protection option enabled in their email client, applied to all delivered emails | [optional] 
**unsubscriptions** | **int** | Number of unsubscription for the campaign | 
**viewed** | **int** | Number of openings for the campaign | 
**deferred** | **int** | Number of deferred emails for the campaign | [optional] 
**return_bounce** | **int** | Total number of non-delivered campaigns for a particular campaign id. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


