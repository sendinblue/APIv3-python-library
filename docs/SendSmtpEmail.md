# SendSmtpEmail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **object** | Mandatory if &#x27;templateId&#x27; is not passed. Pass name (optional) and email of sender from which emails will be sent. For example, &#x60;{\&quot;name\&quot;:\&quot;Mary from MyShop\&quot;, \&quot;email\&quot;:\&quot;no-reply@myshop.com\&quot;}&#x60; | [optional] 
**to** | **list[object]** | List of email addresses and names (optional) of the recipients. For example, &#x60;[{\&quot;name\&quot;:\&quot;Jimmy\&quot;, \&quot;email\&quot;:\&quot;jimmy98@example.com\&quot;}, {\&quot;name\&quot;:\&quot;Joe\&quot;, \&quot;email\&quot;:\&quot;joe@example.com\&quot;}]&#x60; | 
**bcc** | **list[object]** | List of email addresses and names (optional) of the recipients in bcc | [optional] 
**cc** | **list[object]** | List of email addresses and names (optional) of the recipients in cc | [optional] 
**html_content** | **str** | HTML body of the message ( Mandatory if &#x27;templateId&#x27; is not passed, ignored if &#x27;templateId&#x27; is passed ) | [optional] 
**text_content** | **str** | Plain Text body of the message ( Ignored if &#x27;templateId&#x27; is passed ) | [optional] 
**subject** | **str** | Subject of the message. Mandatory if &#x27;templateId&#x27; is not passed | [optional] 
**reply_to** | **object** | Email (required), along with name (optional), on which transactional mail recipients will be able to reply back. For example, &#x60;{\&quot;email&#x27;:&#x27;ann6533@example.com&#x27;, &#x27;name&#x27;:&#x27;Ann&#x27;}&#x60; | [optional] 
**attachment** | **list[object]** | Pass the absolute URL (no local file) or the base64 content of the attachment along with the attachment name (Mandatory if attachment content is passed). For example, &#x60;[{\&quot;url\&quot;:\&quot;https://attachment.domain.com/myAttachmentFromUrl.jpg\&quot;, \&quot;name\&quot;:\&quot;My attachment 1\&quot;}, {\&quot;content\&quot;:\&quot;base64 exmaple content\&quot;, \&quot;name\&quot;:\&quot;My attachment 2\&quot;}]&#x60;. Allowed extensions for attachment file: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub, eps and odt ( If &#x27;templateId&#x27; is passed and is in New Template Language format then only attachment url is accepted. If template is in Old template Language format, then &#x27;attachment&#x27; is ignored ) | [optional] 
**headers** | **object** | Pass the set of headers that shall be sent along the mail headers in the original email. &#x27;sender.ip&#x27; header can be set (only for dedicated ip users) to mention the IP to be used for sending transactional emails. For example, &#x60;{\&quot;Content-Type\&quot;:\&quot;text/html\&quot;, \&quot;charset\&quot;:\&quot;iso-8859-1\&quot;, \&quot;sender.ip\&quot;:\&quot;1.2.3.4\&quot;}&#x60; | [optional] 
**template_id** | **int** | Id of the template | [optional] 
**params** | **object** | Pass the set of attributes to customize the template. For example, &#x60;{\&quot;FNAME\&quot;:\&quot;Joe\&quot;, \&quot;LNAME\&quot;:\&quot;Doe\&quot;}&#x60;. It&#x27;s considered only if template is in New Template Language format. | [optional] 
**tags** | **list[str]** | Tag your emails to find them more easily | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

