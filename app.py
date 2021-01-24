from flask import Flask, url_for, request, render_template, session, redirect
app = Flask(__name__)
# app.jinja_options['extensions'].append('jinja2.ext.do')
app.jinja_env.add_extension('jinja2.ext.do')

app.secret_key = b'\x17\xef\xa3]\xfd\xc9\x18\x061\x1b\xb2\x92e$\xa5\x9a\xdd\xd1\xa6\x0eB|\xcc\xc9\x86l \xf6i\x0c\x9b '

@app.route('/comingsoon')
def comingsoon():
    return render_template('comingsoon.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def landing_page():
    # clear sessions and local storage
    session.clear()
    return render_template('landing_page.html')

@app.route('/dialogue')
def dialogue():
    # initialize inventory items
    session['purple_key'] = False
    session['potion'] = False
    session['red_key'] = False
    session['spell_book'] = False
    session['infinity_stone'] = False
    session['page4_medium'] = False
    session['page6_easy'] = False
    session['page10_easy'] = False
    session['page13_medium'] = False
    return render_template('dialogue.html')
   
@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/update/<item>')
def update(item):
    page = 'page_1'
    if item == 'purple_key':
        session['purple_key'] = True
        page = 'page_3'
    elif item == 'potion_guard':
        session['potion_guard'] = True
        page = 'page_8'
    elif item == 'potion':
        session['potion'] = True
        page = 'page_8'
    elif item == 'red_key':
        session['red_key'] = True
        page = 'page_17'
    elif item == 'spell_book':
        session['spell_book'] = True
        page = 'page_5'
    elif item == 'infinity_stone':
        session['infinity_stone'] = True
        page = 'page_15'
    elif item == 'family_guard':
        session['family_guard'] = True
        page = 'page_18'
    elif item == 'page4_medium':
        session['page4_medium'] = True
        page = 'page_4'
    elif item == 'page6_easy':
        session['page6_easy'] = True
        page = 'page_6'
    elif item == 'page10_easy':
        session['page10_easy'] = True
        page = 'page_10'
    elif item == 'page13_medium':
        session['page13_medium'] = True
        page = 'page_13'
    return redirect(url_for(page, feedback='You got a new item!'))  # feedback statement not exactly used, can change to something other than None

@app.route('/1')
def page_1():
    return render_template('1.html')

@app.route('/2')
def page_2():
    return render_template('2.html')

@app.route('/3/<feedback>')
def page_3(feedback):
    if feedback != 'None':
        return render_template('3_purplekey.html', feedback=feedback)
    else: 
        return render_template('3_purplekey.html', feedback='None')

@app.route('/4/<feedback>/')
@app.route('/4/<feedback>/<prevpage>')
def page_4(feedback, prevpage=None):
    if feedback != 'None':
        return render_template('4_medium.html', feedback=feedback, prevpage=prevpage)
    else: 
        return render_template('4_medium.html', feedback='None', prevpage=prevpage)

@app.route('/5/<feedback>')
def page_5(feedback):
    if feedback != 'None':
        return render_template('5_spellbook.html', feedback=feedback)
    else: 
        return render_template('5_spellbook.html', feedback='None')

@app.route('/6/<feedback>/')
@app.route('/6/<feedback>/<prevpage>')
def page_6(feedback, prevpage=None):
    if feedback != 'None':
        return render_template('6_easy.html', feedback=feedback, prevpage=prevpage)
    else: 
        return render_template('6_easy.html', feedback='None', prevpage=prevpage)

@app.route('/7')
def page_7():
    return render_template('7.html')

@app.route('/8/<feedback>')
def page_8(feedback):
    if feedback != 'None':
        return render_template('8_purplechest.html', feedback=feedback)
    else: 
        return render_template('8_purplechest.html', feedback='None')

@app.route('/9/<prevpage>')
def page_9(prevpage):
    return render_template('9_potionguard.html', prevpage=prevpage)

@app.route('/10/<feedback>/')
@app.route('/10/<feedback>/<prevpage>')
def page_10(feedback, prevpage=None):
    if feedback != 'None':
        return render_template('10_easy.html', feedback=feedback, prevpage=prevpage)
    else: 
        return render_template('10_easy.html', feedback='None', prevpage=prevpage)

@app.route('/11')
def page_11():
    return render_template('11.html')

@app.route('/12')
def page_12():
    return render_template('12_wiseman.html')

@app.route('/13/<feedback>/')
@app.route('/13/<feedback>/<prevpage>')
def page_13(feedback, prevpage=None):
    if feedback != 'None':
        return render_template('13_medium.html', feedback=feedback, prevpage=prevpage)
    else: 
        return render_template('13_medium.html', feedback='None', prevpage=prevpage)

@app.route('/14/<prevpage>')
def page_14(prevpage):
    return render_template('14_keydoor.html', prevpage=prevpage)

@app.route('/15/<feedback>')
def page_15(feedback):
    if feedback != 'None':
        return render_template('15_infinitystone.html', feedback=feedback)
    else: 
        return render_template('15_infinitystone.html', feedback='None')

@app.route('/16')
def page_16():
    return render_template('16.html')

@app.route('/17/<feedback>')
def page_17(feedback):
    if feedback != 'None':
        return render_template('17_keymedium.html', feedback=feedback)
    else: 
        return render_template('17_keymedium.html', feedback='None')

@app.route('/18')
def page_18():
    return render_template('18_bossdragon.html')

@app.route('/end')
def endscreen():
    return render_template('endscreen.html')
