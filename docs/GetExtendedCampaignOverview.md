# GetExtendedCampaignOverview

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the campaign | 
**name** | **str** | Name of the campaign | 
**subject** | **str** | Subject of the campaign. Only available if &#x60;abTesting&#x60; flag of the campaign is &#x60;false&#x60; | [optional] 
**type** | **str** | Type of campaign | 
**status** | **str** | Status of the campaign | 
**scheduled_at** | **str** | UTC date-time on which campaign is scheduled (YYYY-MM-DDTHH:mm:ss.SSSZ) | [optional] 
**ab_testing** | **bool** | Status of A/B Test for the campaign. abTesting &#x3D; false means it is disabled, &amp; abTesting &#x3D; true means it is enabled. | [optional] 
**subject_a** | **str** | Subject A of the ab-test campaign. Only available if &#x60;abTesting&#x60; flag of the campaign is &#x60;true&#x60; | [optional] 
**subject_b** | **str** | Subject B of the ab-test campaign. Only available if &#x60;abTesting&#x60; flag of the campaign is &#x60;true&#x60; | [optional] 
**split_rule** | **int** | The size of your ab-test groups. Only available if &#x60;abTesting&#x60; flag of the campaign is &#x60;true&#x60; | [optional] 
**winner_criteria** | **str** | Criteria for the winning version. Only available if &#x60;abTesting&#x60; flag of the campaign is &#x60;true&#x60; | [optional] 
**winner_delay** | **int** | The duration of the test in hours at the end of which the winning version will be sent. Only available if &#x60;abTesting&#x60; flag of the campaign is &#x60;true&#x60; | [optional] 
**send_at_best_time** | **bool** | It is true if you have chosen to send your campaign at best time, otherwise it is false | [optional] 
**test_sent** | **bool** | Retrieved the status of test email sending. (true&#x3D;Test email has been sent  false&#x3D;Test email has not been sent) | 
**header** | **str** | Header of the campaign | 
**footer** | **str** | Footer of the campaign | 
**sender** | [**GetExtendedCampaignOverviewSender**](GetExtendedCampaignOverviewSender.md) |  | 
**reply_to** | **str** | Email defined as the \&quot;Reply to\&quot; of the campaign | 
**to_field** | **str** | Customisation of the \&quot;to\&quot; field of the campaign | [optional] 
**html_content** | **str** | HTML content of the campaign | 
**share_link** | **str** | Link to share the campaign on social medias | [optional] 
**tag** | **str** | Tag of the campaign | [optional] 
**created_at** | **str** | Creation UTC date-time of the campaign (YYYY-MM-DDTHH:mm:ss.SSSZ) | 
**modified_at** | **str** | UTC date-time of last modification of the campaign (YYYY-MM-DDTHH:mm:ss.SSSZ) | 
**inline_image_activation** | **bool** | Status of inline image. inlineImageActivation &#x3D; false means image can’t be embedded, &amp; inlineImageActivation &#x3D; true means image can be embedded, in the email. | [optional] 
**mirror_active** | **bool** | Status of mirror links in campaign. mirrorActive &#x3D; false means mirror links are deactivated, &amp; mirrorActive &#x3D; true means mirror links are activated, in the campaign | [optional] 
**recurring** | **bool** | FOR TRIGGER ONLY ! Type of trigger campaign.recurring &#x3D; false means contact can receive the same Trigger campaign only once, &amp; recurring &#x3D; true means contact can receive the same Trigger campaign several times | [optional] 
**sent_date** | **str** | Sent UTC date-time of the campaign (YYYY-MM-DDTHH:mm:ss.SSSZ). Only available if &#39;status&#39; of the campaign is &#39;sent&#39; | [optional] 
**return_bounce** | **int** | Total number of non-delivered campaigns for a particular campaign id. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


