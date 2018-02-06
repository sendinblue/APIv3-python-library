# SendEmail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_to** | **list[str]** | Email addresses of the recipients | 
**email_bcc** | **list[str]** | Email addresses of the recipients in bcc | [optional] 
**email_cc** | **list[str]** | Email addresses of the recipients in cc | [optional] 
**reply_to** | **str** | Email on which campaign recipients will be able to reply to | [optional] 
**attachment_url** | **str** | Absolute url of the attachment (no local file). Extension allowed: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps | [optional] 
**attachment** | [**list[SendEmailAttachment]**](SendEmailAttachment.md) | Pass the base64 content of the attachment. Extension allowed: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps | [optional] 
**headers** | **dict(str, str)** |  | [optional] 
**attributes** | **dict(str, str)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


