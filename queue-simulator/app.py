import os
import secrets
from flask import Flask, render_template, request, redirect, url_for, session, flash
from queue_model import Queue

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)

@app.route('/')
def index():
    raw_items = session.get('queue_items', [])
    queue = Queue(list(raw_items))
    dequeued_history = session.get('dequeued', [])
    highlight = request.args.get('pick') == '1'
    
    return render_template(
        'index.html',
        items=queue.items,
        size=queue.size(),
        dequeued=dequeued_history,
        highlight=highlight
    )

@app.route('/operate', methods=['POST'])
def operate():
    action = request.form.get('action')
    value = request.form.get('value', '').strip()
    
    raw_items = session.get('queue_items', [])
    queue = Queue(list(raw_items))
    dequeued_history = session.get('dequeued', [])
    highlight = False

    if action == 'enqueue':
        if not value or len(value) > 24:
            flash('Enter 1 to 24 characters.', 'error')
        elif queue.size() >= 20:
            flash('Queue limit reached (max 20 items).', 'error')
        else:
            queue.enqueue(value)
            flash(f"Enqueued '{value}' to the rear.", 'success')

    elif action == 'dequeue':
        removed = queue.dequeue()
        if removed is None:
            flash('Queue is empty. Cannot dequeue.', 'error')
        else:
            dequeued_history.insert(0, removed)
            flash(f"Dequeued '{removed}' from the front.", 'success')

    elif action == 'peek':
        front_item = queue.peek()
        if front_item is None:
            flash('Queue is empty. Cannot peek.', 'error')
        else:
            flash(f"Front item is '{front_item}'.", 'success')
            highlight = True

    elif action == 'clear':
        queue.clear()
        dequeued_history = []
        flash('Queue and dequeued history cleared.', 'success')

    else:
        flash('Unknown operation.', 'error')

    session['queue_items'] = queue.items
    session['dequeued'] = dequeued_history

    if highlight:
        return redirect(url_for('index', pick=1))
    return redirect(url_for('index'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)