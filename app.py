from flask import Flask, render_template, request
import hashlib
import json

app = Flask(__name__)

# Fichier JSON pour stocker les résultats
DATA_FILE = '/data/results.json'

# Liste des algorithmes de hachage disponibles
HASH_ALGORITHMS = ['sha256', 'sha1', 'md5', 'sha384', 'sha512']

# Fonction pour charger les résultats depuis le fichier JSON
def load_results():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Fonction pour sauvegarder les résultats dans le fichier JSON
def save_results(results):
    with open(DATA_FILE, 'w') as file:
        json.dump(results, file, indent=4)

# Charger les résultats existants au démarrage
results = load_results()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérer la chaîne de caractères saisie par l'utilisateur
        input_str = request.form['input_str']

        # Récupérer l'algorithme choisi par l'utilisateur
        selected_algorithm = request.form.get('algorithm', 'sha256')

        # Calculer le checksum en utilisant l'algorithme sélectionné
        hash_value = hashlib.new(selected_algorithm, input_str.encode()).hexdigest()

        # Ajouter le résultat à la liste
        result = {
            'input': input_str,
            'algorithm': selected_algorithm,
            'hash': hash_value
        }
        results.append(result)

        # Sauvegarder les résultats dans le fichier JSON
        save_results(results)

    return render_template('index.html', results=results, algorithms=HASH_ALGORITHMS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

