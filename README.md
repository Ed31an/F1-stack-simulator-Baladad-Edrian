@"
# Flask Stack Simulator

## Student Information
- **Name:** Edrian C. Baladad
- **Course & Section:** BSIT / ELEC 4 - Python Programming
- **Student ID:** 23-BGU-0293
- **Instructor:** Mr. Jackson S. Soriano, MIT

---

## Activity Description
Starter repository for the **Flask Stack Simulator** pre-demonstration activity. This project demonstrates how Python backend logic (LIFO Stack data structure) connects to a web frontend built with Flask, Jinja, HTML, CSS, Bootstrap, JavaScript, and jQuery.

- **Original Starter Repository:** [Jackson-Soriano/f1-elec4-stack-simulator-starter](https://github.com/Jackson-Soriano/f1-elec4-stack-simulator-starter.git)

---

## Starter File Overview
- `app.py`: Flask routing (`/` and `/stack`) and request processing.
- `stack_model.py`: Python `Stack` class implementing LIFO operations (`push`, `pop`, `peek`, `size`, `clear`).
- `templates/`: HTML templates (`base.html`, `index.html`, `contact.html`).
- `static/`: Custom CSS styling (`style.css`) and client-side scripts (`ui.js`).



-----------------------------
## 📌 Project Overview

This repository contains two standalone interactive web simulators:
1. **Stack Simulator (LIFO - Last-In, First-Out)**: Visualizes stack operations where elements added last are processed first.
2. **Queue Simulator (FIFO - First-In, First-Out)**: Visualizes queue operations where elements are processed strictly in the order of their arrival.

---

## 🚀 Features & Functionality

### Part I: Stack Simulator (Port 5000)
- **Push (Top)**: Adds an element onto the top of the stack.
- **Pop (Top)**: Removes and displays the top element into the *Deleted Stack Data* area.
- **Peek (Top)**: Highlights the current top element without mutating the stack.
- **Clear**: Empties the stack and clears deleted history.
- **Validation**: Enforces capacity limits and input length constraints.

### Part II: Queue Simulator (Port 5001)
- **Enqueue (Rear)**: Appends an element to the rear of the queue.
- **Dequeue (Front)**: Removes the oldest element from the front into the *Dequeued Items* area.
- **Peek (Front)**: Highlights the current front element in yellow without mutating the queue.
- **Clear**: Resets the queue and dequeued item log.
- **Validation**: Restricts input length (1–24 characters) and max capacity (20 items).
---

## Local Setup Instructions
1. Clone this repository:
   ```bash
   git clone [https://github.com/Ed31an/F1-stack-simulator-Baladad-Edrian.git](https://github.com/Ed31an/F1-stack-simulator-Baladad-Edrian.git)