# SendEmail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_to** | **list[str]** | Email addresses of the recipients | 
**email_bcc** | **list[str]** | Email addresses of the recipients in bcc | [optional] 
**email_cc** | **list[str]** | Email addresses of the recipients in cc | [optional] 
**reply_to** | **str** | Email on which campaign recipients will be able to reply to | [optional] 
**attachment_url** | **str** | Absolute url of the attachment (no local file). Extension allowed: gif, png, bmp, cgm, jpg, jpeg, tif, tiff, rtf, txt, css, shtml, html, htm, csv, zip, pdf, xml, ods, doc, docx, docm, ics, xls, xlsx, ppt, tar, and ez | [optional] 
**attachment** | [**list[SendEmailAttachment]**](SendEmailAttachment.md) | Pass the base64 content of the attachment. Extension allowed: gif, png, bmp, cgm, jpg, jpeg, tif, tiff, rtf, txt, css, shtml, html, htm, csv, zip, pdf, xml, ods, doc, docx, docm, ics, xls, xlsx, ppt, tar, and ez | [optional] 
**headers** | **dict(str, str)** |  | [optional] 
**attributes** | **dict(str, str)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


