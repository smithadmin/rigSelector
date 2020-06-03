#!/usr/local/bin/python3.6

"""
   Author: William Smith

   This is a work in progress.

   History:
      0.3 - Normalized DB and updated queries to match
      0.2 - Added DB bits and cleaned up a few things
      0.1 - Initial release uploaded to GitHub
"""

import cgi
import cgitb; cgitb.enable()
import sqlite3

DEBUGGING = True

def print_header():
   """
      This section prints everything for the Header, up to (and including) the Header class.
   """
   print('Content-Type: text/html')
   print('')
   print('<html><head><title>rigSelector</title><link rel="stylesheet" href="split2.css"></head><body>')
   print('<div class="wrapper">')
   print('<h1>rigSelector (demo)</h1>')
   print('<header>&nbsp;Let\'s see what we can do to help you on your search for your next rig!<br/>')
   print('&nbsp;The purpose here is to help provide a list of equipment that may satisfy your needs.<br>')
   print('This is not intended to be an inclusive list, nor is it supposed to be the end of your search.</header>')

def print_footer():
   """
      This section closes up our HTML neatly.
   """
   print('</div>')
   print('</body></html>')

def show_criteria(f, ffList, brList, diList,opList):
   """
      This section should show everything we can choose from.  As the choices are made,
      the page should update the Results.  If this proves to take too long, maybe shift to
      require a Submit button.

      In the Form Factor and Brand sections below, the lists will ultimately be generated by
      query, so they won't need to be hard-coded as they are now.
   """
   print('<criteria>')
   print('<form action="rigSelector.py" method="POST">')
   print('&nbsp;Form Factor:<br/>')
   for ff in ffList:
      tmp = '&nbsp;<input type="checkbox" name="' + ff[1] + '" '
      if f.getvalue(ff[1]):
         tmp += 'checked'
      tmp = tmp + '/> ' + ff[1]
      print(tmp)
   print('<br/><br/>')

   print('&nbsp;Brand:<br/>')
   for br in brList:
      tmp = '&nbsp;<input type="checkbox" name="' + br[1] + '" '
      if f.getvalue(br[1]):
         tmp += 'checked'
      tmp = tmp + '/> ' + br[1]
      print(tmp)
   print('<br/><br/>')

   print('&nbsp;Digital Mode:<br/>')
   for di in diList:
      tmp = '&nbsp;<input type="checkbox" name="' + di[1] + '" '
      if f.getvalue(di[1]):
         tmp += 'checked'
      tmp = tmp + '/> ' + di[1]
      print(tmp)
   print('<br/><br/>')

   print('&nbsp;Options:&nbsp;[not active]<br/>')
   for op in opList:
      tmp = '&nbsp;<input type="checkbox" name="' + op[1] + '" '
      if f.getvalue(op[1]):
         tmp += 'checked'
      tmp = tmp + '/> ' + op[1]
      print(tmp)
   print('<br/><br/>')

   # Until we can do this on-click...
   print('<br/><br/>')
   print('&nbsp;<input type="submit" value="Find my options!" />')
   # The Reset button only works until a Submission has been made.  After that....
   print('&nbsp;<input type=reset>')
   print('</form>')
   print('</criteria>')


def buildQuery(f, ffList, brList, diList, opList):
   """
      This should parse any selected options and build a query to work with.
   """
   formFactor = ""

   for ff in ffList:
      if f.getvalue(ff[1]):
         if len(formFactor) > 0:
            formFactor += ' OR '
         formFactor += "p.shape = '" + ff[1] + "'"

   brand = ""

   for br in brList:
      if f.getvalue(br[1]):
         if len(brand) > 0:
            brand += ' OR '
         brand += "b.brandName = '" + br[1] + "'"
   
   digital = ""
   
   for di in diList:
      if f.getvalue(di[1]):
         if len(digital) > 0:
            digital += ' OR '
         digital += "d.mode = '" + di[1] + "'"
   
   options = ""
   
   for op in opList:
      if f.getvalue(op[1]):
         if len(options) > 0:
            options += ' OR '
         options += "option = '" + op[1] + "'"

   
   q = "SELECT r.model, r.brand, p.shape, d.mode, r.msrp, r.vlink FROM rigs r, phyForm p, brand b, digMode d"
   q += " WHERE (r.shape = p.phyKey) AND (r.mode = d.digKey)"

   # If there are any criteria chosen, prepare to add to the query
   suffix = ""
   if len(formFactor) > 0:
      suffix += " AND (" + formFactor + ")"
   if len(brand) > 0:
      suffix += " AND (" + brand + ")"
   if len(digital) > 0:
      suffix += " AND (" + digital + ")"

   # Commented this part out for now, not sure how to work it in just yet.
   #if len(options) > 0:
   #   if len(suffix) > 0:
   #      suffix += " AND "
   #   suffix += "(" + options + ")"

   # Now add any details to the query
   q += suffix
   if DEBUGGING:
      print('*** Query as built: {}'.format(q))
   return q


def runQuery(q):
   """
      This is a generic function that takes the query, executes it, and returns the value set
   """

   # First, trap an errant DB failure:
   try:
      con = sqlite3.connect('rigSelector.sqlite3')
   except:
      print('CRITICAL: Could not connect to Database!')

   # Now we collect information based on the query.
   cur = con.cursor()
   cur.execute(q)
   qResult = cur.fetchall()

   # Now close the DB so we don't break anything.
   # We don't need commit() because this program SHOULD be read-only...
   if con:
      con.close()

   return qResult
 

def show_results(qry):
   """
      This section should show the results of the search, given the criteria.
   """

   result = runQuery(qry)
   resLen = len(result)

   # From this point, we need to make everything look pretty for the screen.
   print('<results>')
   print('&nbsp;Imagine a pretty nifty list of devices here with links and all that.<br/>&nbsp;Here is what we know based on our current database:<br/><br/>')
   if DEBUGGING:
      print('Query as received: {}\n'.format(qry))
      print('Result Length: {}\n'.format(resLen))
   if resLen > 0:
      print('<table><tr><th>Brand</th><th>Model</th><th>Form</th><th>Digital<br/>Modes</th><th>MSRP</th><th>Vendor</th></tr>')
      for rig in result:
         model, brand, form, mode, msrp, vlink = rig[0], rig[1], rig[2], rig[3], rig[4], rig[5]
         print(f"<tr><td>&nbsp;{brand}&nbsp;</td><td>&nbsp;{model}&nbsp;</td><td>&nbsp;{form}&nbsp;</td><td>&nbsp;{mode}&nbsp;</td><td>&nbsp;${msrp}&nbsp;</td><td>&nbsp;<a href='{vlink}'>Link</a>&nbsp;</td></tr>")
      print('</table>')
   else:
      print('<br/>There were no devices matching the criteria selected.')
   print('</results>')


"""
   Everything below here is the Main Routine.
"""
print_header()

form = cgi.FieldStorage()

fList = runQuery('SELECT * FROM phyForm')
dList = runQuery('SELECT * FROM digMode')
bList = runQuery('SELECT * FROM brand')
oList = runQuery('SELECT optKey, option FROM options WHERE rigndx = "0"')

show_criteria(form, fList, bList, dList, oList)

query = buildQuery(form, fList, bList, dList, oList)
show_results(query)

print_footer()

