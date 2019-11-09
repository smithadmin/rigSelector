#!/usr/local/bin/python3.6

"""
    Author: William Smith

   This is a work in progress.
"""

import cgi
import cgitb; cgitb.enable()

def print_header():
   """
      This section prints everything for the Header, up to (and including) the Header class.
   """
   print('Content-Type: text/html')
   print('')
   print('<html><head><title>rigSelector</title><link rel="stylesheet" href="split2.css"></head><body>')
   print('<div class="wrapper">')
   print('<h1>rigSelector (demo)</h1>')
   print('<header>Let\'s see what we can do to help you on your search for your next rig!</header>')

def print_footer():
   """
      This section closes up our HTML neatly.
   """
   print('</div>')
   print('</body></html>')

def show_criteria(f):
   """
      This section should show everything we can choose from.  As the choices are made,
      the page should update the Results.  If this proves to take too long, maybe shift to
      require a Submit button.

      In the Form Factor and Brand sections below, the lists will ultimately be generated by
      query, so they won't need to be hard-coded as they are now.
   """
   print('<criteria>')
   print('<form action="rigSelectorDemo.py" method="POST">')
   print('Form Factor:<br/>')
   for ff in ['HT', 'Mobile', 'Base']:
      tmp = '<input type="checkbox" name="' + ff + '" '
      if f.getvalue(ff):
         tmp += 'checked'
      tmp = tmp + '/> ' + ff
      print(tmp)
   print('<br/><br/>')

   print('Brand:<br/>')
   for br in ['Anytone', 'Icom', 'Kenwood', 'Yaesu']:
      tmp = '<input type="checkbox" name="' + br + '" '
      if f.getvalue(br):
         tmp += 'checked'
      tmp = tmp + '/> ' + br
      print(tmp)
   print('<br/><br/>')

   print('Digital Mode:<br/>')
   for br in ['DMR', 'DStar', 'YSF']:
      tmp = '<input type="checkbox" name="' + br + '" '
      if f.getvalue(br):
         tmp += 'checked'
      tmp = tmp + '/> ' + br
      print(tmp)
   print('<br/><br/>')

   # Until we can do this on-click...
   print('<br/><br/>')
   print('<input type="submit" value="Find my options!" />')
   print('</form>')
   print('</criteria>')


def buildQuery(f):
   """
      This should parse any selected options and build a query to work with.
   """
   formFactor = ""
   ffList = ['HT', 'Mobile', 'Base']
   for ff in ffList:
      if f.getvalue(ff):
         if len(formFactor) > 0:
            formFactor += ' OR '
         formFactor += "form = '" + ff + "'"

   brand = ""
   brList = ['Anytone', 'Icom', 'Kenwood', 'Yaesu']
   for br in brList:
      if f.getvalue(br):
         if len(brand) > 0:
            brand += ' OR '
         brand += "brand = '" + br + "'"
   
   digital = ""
   diList = ['DMR', 'DStar', 'YSF']
   for di in diList:
      if f.getvalue(di):
         if len(digital) > 0:
            digital += ' OR '
         digital += "digital = '" + di + "'"
   
   q = "SELECT * from database"
   if (len(formFactor) > 0) or (len(brand) > 0):
      q += " WHERE "
   if len(formFactor) > 0:
      q += "(" + formFactor + ")"
   if len(brand) > 0:
      if len(formFactor) > 0:
         q += " AND "
      q += "(" + brand + ")"
   if len(digital) > 0:
      if (len(formFactor) > 0) or (len(brand) > 0):
         q += " AND "
      q += "(" + digital + ")"

   return q


def show_results(q):
   """
      This section should show the results of the search, given the criteria.
   """
   print('<results>')
   print('Imagine a pretty nifty list of devices here with links and all that.<br/><br/>')
   print('Query: {}<br/>Length: {}'.format(q, len(q)))
   print('</results>')

"""
   Everything below here is the Main Routine.
"""
print_header()

form = cgi.FieldStorage()

show_criteria(form)

query = buildQuery(form)

show_results(query)

print_footer()
