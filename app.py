from flask import Flask, render_template, request
import random

app = Flask(__name__)

quotes = [
    "Distraction is the enemy of focus.",
    "Stay focused, stay strong.",
    "Small distractions lead to big regrets.",
    "The cost of distraction is the life you could have lived.",
    "Where focus goes, energy flows.",
    "Discipline is choosing between what you want now and what you want most.",
    "You become what you focus on.",
    "Success demands single-minded focus.",
    "Your future is created by what you do today, not tomorrow.",
    "Cut off distractions. Connect to your vision."
]
@app.route('/history')
def view_history():
    return "<h2>History feature coming soon!</h2><p>We'll record your distractions here later.</p>"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        distraction = request.form.get('distraction', '')
        duration = request.form.get('duration', '0')
        unit = request.form.get('unit', 'minutes')
        reason = request.form.get('reason', '')

        try:
            duration = float(duration)
        except ValueError:
            duration = 0

        if unit == 'days':
            duration_in_minutes = duration * 24 * 60
        else:
            duration_in_minutes = duration

        cost_per_minute = 7
        total_cost = duration_in_minutes * cost_per_minute

        quote = random.choice(quotes)  # Randomly select one quote

        return render_template('result.html',
                               distraction=distraction,
                               duration=duration,
                               unit=unit,
                               reason=reason,
                               minutes=duration_in_minutes,
                               cost=total_cost,
                               quote=quote)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)