# UpdateEmailCampaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | Tag of the campaign | [optional] 
**sender** | **object** | Sender details including email and/or name. For example &#x60;{\&quot;name\&quot;:\&quot;xyz\&quot;, \&quot;email\&quot;:\&quot;example@abc.com\&quot;}&#x60; | [optional] 
**name** | **str** | Name of the campaign | [optional] 
**html_content** | **str** | Body of the message (HTML version). REQUIRED if htmlUrl is empty | [optional] 
**html_url** | **str** | Url which contents the body of the email message. REQUIRED if htmlContent is empty | [optional] 
**scheduled_at** | **datetime** | UTC date-time on which the campaign has to run (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result. If sendAtBestTime is set to true, your campaign will be sent according to the date passed (ignoring the time part). | [optional] 
**subject** | **str** | Subject of the campaign | [optional] 
**reply_to** | **str** | Email on which campaign recipients will be able to reply to | [optional] 
**to_field** | **str** | To personalize the «To» Field. If you want to include the first name and last name of your recipient, add &#x60;{FNAME} {LNAME}&#x60;. These contact attributes must already exist in your SendinBlue account. If input parameter &#x27;params&#x27; used please use &#x60;{{contact.FNAME}} {{contact.LNAME}}&#x60; for personalization | [optional] 
**recipients** | **object** | List ids to include/exclude from campaign | [optional] 
**attachment_url** | **str** | Absolute url of the attachment (no local file). Extension allowed: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps | [optional] 
**inline_image_activation** | **bool** | Status of inline image. inlineImageActivation &#x3D; false means image can’t be embedded, &amp; inlineImageActivation &#x3D; true means image can be embedded, in the email. You cannot send a campaign of more than 4MB with images embedded in the email. Campaigns with the images embedded in the email must be sent to less than 5000 contacts. | [optional] [default to False]
**mirror_active** | **bool** | Status of mirror links in campaign. mirrorActive &#x3D; false means mirror links are deactivated, &amp; mirrorActive &#x3D; true means mirror links are activated, in the campaign | [optional] 
**recurring** | **bool** | FOR TRIGGER ONLY ! Type of trigger campaign.recurring &#x3D; false means contact can receive the same Trigger campaign only once, &amp; recurring &#x3D; true means contact can receive the same Trigger campaign several times | [optional] [default to False]
**footer** | **str** | Footer of the email campaign | [optional] 
**header** | **str** | Header of the email campaign | [optional] 
**utm_campaign** | **str** | Customize the utm_campaign value. If this field is empty, the campaign name will be used. Only alphanumeric characters and spaces are allowed | [optional] 
**params** | **object** | Pass the set of attributes to customize the type &#x27;classic&#x27; campaign. For example, &#x60;{\&quot;FNAME\&quot;:\&quot;Joe\&quot;, \&quot;LNAME\&quot;:\&quot;Doe\&quot;}&#x60;. The &#x27;params&#x27; field will get updated, only if the campaign is in New Template Language, else ignored. The New Template Language is dependent on the values of &#x27;subject&#x27;, &#x27;htmlContent/htmlUrl&#x27;, &#x27;sender.name&#x27; &amp; &#x27;toField&#x27; | [optional] 
**send_at_best_time** | **bool** | Set this to true if you want to send your campaign at best time. Note:- if true, warmup ip will be disabled. | [optional] 
**ab_testing** | **bool** | Status of A/B Test. abTesting &#x3D; false means it is disabled, &amp; abTesting &#x3D; true means it is enabled. &#x27;subjectA&#x27;, &#x27;subjectB&#x27;, &#x27;splitRule&#x27;, &#x27;winnerCriteria&#x27; &amp; &#x27;winnerDelay&#x27; will be considered if abTesting is set to true. &#x27;subject&#x27; if passed is ignored.  Can be set to true only if &#x27;sendAtBestTime&#x27; is &#x27;false&#x27;. You will be able to set up two subject lines for your campaign and send them to a random sample of your total recipients. Half of the test group will receive version A, and the other half will receive version B | [optional] [default to False]
**subject_a** | **str** | Subject A of the campaign. Considered if abTesting &#x3D; true. subjectA &amp; subjectB should have unique value | [optional] 
**subject_b** | **str** | Subject B of the campaign. Considered if abTesting &#x3D; true. subjectA &amp; subjectB should have unique value | [optional] 
**split_rule** | **int** | Add the size of your test groups. Considered if abTesting &#x3D; true. We&#x27;ll send version A and B to a random sample of recipients, and then the winning version to everyone else | [optional] 
**winner_criteria** | **str** | Choose the metrics that will determinate the winning version. Considered if &#x27;splitRule&#x27; &gt;&#x3D; 1 and &lt; 50. If splitRule &#x3D; 50, &#x27;winnerCriteria&#x27; is ignored if passed or alreday exist in record | [optional] 
**winner_delay** | **int** | Choose the duration of the test in hours. Maximum is 7 days, pass 24*7 &#x3D; 168 hours. The winning version will be sent at the end of the test. Considered if &#x27;splitRule&#x27; &gt;&#x3D; 1 and &lt; 50. If splitRule &#x3D; 50, &#x27;winnerDelay&#x27; is ignored if passed or alreday exist in record | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

