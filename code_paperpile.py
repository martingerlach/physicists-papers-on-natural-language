#! /usr/bin/env python

# Written by GBdO (June 1, 2010). Licensed under GPL... :)

# How to run the program:
#
# python code.py physicist-language_mend.bib template.html > index.html
# python code_paperpile.py physicist-language_paperpile.bib template.html > index.html

#
# The html code will be printed to the standard output ( or to out.html ).

from datetime import date
import sys

def replacement(s):
    dictionary = {'\\"{a}': '&auml;', '\\"{A}': '&Auml;', '\\"{e}': '&euml;', 
    '\\"{E}': '&Euml;', '\\"{i}': '&iuml;', '\\"{I}': '&Iuml;', '\\"{o}': '&ouml;', 
    '\\"{O}': '&Ouml;', '\\"{u}': '&uuml;', '\\"{U}': '&Uuml;', "\\'{a}": '&aacute;',
    "\\'{A}": "&Aacute;", "\\'{e}": '&eacute;', "\\'{i}": '&iacute;', "\\'{\i}": '&iacute;',  
    "\\'{I}": '&Iacute;', "\\'{E}": '&Eacute;', "\\'{o}": '&oacute;', 
    "\\'{O}": '&Oacute;', "\\'{u}": '&uacute;', "\\'{U}": '&Uacute;',
    '\\~{n}': '&ntilde;','\\~{N}': '&Ntilde',  '\\~{a}': '&atilde;', 
    '\\~{A}': '&Atilde;', '\\~{o}': '&otilde;', '\\~{O}': '&Otilde;',
    "\\'{c}": '&#263;', "\\'{C}":'&#262;',
    "\\c{c}" :'&ccedil;',"\\c{C}" :'&Ccedil;',
    "\\'\\": '',  ' And ': ' and ',
    "\xe2\x80\x99" : "'",'\xe2\x80\x93':'-','\&':'&'} 
    #'\\~{N}': '&Ntilde;','{': '', '}': '',

    for k, v in dictionary.items():
#         print k,v
        s = s.replace(k, v)
    s.replace("\\","")
    return s
def cleanup_author(s):
    """Clean up and format author names.
    
    cleanup_author(str) -> str
    """

#     dictionary = {'\\"a': '&auml;', '\\"A': '&Auml;', '\\"e': '&euml;', 
#     '\\"E': '&Euml;', '\\"i': '&iuml;', '\\"I': '&Iuml;', '\\"o': '&ouml;', 
#     '\\"O': '&Ouml;', '\\"u': '&uuml;', '\\"U': '&Uuml;', "\\'a": '&aacute;',
#     "\\'A": '&Aacute;', "\\'e": '&eacute;', "\\'i": '&iacute;', 
#     "\\'I": '&Iacute;', "\\'E": '&Eacute;', "\\'o": '&oacute;', 
#     "\\'O": '&Oacute;', "\\'u": '&uacute;', "\\'U": '&Uacute;', 
#     '\\~n': '&ntilde;', '\\~N': '&Ntilde;', '\\~a': '&atilde;', 
#     '\\~A': '&Atilde;', '\\~o': '&otilde;', '\\~O': '&Otilde;', 
#     '.': ' ', "\\'\\": '', '{': '', '}': '', ' And ': ' and '}
    dictionary = {'\\"{a}': '&auml;', '\\"{A}': '&Auml;', '\\"{e}': '&euml;', 
    '\\"{E}': '&Euml;', '\\"{i}': '&iuml;', '\\"{I}': '&Iuml;', '\\"{o}': '&ouml;', 
    '\\"{O}': '&Ouml;', '\\"{u}': '&uuml;', '\\"{U}': '&Uuml;', "\\'{a}": '&aacute;',
    "\\'{A}": "&Aacute;", "\\'{e}": '&eacute;', "\\'{i}": '&iacute;', "\\'{\i}": '&iacute;',  
    "\\'{I}": '&Iacute;', "\\'{E}": '&Eacute;', "\\'{o}": '&oacute;', 
    "\\'{O}": '&Oacute;', "\\'{u}": '&uacute;', "\\'{U}": '&Uacute;',
    '\\~{n}': '&ntilde;','\\~{N}': '&Ntilde',  '\\~{a}': '&atilde;', 
    '\\~{A}': '&Atilde;', '\\~{o}': '&otilde;', '\\~{O}': '&Otilde;',
    "\\'{c}": '&#263;', "\\'{C}":'&#262;',
    "\\c{c}" :'&ccedil;',"\\c{C}" :'&Ccedil;',
    '.': ' ', "\\'\\": '',  ' And ': ' and ',
    "\xe2\x80\x99" : "'"}#','{': '', '}': '',

    dictionary_2 = {'{': '', '}': '',"\\":""}#second dict so that temp order

    for k, v in dictionary.items():
