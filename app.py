"""Flask Stack Simulator starter: complete TODOs during the live demo.
Before class, preview templates/index.html directly in the browser.
Running this file starts a status page, not the completed simulator.
"""
import os
import secrets
from flask import Flask, render_template, request, redirect, url_for, session, flash
from stack_model import Stack

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)

@app.route('/')
def index():
    raw_items = session.get('items', [])
    stack = Stack(list(raw_items))
    display_items = list(reversed(stack.items))
    pop_history = session.get('pop', [])
    highlight = request.args.get('pick') == '1'
    
    return render_template(
        'index.html',
        items=display_items,
        size=stack.size(),
        pop=pop_history,
        highlight=highlight
    )

@app.route('/operate', methods=['POST'])
def operate():
    action = request.form.get('action')
    value = request.form.get('value', '').strip()
    
    raw_items = session.get('items', [])
    stack = Stack(list(raw_items))
    pop_history = session.get('pop', [])
    highlight = False

    if action == 'push':
        if not value or len(value) > 24:
            flash('Enter 1 to 24 characters.', 'error')
        elif stack.size() >= 20:
            flash('Stack limit reached (max 20 items).', 'error')
        else:
            stack.push(value)
            flash(f"Pushed '{value}' to top of stack.", 'success')

    elif action == 'pop':
        removed = stack.pop()
        if removed is None:
            flash('Stack is empty. Cannot pop.', 'error')
        else:
            pop_history.insert(0, removed)
            flash(f"Popped '{removed}' from stack.", 'success')

    elif action == 'peek':
        top_item = stack.peek()
        if top_item is None:
            flash('Stack is empty. Cannot peek.', 'error')
        else:
            flash(f"Top item is '{top_item}'.", 'success')
            highlight = True

    elif action == 'clear':
        stack.clear()
        pop_history = []
        flash('Stack and deleted history cleared.', 'success')

    session['items'] = stack.items
    session['pop'] = pop_history

    if highlight:
        return redirect(url_for('index', pick=1))
    return redirect(url_for('index'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)