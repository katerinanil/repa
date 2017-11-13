import re
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import config
import getQuery
from lemmatizer import lemmatizer

class myHandler(BaseHTTPRequestHandler):
    lemma = lemmatizer()
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
                &nbsp;&nbsp;&nbsp;&nbsp;<b><i>Искать в документах:</b></i>&nbsp;
                <input type="text" name="doc_count" value=
    '''
    HTML_DOC_3 = \
    '''>
                &nbsp;&nbsp;&nbsp;&nbsp;<b><i>Начиная с:</b></i>&nbsp;
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
            qres = getQuery.query(inputWords, config.DATABASE_NAME,
                myHandler.lemma, doc_count, doc_start, myHandler.QUTES_COUNTS)
            resDict = getQuery.makeContexts(qres)
            myHandler.QUTES_COUNTS = []
            for i, path in enumerate(resDict):
                myHandler.QUTES_COUNTS.append((None, None))
                result_line += r'<li>'  + '<b>' + path + '</b>' + r'<ul>'
                tup = resDict[path]
                for context, positions in zip(tup[0], tup[1]):
                    result_line += r'<li>'
                    result_line += context[:positions[0][0]]
                    for i in range(len(positions)-1):
                        pos = positions[i]
                        result_line += '<b>'
                        result_line += context[pos[0]:pos[1]]
                        result_line += '</b>'
                        result_line += context[pos[1]:positions[i+1][0]]
                    last_pos = positions[-1]
                    result_line += '<b>'
                    result_line += context[last_pos[0]:last_pos[1]]
                    result_line += '</b>'
                    result_line += context[last_pos[1]:]
                    result_line += r'</li>'
                result_line += r'</ul><p>'
                result_line += '<b><i>&nbsp;&nbsp;Количество цитат:</b></i>&nbsp;&nbsp;'
                result_line += \
                    r'<input type="text" name="countQuote' + str(i) + r'">'
                result_line += '<b><i>&nbsp;&nbsp;&nbsp;&nbsp;Начиная с:</b></i>&nbsp;&nbsp;'
                result_line += \
                    r'<input type="text" name="startQuote' + str(i) + r'">'
                result_line += r'</li></p>'
            if len(result_line) != 0:
                result_line = r'<ol type="I">' + result_line + r'</ol>'
            else:
                result_line = '<p>Ничего не найдено. Искать в Яндекс, Google, Mail.ru</p>'
        else:
            result_line = '<p><p><p>Задан пустой поисковый запрос</p></p></p>'
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