#         print k,v
        s = s.replace(k, v)
        
    for k, v in dictionary_2.items():
#         print k,v
        s = s.replace(k, v)
        

    names = s.split(' and ')
    s = ''
    for i in range(len(names)):
        sur, sep, fore = names[i].partition(',')
        fore_=''
        for n in fore.split(' '):
            try:
                if n[0]=='&':
                    fore_+= n[:n.index(';')]
                else:
                    fore_+= n[0].upper()
            except IndexError:
                pass
#         names[i] = fore+' '+sur
        name_ = fore_+' '+sur
        if i == 0:
            s += name_
        elif i < len(names) - 1:
            s += ', '+name_
        elif i==len(names)-1 and len(names)==2:
            s += ' and '+name_
        else:
            s += ', and '+name_
        
        
#     before, sep, after = s.rpartition(' and ')
#     before = before.replace(' and ', ', ')
#     s = before + sep + after

    return s


def cleanup_title(s):
    """Clean up and format article titles.

    cleanup_title(str) -> str
    """
#     s = s.replace("\xe2\x80\x99","'")
    s = s.lower()
    s = s.capitalize()

    return s


def cleanup_page(s):
    """Clean up the article page string.

    cleanup_pages(str) -> str
    """

    s = s.replace('--', '-')

    return s



# # Get the BibTeX and template file names.
# bibfile = 'physicist-language_mend.bib'#sys.argv[1]
# templatefile = 'template_02.html'#sys.argv[2]
bibfile = sys.argv[1]
templatefile = sys.argv[2]


# Open, read and close the files.
with open(templatefile, 'r') as f:
    template = f.read()

with open(bibfile, 'r') as f:
    datalist = f.readlines()


# Discard unwanted characteres and commented lines.
datalist = [s.strip(' \n\t') for s in datalist]
datalist = [s for s in datalist if s[:2] != '%%']


# Convert a list into a string.
data = ''
for s in datalist: data += s


# Split the data at the separators @ and put it in a list.
# biblist = data.split('@')
# bugfix for mendeley since in abstract there is sometimes the mailadress
# all other wanted seperators than article should be included in split_list
# split_list = ["@inproceedings","@incollection","@book"] # except article
split_list = ["@INPROCEEDINGS","@INCOLLECTION","@INBOOK"] # except article

for splitter in split_list:
    data_tmp=''
    data_split = data.split(splitter)
    for i in range(len(data_split)):
        if i == 0:
            data_tmp = data_split[0]
        else:
            data_tmp += '@ARTICLE'+data_split[i]
    data = data_tmp

biblist = data.split('@ARTICLE')
# Discard empty strings from the list.
biblist = ['article'+s for s in biblist if s != '']

# Create a list of lists containing the strings "key = value" of each bibitem.
listlist = []



list_fields1 = ['author', 'title','journal',  'pages',  'url', 'doi','arxivid']
list_fields2 = ['year','volume'] ## without quotes
for s in biblist:
    if len(s.split('}@'))>1:
        s = s.split('}@')[0] + '}'

    type, sep, s = s.partition('{')
    id, sep, s = s.partition(',')
    s = s.rpartition('}')[0]

    keylist = ['type = ' + type.lower(), 'id = ' + id]

    s = s + ","
    s = s.replace('booktitle','journal') ## for @Inproceedings

    for field in list_fields1:
        h = s.split("%s = \""%(field))
        field_val = h[-1].split("\",")[0]
        
        if len(h)>1:
            p = "%s = %s"%(field,field_val)
            keylist.append(replacement(p))

    for field in list_fields2:
        h = s.split("%s =  "%(field))
        field_val = h[-1].split(",")[0]
        if len(h)>1:
            p = "%s = %s"%(field,field_val)
            keylist.append(replacement(p))

    keylist = [t.strip(' ,\t\n') for t in keylist]
    listlist.append(keylist)

