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

# Static variables, defined here for convenience
OUTFILE = "newRigs.sql"

def print_header():
   """
      This section prints everything for the Header, up to (and including) the Header class.
   """
   print('Content-Type: text/html')
   print('')
   print('<html><head><title>rigSelector New Rig Entry</title></head><body>')
   print('<h1>rigSelector New Rig Entry</h1>')
   print('&nbsp;Here we are, ready to add a new Radio to the database!<br/>')

def print_footer():
   """
      This section closes up our HTML neatly.
   """
   print('</body></html>')

def show_form(f, ffList, brList, diList,opList):
   """
      This section should show everything we can choose from.  The results should be written
      to the file OUTFILE.
   """
   print('<form action="rigEntry.py" method="POST">')

   print('<div>')
   print('<label for="rigBrand">Brand: </label>')
   # Input here, but change to dropdown/text for other later.  Reference brList
   print('<input type="text" id="rigBrand" name="rigBrand" />')
   print('</div>')

   print('<div>')
   print('<label for="rigModel">Model: </label>')
   # Input here, but change to dropdown/text for other later.  Reference brList
   print('<input type="text" id="rigModel" name="rigModel" />')
   print('</div>')

   print('&nbsp;Form Factor:<br/>')
   for ff in ffList:
      tmp = '&nbsp;<input type="radio" name="rigForm" id="' + ff[1] + '" value="' + ff[1] + '" />'
      tmp = tmp + '<label for="' + ff[1] + '">' + ff[1] + '</label><br/>'
      print(tmp)
   print('<br/><br/>')

   print('&nbsp;Digital Mode:<br/>')
   for di in diList:
      tmp = '&nbsp;<input type="radio" name="rigDigi" id="' + di[1] + '" value=' + di[1] + '" />'
      tmp = tmp + '<label for="' + di[1] + '">' + di[1] + '</label><br/>'
      print(tmp)
   print('<br/><br/>')

   print('&nbsp;Options:<br/>')
   for op in opList:
      opName = 'option' + str(opList.index(op))  # option0 ..optionN
      tmp = '&nbsp;<input type="checkbox" name="' + opName + '" id="' + opName + '" value="' + op[1] + '" />'
      tmp = tmp + '<label for="' + opName + '">' + op[1] + '</label><br/>'
      print(tmp)
   print('<br/><br/>')

   # Until we can do this on-click...
   print('<br/><br/>')
   print('<input type="hidden" id="rigEntry" name="rigEntry" value="424242">')
   print('&nbsp;<input type="submit" value="Add this radio!" />')
   # The Reset button only works until a Submission has been made.  After that....
   print('&nbsp;<input type=reset>')
   print('</form>')


def saveQuery(f, opList):
   """
      This should build the query and write it to OUTFILE
   """
   formFactor = ""

   # we have option0 through optionN, depending on length of opList
   # This part here is legacy; re-write it
   for op in opList:
      if f.getvalue(op[1]):
         if len(options) > 0:
            options += ' OR '
         options += "option = '" + op[1] + "'"
         

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
 


"""
   Everything below here is the Main Routine.
"""
print_header()

form = cgi.FieldStorage()

# Do this here because we need the info if this is a submission of a new radio
oList = runQuery('SELECT * FROM options WHERE rigndx = "0"')  # This way, no repeats

if form.getvalue(rigEntry) == "424242"
   # write values out to OUTFILE
   saveQuery(form, oList)
   

fList = runQuery('SELECT * FROM phyForm')
dList = runQuery('SELECT * FROM digMode')
bList = runQuery('SELECT * FROM brand')

show_form(form, fList, bList, dList, oList)

print_footer()

