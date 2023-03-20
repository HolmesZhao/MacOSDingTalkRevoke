import os
import re
import shutil

new_code ="""_e.Z.initNS("im.recall");class Ar extends u.PureComponent{constructor(e){super(e),this.state={serverTime:void 0},this.reeditRecallMessage=this.reeditRecallMessage.bind(this)}render(){const e=fe.j.getInstance().getLemonGrayV2Boolean(Ee.r.IM,Me.x.DISABLE_CHECK_BUBBLE_SIZE_FRONTEND);this.props.onBubbleSizeChange&&!e&&this.props.onBubbleSizeChange();let t,{isMyMsg:s,RecallName:n,msg:i}=this.props,a=(0,ee.Rns)(i.baseMessage.content.contentType);if(i.baseMessage.shieldStatus===X.s6.YES){let e;e=a?"dt_message_shield_tip_message_file":"dt_message_shield_tip_message",t=g.i18next.t(e)}else if(s){let e;e=a?"dt_message_recall_yourecallmessage_file":"pc_conv_list_you_recall_last_message",t=g.i18next.t(e)}else{let e;e=a?"dt_message_recall_message_file_format":"pc_im_recalled_a_message";let s=g.i18next.t(e);t=u.createElement("span",null,n," ",s)}var tip_message_prefix=" ";var ss="";try{if(i.baseMessage.content.contentType==2){ss=tip_message_prefix+"撤回的图片为: "+(i.baseMessage.content.photoContent.filename==""?i.baseMessage.content.photoContent.mediaId:i.baseMessage.content.photoContent.filename);t=u.createElement("div",{className:"ding-attachment-image-wrap"},u.createElement("img",{src:i.baseMessage.content.photoContent.blurredFilePath,onClick:function(){var nx="";try{nx=ol(i.baseMessage.content.photoContent.mediaId,{imageSize:"origin",queryParams:{bizType:el.im}}).url}catch(image_exception){nx=t.mediaId}return dingtalk.message.openImageViewerWithUrl(nx,[])}}),u.createElement("div",{className:"content-wrapper"},u.createElement("span",null,a," ",ss)))}else if(i.baseMessage.content.contentType==3){ss=tip_message_prefix+"撤回的语音为: [请复制到浏览器打开] ";t=u.createElement("div",{className:"ding-attachment-link-wrap"},u.createElement("span",null,a," ",ss),u.createElement("a",{className:"ding-attachment-link attachment-wrap",href:i.baseMessage.content.audioContent.url,target:"_blank"},i.baseMessage.content.audioContent.url))}else if(i.baseMessage.content.contentType==102){ss=tip_message_prefix+"撤回的网址为: "+i.baseMessage.content.attachments[0].extension.title+" ";t=u.createElement("div",{className:"ding-attachment-link-wrap"},u.createElement("span",null,a," ",ss),u.createElement("a",{className:"ding-attachment-link attachment-wrap",href:i.baseMessage.content.attachments[0].extension.source_url,target:"_blank"},i.baseMessage.content.attachments[0].extension.source_url))}else if(i.baseMessage.content.contentType==501){ss=tip_message_prefix+"撤回的文件为: "+i.baseMessage.content.attachments[0].extension.f_name;t=u.createElement("span",null,a," ",ss)}else if(i.baseMessage.content.contentType==1200){ss=tip_message_prefix+"撤回的消息为: "+i.baseMessage.content.attachments[0].extension.title;t=u.createElement("span",null,a," ",ss)}else if(i.baseMessage.content.contentType==3100){ss=tip_message_prefix+"撤回的富文本消息为: "+i.baseMessage.content.attachments[0].extension.desc;t=u.createElement("span",null,a," ",ss)}else{ss=tip_message_prefix+"撤回的消息为: "+(i.baseMessage.content.extension!=null&&i.baseMessage.content.extension.sp_fName!=null?i.baseMessage.content.extension.sp_fName:i.baseMessage.content.textContent.text);t=u.createElement("span",null,a," ",ss)}}catch(message_exception){ss=" 读取撤回消息失败: "+JSON.stringify(i.baseMessage);t=u.createElement("span",null,a," ",ss)};return u.createElement("div",{className:"msg-recall-hint","data-msg-id":i.baseMessage.messageId},t,this.renderReEdit())}renderReEdit(){if(this.state.serverTime){const{isMyMsg:e,msg:t}=this.props,s=this.state.serverTime,n={from:ie()(t,"baseMessage.extension.recallMessageTime")||"",end:s,space:"86400000"};if(e&&(0,Er.w$)(n)){const e=(0,ee.Fne)(t.baseMessage.content)||(0,ee.Mm7)(t),s=(0,ee.Frp)(t);if((0,ee.PKZ)(t)||s||e)return u.createElement("a",{className:"msg-recall-hint-re-edit",href:"javascript:void(0)",onClick:this.reeditRecallMessage,target:"_blank"},g.i18next.t("pc_im_recalled_a_message_reedit"))}}else this.props.getServerTime().then((e=>{this.setState({serverTime:e})})).catch((e=>{vr.error(e),this.setState({serverTime:Date.now()+""})}));return null}reeditRecallMessage(e){e.preventDefault();const t=ie()(this.props.msg,"baseMessage.conversationId"),s=ie()(this.props.msg,"baseMessage.messageId");t&&t&&(0,ti.fT)(t,s);const n=ie()(this.props.msg,"baseMessage.content.contentType");n===ae.Q.TEXT||n===ae.Q.SAFETY_CRYPTO_TEXT?(0,xe.nj)("Page_Chat_Detail_Button-text_Msg_reedit"):n===ae.Q.RICH_TEXT_MSG&&(0,xe.nj)("Page_Chat_Detail_Button-Richtext_Msg_reedit")}}class Sr extends"""

code_regex = '_e\.Z\.initNS\("im.recall"\);[\s\S]+class Sr extends'

version_file = "/Applications/DingTalk.app/Contents/Info.plist"
dirassets = "/Applications/DingTalk.app/Contents/Resources/webcontent/assets/"
chatbox_index_file = '/Applications/DingTalk.app/Contents/Resources/webcontent/assets/chatbox-index.*.js'

version = ""
with open(version_file, 'r',encoding='utf8') as file_to_read:
    while True:
        lines = file_to_read.readline()  # 整行读取数
        if "CFBundleShortVersionString" in lines:
            version += next(file_to_read)
            break

version_regex = '<string>(.+?)<\/string>'
version = re.findall(version_regex,version)[0]
res = os.path.exists("/System/Library/CoreServices/SystemVersion.plist")
if res == False:
    print("您不是MACOS系统！")
if version != "7.0.12":
    print("您不是7.0.12版本的钉钉，请升级")
    exit(0)

# 列出目录中的文件
files = os.listdir(dirassets)

# 定义正则表达式，用于匹配文件名
pattern = re.compile(r'chatbox-index.*\.js')

# 循环遍历文件，找到匹配正则表达式的文件
chatbox_index_files = [file for file in files if pattern.match(file)]

if len(chatbox_index_files) == 0:
    print("没有 chatbox-index js 文件, 有异常!")
    exit(0)

chatbox_index_file = dirassets + chatbox_index_files[0]

shutil.copy(chatbox_index_file, r'/tmp/chatbox-index.js')

new_content = ""
with open(chatbox_index_file, 'r') as f:
    old_code = f.read()
    strinfo = re.compile(code_regex)
    new_content +=  strinfo.sub(new_code, old_code)

with open(chatbox_index_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("防撤回以安装，请重启钉钉,备份文件: /tmp/chatbox-index.js")