# CreateSmtpTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | Tag of the template | [optional] 
**sender** | [**CreateSmtpTemplateSender**](CreateSmtpTemplateSender.md) |  | 
**template_name** | **str** | Name of the template | 
**html_content** | **str** | Body of the message (HTML version). The field must have more than 10 characters. REQUIRED if htmlUrl is empty | [optional] 
**html_url** | **str** | Url which contents the body of the email message. REQUIRED if htmlContent is empty | [optional] 
**subject** | **str** | Subject of the template | 
**reply_to** | **str** | Email on which campaign recipients will be able to reply to | [optional] 
**to_field** | **str** | To personalize the «To» Field. If you want to include the first name and last name of your recipient, add &#x60;{FNAME} {LNAME}&#x60;. These contact attributes must already exist in your SendinBlue account. If input parameter &#39;params&#39; used please use &#x60;{{contact.FNAME}} {{contact.LNAME}}&#x60; for personalization | [optional] 
**attachment_url** | **str** | Absolute url of the attachment (no local file). Extension allowed: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps | [optional] 
**is_active** | **bool** | Status of template. isActive &#x3D; true means template is active and isActive &#x3D; false means template is inactive | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


