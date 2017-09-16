import re
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import config
import stolenQuery4 as stolenQuery

class myHandler(BaseHTTPRequestHandler):
    LAST_QUERY = ''
    LAST_DOC_COUNT = ''
    LAST_DOC_START = ''
    QUTES_COUNTS = None
    HTML_DOC_1 = \
    '''
    <html>
        <head>
            <title>Vkladka</title>
        </head>
        <body>
            <form action="" method="POST">
                <input type="text" name="query" value=
    '''
    HTML_DOC_2 = \
    '''
    >
                <input type="submit" value="Go!">
                &nbsp;&nbsp;&nbsp;&nbsp;Искать в документах:&nbsp;
                <input type="text" name="doc_count" value=
    '''
    HTML_DOC_3 = \
    '''>
                &nbsp;&nbsp;&nbsp;&nbsp;Начиная с:&nbsp;
                <input type="text" name="doc_start" value=
    '''
    HTML_DOC_4 = \
    '''>
    '''
    HTML_DOC_5 = \
    """
            </form>
        </body>
    </html>
    """

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(
            bytes(myHandler.HTML_DOC_1 + '""' + myHandler.HTML_DOC_2 + '""' +
                myHandler.HTML_DOC_3 + '""' + myHandler.HTML_DOC_4 +
                myHandler.HTML_DOC_5, encoding='utf-8'))
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type']})
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        inputWords = form.getvalue('query')
        doc_count = form.getvalue('doc_count')
        doc_start = form.getvalue('doc_start')
        try:
            doc_count = int(doc_count)
            if doc_count < 0: doc_count = -1
        except: doc_count = -1
        try:
            doc_start = int(doc_start)
            if doc_start <= 0: doc_start = -1
        except: doc_start = -1
        result_line = ''
        if inputWords != None:
            if myHandler.LAST_QUERY == inputWords and \
               myHandler.LAST_DOC_COUNT == doc_count and \
               myHandler.LAST_DOC_START == doc_start:
                print('YES')
                for i in range(len(myHandler.QUTES_COUNTS)):
                    countQuote = form.getvalue('countQuote' + str(i))
                    #print('CQ =', countQuote, 'i =', i)
                    try: countQuote= int(countQuote)
                    except: countQuote = None
                    startQuote = form.getvalue('startQuote' + str(i))
                    try: startQuote = int(startQuote)
                    except: startQuote = None
                    myHandler.QUTES_COUNTS[i] = (countQuote, startQuote)
            else:
                print('NO', 'LQ =', myHandler.LAST_QUERY, 'LDC =', \
                       myHandler.LAST_DOC_COUNT, 'LDS =', \
                       myHandler.LAST_DOC_START, 'Q =', inputWords, \
                      'DC =', doc_count, 'DS =', doc_start)
                myHandler.QUTES_COUNTS = None
            print('QQ =', myHandler.QUTES_COUNTS)
            qres = stolenQuery.query(inputWords, config.DATABASE_NAME,
                doc_count, doc_start, myHandler.QUTES_COUNTS)
            resDict = stolenQuery.makeContexts(qres)
            myHandler.QUTES_COUNTS = []
            for i, path in enumerate(resDict):
                myHandler.QUTES_COUNTS.append((None, None))
                result_line += r'<li>' + path + r'<ul>'
                for context in resDict[path]:
                    result_line += r'<li>'
                    context = ' ' + context + ' '
                    for w in filter(bool, inputWords.split()):
                        context = re.sub('(\W)(' + w + ')(\W)', \
                            '\g<1><b>' + '\g<2>' + '</b>\g<3>', \
                            context, flags=re.I)
                    result_line += context[1:-1]
                    result_line += r'</li>'
                result_line += r'</ul>'
                result_line += 'Количество цитат:'
                result_line += \
                    r'<input type="text" name="countQuote' + str(i) + r'">'
                result_line += 'Начинать с'
                result_line += \
                    r'<input type="text" name="startQuote' + str(i) + r'">'
                result_line += r'</li>'
            if len(result_line) != 0:
                result_line = r'<ol type="1">' + result_line + r'</ol>'
            else:
                result_line = '<p>Ничего не найдено. Искать в Яндекс, Google, Mail.ru</p>'
        else:
            result_line = 'Вы ничего не ввели'
            inputWords = ''
        myHandler.LAST_QUERY = inputWords
        myHandler.LAST_DOC_COUNT = doc_count
        myHandler.LAST_DOC_START = doc_start
        if doc_count == -1: doc_count = ''
        else: doc_count = str(doc_count)
        if doc_start == -1: doc_start = ''
        self.wfile.write(
            bytes(myHandler.HTML_DOC_1 + '"' + inputWords + '"' +
                  myHandler.HTML_DOC_2 + '"' + str(doc_count) + '"' +
                  myHandler.HTML_DOC_3 + '"' + str(doc_start) + '"' +
                  myHandler.HTML_DOC_4 + result_line +
                  myHandler.HTML_DOC_5, encoding = 'utf-8'))

try:
    PORT_NUMBER = 8080
    server = HTTPServer(("", PORT_NUMBER), myHandler)
    print("Started httpserver on port", PORT_NUMBER)
    server.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