# Create a list of dicts containing key : value of each bibitem.
dictlist = []
for l in listlist:
    keydict = {}
    for s in l:
        key, sep, value = s.partition('=')
        key = key.strip(' ,\n\t{}')
        key = key.lower()
        value = value.strip(' ,\n\t{}')
        keydict[key] = value

    dictlist.append(keydict)

# Backup all the original data.
full_dictlist = dictlist


# Keep only articles in the list.
dictlist = [d for d in dictlist if d['type'] == 'article']
# keep only articles that have author and title.
dictlist = [d for d in dictlist if 'author' in d and 'title' in d]
dictlist = [d for d in dictlist if d['author'] != '' and d['title'] != '']

# Get a list of the article years and the min and max values.
years = [int(d['year']) for d in dictlist if 'year' in d]
years.sort()
older = years[0]
newer = years[-1]


###########################################################################
# Set the fields to be exported to html (following this order).
mandatory = ['author', 'title']
optional = ['journal', 'volume', 'pages', 'year', 'url', 'doi','arxivid']
###########################################################################

# Clean up data.
for i in range(len(dictlist)):
    dictlist[i]['author'] = cleanup_author(dictlist[i]['author'])
    dictlist[i]['title'] = cleanup_title(dictlist[i]['title'])

 # Write down the list html code.
counter = 0
html = ''
for y in reversed(range(older, newer + 1)):
    if y in years:
        html += '<h3 id="y{0}">{0}</h3>\n\n\n<ul>\n'.format(y)
        for d in dictlist:
            if 'year' in d and int(d['year']) == y:
                mandata = [d[key] for key in mandatory]
                html += '<li>{0}, <i>{1}</i>'.format(*mandata)

                for t in optional:
                    # journal
                    if t=='journal':
                        # no journal supplied
                        if t not in d:
                            # see if there is an arxivId
                            try:
                                html += ', {0}'.format('arXiv:'+d['arxivid']) 
                            except KeyError:
                                pass
                        elif 'arxiv' in d[t].lower():
                            try:
                                html += ', {0}'.format('arXiv:'+d['arxivid'])
                            except KeyError:
                                pass
                        else:
                            html += ', {0}'.format(d[t])
                            
                    if t in d:
#                         if t == 'journal': html += ', {0}'.format(d[t])
#                         if t == 'eprint': html += ':{0}'.format(d[t])
                        if t == 'volume': html += ' <b>{0}</b>'.format(d[t])
                        if t == 'pages': 
                            a = cleanup_page(d[t])
                            html += ', {0}'.format(a)
                        if t == 'year': html += ', {0}'.format(d[t])
                        if t == 'url':
                            # if there are more than one url
                            url_temp = d[t].split(' ')  
                            url = ''
                            for j,url_ in enumerate(url_temp):
                                if 'arxiv' not in url_.lower():
                                    url = url_
                            if url != '':
                                html += ' <a href="{0}">[html]</a>'.format(url.replace('\\',''))
#                             print url
#                                     print j,url_
#                                     break
#                             print ''
                                    
                        if t == 'doi': 
                            html += ' <a href="'+'http://dx.doi.org/'+'{0}">[doi]</a>'.format(d[t])
                        if t=='arxivid':
                            html += ' <a href="'+'http://arxiv.org/abs/'+'{0}">[arXiv]</a>'.format(d[t])


                html += '</li>\n'
                counter += 1

        html += '</ul>\n'


# Fill up the empty fields in the template.
a, mark, b = template.partition('<!--LIST_GOES_HERE-->')
a = a.replace('<!--NUM_OF_ARTICLES-->', str(counter), 1)
a = a.replace('<!--NEWER-->', str(newer), 1)
a = a.replace('<!--OLDER-->', str(older), 1)
now = date.today()
a = a.replace('<!--DATE-->', date.today().strftime('%d %b %Y'))


# Join the header, list and footer html code.
final = a + html + b


# Print the final result to the standard output.
print(final)
