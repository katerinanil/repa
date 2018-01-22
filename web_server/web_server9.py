import re
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import config
import getQuery
from lemmatizer import lemmatizer

class myHandler(BaseHTTPRequestHandler):
    lemma = lemmatizer()
    QUERY = ''
    DOC_COUNT = 2
    DOC_START = 1
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
                <input type="submit" name="search" value="&#128270;">&emsp;&emsp;&emsp;&emsp;&emsp;
                <input type="submit" name="begin" value="В начало">
                <input type="submit" name="back" value="Назад">
                <input type="submit" name="forward" value="Вперед">
                <input type="text" name="doc_count" value=
    '''
    HTML_DOC_3 = \
    '''">
    '''
    HTML_DOC_4 = \
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
            bytes(myHandler.HTML_DOC_1 + '""' + myHandler.HTML_DOC_2  + \
                '"' + str(myHandler.DOC_COUNT) + myHandler.HTML_DOC_3 +
                myHandler.HTML_DOC_4, encoding='utf-8'))
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type']})
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        inputWords = form.getvalue('query').lower()
        doc_count = form.getvalue('doc_count')
        try:
            doc_count = int(doc_count)
            if doc_count < 0: doc_count = 2
        except: doc_count = 2

        if form.getvalue('begin'):
            myHandler.DOC_START = 1
        elif form.getvalue('back'):
            sh = doc_count
            if myHandler.DOC_START - sh < 1:
                sh = myHandler.DOC_START - 1
            myHandler.DOC_START -= sh
        elif form.getfirst('forward'):
            myHandler.DOC_START += doc_count

        result_line = ''
        if inputWords != None:
            if myHandler.QUERY == inputWords and \
               myHandler.DOC_COUNT == doc_count:
                for i in range(len(myHandler.QUTES_COUNTS)):
                    countQuote = form.getvalue('countQuote' + str(i))
                    try: countQuote= int(countQuote)
                    except: countQuote = 10
                    if form.getvalue('beginQuote' + str(i)):
                        myHandler.QUTES_COUNTS[i] = [countQuote, 0]
                    elif form.getvalue('backQuote' + str(i)):
                        sh = countQuote
                        if myHandler.QUTES_COUNTS[i][1] - sh < 0:
                            sh = mmyHandler.QUTES_COUNTS[i][1]
                        myHandler.QUTES_COUNTS[i][1] -= sh
                    elif form.getfirst('forwardQuote' + str(i)):
                        myHandler.QUTES_COUNTS[i][1] += countQuote
                    myHandler.QUTES_COUNTS[i][0] = countQuote
            else:
                myHandler.DOC_START = 1
                myHandler.DOC_COUNT = 2
                myHandler.QUERY = inputWords
                myHandler.QUTES_COUNTS = []
                for i in range(myHandler.DOC_COUNT):
                    myHandler.QUTES_COUNTS.append([10, 0])
            qres = getQuery.query(inputWords, config.DATABASE_NAME,
                myHandler.lemma, doc_count, myHandler.DOC_START, myHandler.QUTES_COUNTS)
            #resDict - { 'path' : ( [ 'context' ], [ [ (stBoldWord_1 , endBoldWord_1), (stBoldWord_2 , endBoldWord_2) ] ] ) }
            resDict = getQuery.makeContexts(qres, myHandler.QUTES_COUNTS)
            
            newQuotes = myHandler.QUTES_COUNTS == None
            if newQuotes: myHandler.QUTES_COUNTS = []
            for i, path in enumerate(resDict):
                if newQuotes: myHandler.QUTES_COUNTS.append([10, 0])
                #list for documents
                result_line += r'<li>'  + r'<b>' + path + r'</b>' + r'<ul>'
                tup = resDict[path]
                for context, positions in zip(tup[0], tup[1]):
                    #list for contexts
                    result_line += r'<li>'
                    result_line += context[:positions[0][0]]
                    for j in range(len(positions)-1):
                        pos = positions[j]
                        result_line += r'<b>'
                        result_line += context[pos[0]:pos[1]]
                        result_line += r'</b>'
                        result_line += context[pos[1]:positions[j+1][0]]
                    #code for last bold word in context
                    last_pos = positions[-1]
                    result_line += r'<b>'
                    result_line += context[last_pos[0]:last_pos[1]]
                    result_line += r'</b>'
                    result_line += context[last_pos[1]:]
                    result_line += r'</li>'
                result_line += r'</ul><p>'
                result_line += r'<input type="submit" name="beginQuote' + str(i) + '" value="В начало">'
                result_line += r'<input type="submit" name="backQuote' + str(i) + '" value="Назад">'
                result_line += r'<input type="submit" name="forwardQuote' + str(i) + '" value="Вперед">'
                result_line += r'<input type="text" name="countQuote' + str(i) + r'" value="'
                countQuote = myHandler.QUTES_COUNTS[i][0]
                result_line += str(countQuote) + r'"></li></p>'
            if len(result_line) != 0:
                result_line = r'<ol type="I">' + result_line + r'</ol>'
            else:
                result_line = r'<p>Ничего не найдено. Искать в Яндекс, Google, Mail.ru</p>'
        else:
            result_line = r'<p><p><p>Задан пустой поисковый запрос</p></p></p>'
            inputWords = ''
        myHandler.QUERY = inputWords
        myHandler.DOC_COUNT = doc_count
        self.wfile.write(
            bytes(myHandler.HTML_DOC_1 + '"' + myHandler.QUERY + '"' +
                  myHandler.HTML_DOC_2 + '"' + str(myHandler.DOC_COUNT) +
                  myHandler.HTML_DOC_3 + result_line +
                  myHandler.HTML_DOC_4, encoding = 'utf-8'))

try:
    PORT_NUMBER = 8080
    server = HTTPServer(("", PORT_NUMBER), myHandler)
    print("Started httpserver on port", PORT_NUMBER)
    server.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
