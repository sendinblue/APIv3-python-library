# SendSmtpEmail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | [**SendSmtpEmailSender**](SendSmtpEmailSender.md) |  | [optional] 
**to** | [**list[SendSmtpEmailTo]**](SendSmtpEmailTo.md) | Email addresses and names of the recipients | 
**bcc** | [**list[SendSmtpEmailBcc]**](SendSmtpEmailBcc.md) | Email addresses and names of the recipients in bcc | [optional] 
**cc** | [**list[SendSmtpEmailCc]**](SendSmtpEmailCc.md) | Email addresses and names of the recipients in cc | [optional] 
**html_content** | **str** | HTML body of the message ( Mandatory if &#39;templateId&#39; is not passed, ignored if &#39;templateId&#39; is passed ) | [optional] 
**text_content** | **str** | Plain Text body of the message ( Ignored if &#39;templateId&#39; is passed ) | [optional] 
**subject** | **str** | Subject of the message. Mandatory if &#39;templateId&#39; is not passed | [optional] 
**reply_to** | [**SendSmtpEmailReplyTo**](SendSmtpEmailReplyTo.md) |  | [optional] 
**attachment** | [**list[SendSmtpEmailAttachment]**](SendSmtpEmailAttachment.md) | Pass the absolute URL (no local file) or the base64 content of the attachment. Name can be used in both cases to define the attachment name. It is mandatory in case of content. Extension allowed: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps ( Ignored if &#39;templateId&#39; is passed ) | [optional] 
**headers** | **dict(str, str)** |  | [optional] 
**template_id** | **int** | Id of the template | [optional] 
**params** | **dict(str, str)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


