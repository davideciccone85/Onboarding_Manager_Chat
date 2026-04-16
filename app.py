```python
# Baustein 1 & 3: Das "Gehirn" & Die "Brücke" - Kombinierte Backend-Logik
# Dieser Code simuliert einen Webserver, der Anfragen vom Frontend entgegennimmt
# und den Gesprächsfluss des Onboarding Managers steuert.

import random
import json

# --- Persistenter Speicher (Simulation) ---
# In einer echten Anwendung wäre dies eine Datenbank (z.B. SQLite, PostgreSQL)
# oder ein Dateisystem auf dem Server.
# Wir verwenden ein einfaches Dictionary, um den Zustand zwischen den Aufrufen zu speichern.
USER_SESSIONS = {}

def handle_chat_request(request_data):
    """
    Dies ist die zentrale Funktion, die jede Anfrage vom Frontend verarbeitet.
    Sie entspricht einem API-Endpunkt wie /api/chat.
    
    Args:
        request_data (dict): Die JSON-Daten, die vom Frontend gesendet wurden.
                             Erwartet {"user_code": string|from flask import Flask, request, jsonify
import random
import json

# Erstellen der Flask-Server-Anwendung
app = Flask(__name__)

# --- Persistenter Speicher (Simulation) ---
USER_SESSIONS = {}

# --- Konfiguration der Lerninhalte ---
LERN_NUGGETS = {
    1: {"titel": "Grundlagen: Unsere Unternehmenswerte", "typ": "video", "link": "https://onedrive.live.com/link_zu_video_1"},
    2: {"titel": "Fahrrad-Leasing: Die Basics", "typ": "video", "link": "https://onedrive.live.com/link_zu_video_2"},
}

# --- Frontend Auslieferung ---
# Der HTML-Code unseres Frontends wird hier direkt eingefügt.
@app.route('/')
def serve_frontend():
    return '''
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FXXL Akademie - Onboarding Manager</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-red: #D32D3A;
            --text-dark: #4A4A4A;
            --background-light: #f4f4f4;
            --background-white: #ffffff;
            --border-color: #e0e0e0;
        }
        body {
            font-family: 'Open Sans', Arial, Helvetica, sans-serif;
            background-color: var(--background-light);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        #chat-container {
            width: 100%;
            max-width: 600px;
            height: 90vh;
            max-height: 800px;
            display: flex;
            flex-direction: column;
            background-color: var(--background-white);
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }
        header {
            background-color: var(--primary-red);
            color: var(--background-white);
            padding: 20px 15px;
            text-align: center;
            flex-shrink: 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        header h1 {
            margin: 0;
            font-size: 24px;
            font-weight: 700;
        }
        header p {
            margin: 5px 0 0;
            font-size: 14px;
            font-weight: 400;
            opacity: 0.9;
        }
        #chat-window {
            flex-grow: 1;
            padding: 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
        }
        .message {
            max-width: 75%;
            padding: 10px 15px;
            border-radius: 18px;
            margin-bottom: 10px;
            line-height: 1.4;
            opacity: 0;
            transform: translateY(10px);
            animation: fadeIn 0.3s forwards;
        }
        @keyframes fadeIn {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .bot-message {
            background-color: #eef2f6;
            color: var(--text-dark);
            align-self: flex-start;
            border-bottom-left-radius: 4px;
        }
        .user-message {
            background-color: var(--primary-red);
            color: var(--background-white);
            align-self: flex-end;
            border-bottom-right-radius: 4px;
        }
        #input-area {
            display: flex;
            padding: 15px;
            border-top: 1px solid var(--border-color);
            flex-shrink: 0;
        }
        #message-input {
            flex-grow: 1;
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 10px 15px;
            font-size: 16px;
            margin-right: 10px;
            outline: none;
        }
        #message-input:focus {
            border-color: var(--primary-red);
        }
        #send-button {
            background-color: var(--primary-red);
            color: white;
            border: none;
            border-radius: 50%;
            width: 44px;
            height: 44px;
            font-size: 20px;
            cursor: pointer;
            transition: background-color 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        #send-button:hover {
            background-color: #a9242f; /* Darker red */
        }
        .typing-indicator {
            display: flex;
            align-items: center;
            padding: 10px 15px;
        }
        .typing-indicator span {
            height: 8px;
            width: 8px;
            background-color: #c1c1c1;
            border-radius: 50%;
            display: inline-block;
            margin: 0 2px;
            animation: bounce 1.2s infinite;
        }
        .typing-indicator span:nth-of-type(2) {
            animation-delay: 0.2s;
        }
        .typing-indicator span:nth-of-type(3) {
            animation-delay: 0.4s;
        }
        @keyframes bounce {
            0%, 60%, 100% {
                transform: translateY(0);
            }
            30% {
                transform: translateY(-6px);
            }
        }
    </style>
</head>
<body>
    <div id="chat-container">
        <header>
            <h1>Fahrrad XXL Akademie</h1>
            <p>Gemeinsam. Weiter. Bilden.</p>
        </header>
        <div id="chat-window">
        </div>
        <div id="input-area">
            <input type="text" id="message-input" placeholder="Schreibe eine Antwort...">
            <button id="send-button" title="Senden">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
        </div>
    </div>
    <script>
        const chatWindow = document.getElementById('chat-window');
        const input = document.getElementById('message-input');
        const sendButton = document.getElementById('send-button');
        let userCode = null;
        function addMessage(text, type) {
            const messageElement = document.createElement('div');
            messageElement.classList.add('message', `${type}-message`);
            messageElement.textContent = text;
            chatWindow.appendChild(messageElement);
            chatWindow.scrollTop = chatWindow.scrollHeight;
        }
        function showTypingIndicator() {
            const indicator = document.createElement('div');
            indicator.id = 'typing';
            indicator.classList.add('typing-indicator');
            indicator.innerHTML = '<span></span><span></span><span></span>';
            chatWindow.appendChild(indicator);
            chatWindow.scrollTop = chatWindow.scrollHeight;
        }
        function removeTypingIndicator() {
            const indicator = document.getElementById('typing');
            if (indicator) {
                indicator.remove();
            }
        }
        async function sendMessageToBackend(messageText) {
            input.disabled = true;
            sendButton.disabled = true;
            showTypingIndicator();
            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        user_code: userCode,
                        message: messageText
                    }),
                });
                if (!response.ok) {
                    throw new Error('Netzwerk-Antwort war nicht in Ordnung.');
                }
                const data = await response.json();
                removeTypingIndicator();
                if (data.user_code) {
                    userCode = data.user_code;
                }
                for (const botMessage of data.responses) {
                    addMessage(botMessage, 'bot');
                    await new Promise(resolve => setTimeout(resolve, 800));
                }
            } catch (error) {
                removeTypingIndicator();
                addMessage('Entschuldigung, es ist ein technischer Fehler aufgetreten. Bitte versuchen Sie es später erneut.', 'bot');
                console.error('Fehler bei der Kommunikation mit dem Backend:', error);
            }
            input.disabled = false;
            sendButton.disabled = false;
            input.focus();
        }
        function handleUserInput() {
            const text = input.value.trim();
            if (!text) return;
            addMessage(text, 'user');
            input.value = '';
            sendMessageToBackend(text);
        }
        sendButton.addEventListener('click', handleUserInput);
        input.addEventListener('keydown', (event) => {
            if (event.key === 'Enter') {
                handleUserInput();
            }
        });
        window.onload = () => {
            sendMessageToBackend(null);
        };
    </script>
</body>
</html>
'''

# --- Chat-Logik (Das "Gehirn") ---
@app.route('/api/chat', methods=['POST'])
def handle_chat_request():
    request_data = request.get_json()
    user_code = request_data.get('user_code')
    user_message = request_data.get('message')

    if user_code and user_code in USER_SESSIONS:
        session = USER_SESSIONS[user_code]
    else:
        new_code = f"FXXL-{random.randint(1000, 9999)}"
        session = {
            "user_code": new_code,
            "state": "NEU",
            "user_data": {},
            "current_nugget": 1
        }
        USER_SESSIONS[new_code] = session

    response_data = {
        "user_code": session["user_code"],
        "responses": []
    }

    if session["state"] == "NEU":
        response_data["responses"].append("Hallo! Ich bin dein persönlicher Onboarding Manager.")
        response_data["responses"].append("Wie lautet dein Vorname?")
        session["state"] = "ERWARTE_NAME"

    elif session["state"] == "ERWARTE_NAME":
        session["user_data"]["vorname"] = user_message
        response_data["responses"].append(f"Danke, {user_message}! In welcher Filiale arbeitest du?")
        session["state"] = "ERWARTE_FILIALE"

    elif session["state"] == "ERWARTE_FILIALE":
        session["user_data"]["filiale"] = user_message
        response_data["responses"].append("Super, und in welcher Abteilung?")
        session["state"] = "ERWARTE_ABTEILUNG"

    elif session["state"] == "ERWARTE_ABTEILUNG":
        session["user_data"]["abteilung"] = user_message
        response_data["responses"].append("Perfekt, danke dir!")
        response_data["responses"].append("Um dein Onboarding individuell zu gestalten, stelle ich dir nun 3-4 schnelle Fragen, um deinen bevorzugten Lernstil herauszufinden.")
        response_data["responses"].append("Bist du bereit?")
        session["state"] = "START_LERNTYP_ANALYSE"

    elif session["state"] == "START_LERNTYP_ANALYSE":
        session["user_data"]["lernpfad"] = "Lernpfad: Verkaufsspezialist"
        response_data["responses"].append(f"Alles klar, dein persönlicher Lernpfad '{session['user_data']['lernpfad']}' wird jetzt für dich zusammengestellt.")
        response_data["responses"].append(f"Dein persönlicher Wiederanmelde-Code lautet: {session['user_code']}")
        response_data["responses"].append("Bitte notiere ihn dir gut. Du brauchst ihn, um morgen hier weiterzumachen.")
        response_data["responses"].append("Lass uns mit dem ersten Thema starten!")
        nugget = LERN_NUGGETS[session["current_nugget"]]
        response_data["responses"].append(f"Nugget 1: {nugget['titel']}")
        if nugget['typ'] == 'video':
            response_data["responses"].append(f"Schau dir bitte dieses Video an: {nugget['link']}")
        response_data["responses"].append("Schreibe 'fertig', wenn du das Video angesehen hast.")
        session["state"] = "LERNPHASE"

    elif session["state"] == "LERNPHASE":
        if user_message and "fertig" in user_message.lower():
            session["current_nugget"] += 1
            response_data["responses"].append("Super! Auf zum nächsten Thema...")
        else:
            response_data["responses"].append("Kein Problem, schau dir das Video in Ruhe an und schreibe dann 'fertig'.")

    USER_SESSIONS[session["user_code"]] = session
    return jsonify(response_data)

# --- Server starten ---
if __name__ == '__main__':
    app.run(debug=True)
|null}
                             
    Returns:
        dict: Eine JSON-Antwort für das Frontend.
              Format: {"user_code": string, "responses": [string, ...]}}
    """
    user_code = request_data.get('user_code')
    user_message = request_data.get('message')

    # Prüfen, ob eine bestehende Session geladen werden soll
    if user_code and user_code in USER_SESSIONS:
        session = USER_SESSIONS[user_code]
    else:
        # Neue Session erstellen
        new_code = f"FXXL-{random.randint(1000, 9999)}"
        session = {
            "user_code": new_code,
            "state": "NEU", # Der Zustand der Konversation (z.B. NEU, ERWARTE_NAME, LERNPHASE)
            "user_data": {},
            "current_nugget": 1
        }
        USER_SESSIONS[new_code] = session

    # Die Antwort, die an das Frontend zurückgesendet wird
    response = {
        "user_code": session["user_code"],
        "responses": []
    }

    # =============================================================================
    # HIER FINDET DIE GESAMTE GESPRÄCHSSTEUERUNG STATT (STATE MACHINE)
    # =============================================================================

    if session["state"] == "NEU":
        response["responses"].append("Hallo! Ich bin dein persönlicher Onboarding Manager.")
        response["responses"].append("Wie lautet dein Vorname?")
        session["state"] = "ERWARTE_NAME"

    elif session["state"] == "ERWARTE_NAME":
        session["user_data"]["vorname"] = user_message
        response["responses"].append(f"Danke, {user_message}! In welcher Filiale arbeitest du?")
        session["state"] = "ERWARTE_FILIALE"

    elif session["state"] == "ERWARTE_FILIALE":
        session["user_data"]["filiale"] = user_message
        response["responses"].append("Super, und in welcher Abteilung?")
        session["state"] = "ERWARTE_ABTEILUNG"

    elif session["state"] == "ERWARTE_ABTEILUNG":
        session["user_data"]["abteilung"] = user_message
        response["responses"].append("Perfekt, danke dir!")
        response["responses"].append("Um dein Onboarding individuell zu gestalten, stelle ich dir nun 3-4 schnelle Fragen, um deinen bevorzugten Lernstil herauszufinden.")
        response["responses"].append("Bist du bereit?")
        session["state"] = "START_LERNTYP_ANALYSE"

    elif session["state"] == "START_LERNTYP_ANALYSE":
        # Hier würde die Lerntyp-Analyse stattfinden.
        # ... (Logik für 3-4 Fragen) ...
        # Wir simulieren das Ergebnis für die Demo:
        session["user_data"]["lernpfad"] = "Lernpfad: Verkaufsspezialist"
        response["responses"].append(f"Alles klar, dein persönlicher Lernpfad '{session['user_data']['lernpfad']}' wird jetzt für dich zusammengestellt.")
        response["responses"].append(f"Dein persönlicher Wiederanmelde-Code lautet: {session['user_code']}")
        response["responses"].append("Bitte notiere ihn dir gut. Du brauchst ihn, um morgen hier weiterzumachen.")
        response["responses"].append("Lass uns mit dem ersten Thema starten!")
        
        # Erstes Nugget starten
        nugget = LERN_NUGGETS[session["current_nugget"]]
        response["responses"].append(f"Nugget 1: {nugget['titel']}")
        if nugget['typ'] == 'video':
            response["responses"].append(f"Schau dir bitte dieses Video an: {nugget['link']}")
        response["responses"].append("Schreibe 'fertig', wenn du das Video angesehen hast.")
        session["state"] = "LERNPHASE"

    elif session["state"] == "LERNPHASE":
        if user_message and "fertig" in user_message.lower():
            session["current_nugget"] += 1
            # Logik für das nächste Nugget...
            response["responses"].append("Super! Auf zum nächsten Thema...")
        else:
            response["responses"].append("Kein Problem, schau dir das Video in Ruhe an und schreibe dann 'fertig'.")

    # Den aktualisierten Zustand der Session "speichern"
    USER_SESSIONS[session["user_code"]] = session

    return response

import random
import json


# --- Konfiguration ---
# In einer echten Anwendung würden diese Daten aus einer Datenbank oder Konfigurationsdatei kommen.
LERN_NUGGETS = {
    1: {"titel": "Grundlagen: Unsere Unternehmenswerte", "typ": "video", "link": "https://onedrive.live.com/link_zu_video_1"},
    2: {"titel": "Fahrrad-Leasing: Die Basics", "typ": "video", "link": "https://onedrive.live.com/link_zu_video_2"},
    3: {"titel": "Unser Kassensystem: Eine Einführung", "typ": "text", "inhalt": "Das Kassensystem 'CyclePay' ist einfach..."},
    # ... hier würden alle 21 Nuggets definiert werden.
    21: {"titel": "Abschlusstest & Feedback", "typ": "quiz", "fragen": []}
}

class OnboardingManager:
    """
    Diese Klasse steuert die gesamte Logik des Onboarding-Prozesses.
    Sie verwaltet den Zustand des Nutzers und simuliert die Interaktion.
    """

    def __init__(self):
        """Initialisiert den Manager."""
        self.user_data = {}
        self.current_nugget = 1
        print("Onboarding Manager Backend gestartet.")
        print("-" * 40)

    def _simulate_claude_analysis(self, answers):
        """
        Simuliert die Analyse durch eine KI wie Claude.
        In der Realität würde hier ein API-Aufruf an Claude stattfinden.
        """
        # Einfache Logik für die Demo: Wenn "Verkauf" erwähnt wird,
        # bekommt der Nutzer einen speziellen Lernpfad.
        if "verkauf" in answers.get("abteilung", "").lower():
            return "Lernpfad: Verkaufsspezialist"
        return "Lernpfad: Standard-Onboarding"

    def _generate_user_code(self):
        """Generiert einen einzigartigen, einfachen Code für den Nutzer."""
        # Format: FXXL-XXXX (vier zufällige Ziffern)
        code = f"FXXL-{random.randint(1000, 9999)}"
        return code

    def _save_progress(self, user_code):
        """
        Simuliert das Speichern des Fortschritts.
        In der Realität würde dies in einer einfachen Datenbank oder einer
        dedizierten Datei pro Nutzer geschehen. Wir geben es hier nur aus.
        """
        progress_data = {
            "user_info": self.user_data,
            "current_nugget": self.current_nugget,
            "lernpfad": self.user_data.get("lernpfad"),
            "last_seen": datetime.now().isoformat()
        }
        
        # Simuliertes Speichern als JSON-Datei (ohne echten Dateizugriff)
        print("\n--- [BACKEND-AKTION: Fortschritt wird gespeichert] ---")
        print(f"Dateiname (simuliert): {user_code}.json")
        print(json.dumps(progress_data, indent=2, ensure_ascii=False))
        print("--- [ENDE BACKEND-AKTION] ---\n")

    def _load_progress(self, user_code):
        """
        Simuliert das Laden des Fortschritts.
        In der Realität würde die Datei/Datenbank für den Code gelesen.
        """
        # Wir simulieren hier, dass wir die Daten wiederherstellen.
        # In einer echten App würden wir die JSON-Datei `user_code.json` lesen.
        print(f"\n--- [BACKEND-AKTION: Lade Fortschritt für {user_code}] ---")
        # Feste Demodaten für die Simulation des Ladens
        simulated_data = {
            "user_info": {"vorname": "Max", "filiale": "Frankfurt", "abteilung": "Verkauf"},
            "current_nugget": 3, # Simuliert, dass der Nutzer bei Nugget 3 aufgehört hat
            "lernpfad": "Lernpfad: Verkaufsspezialist",
            "last_seen": "2026-04-16T10:00:00"
        }
        self.user_data = simulated_data["user_info"]
        self.current_nugget = simulated_data["current_nugget"]
        print("Fortschritt erfolgreich geladen.")
        print("--- [ENDE BACKEND-AKTION] ---\n")
        return True # Gibt zurück, ob das Laden erfolgreich war

    def _send_completion_email(self):
        """Simuliert das Senden einer E-Mail an die Filialleitung."""
        filiale = self.user_data.get('filiale', 'Unbekannt')
        vorname = self.user_data.get('vorname', 'Ein neuer Mitarbeiter')
        
        print("\n--- [BACKEND-AKTION: Sende E-Mail] ---")
        print(f"An: filialleitung.{filiale.lower()}@fahrrad-xxl.de")
        print(f"Betreff: Onboarding von {vorname} erfolgreich abgeschlossen")
        print("\nHallo,\n")
        print(f"der neue Mitarbeiter {vorname} hat das digitale Onboarding erfolgreich beendet.")
        print("Die initialen Lerndaten wurden datenschutzkonform gelöscht.\n")
        print("Viele Grüße,")
        print("Ihr digitaler Onboarding Manager")
        print("--- [ENDE BACKEND-AKTION] ---\n")

    def start_new_session(self):
        """Startet eine komplett neue Onboarding-Sitzung."""
        print("ONBOARDING MANAGER: Hallo! Ich bin dein persönlicher Onboarding Manager für Fahrrad XXL.")
        
        # 1. Daten sammeln
        self.user_data['vorname'] = "Max" # Simulierter Input
        print(f"ONBOARDING MANAGER: Wie ist dein Vorname? \nDU: {self.user_data['vorname']}")
        
        self.user_data['filiale'] = "Frankfurt" # Simulierter Input
        print(f"ONBOARDING MANAGER: In welcher Filiale arbeitest du? \nDU: {self.user_data['filiale']}")
        
        self.user_data['abteilung'] = "Verkauf" # Simulierter Input
        print(f"ONBOARDING MANAGER: Und in welcher Abteilung? \nDU: {self.user_data['abteilung']}")

        # 2. Lerntyp-Analyse simulieren
        print("\nONBOARDING MANAGER: Perfekt, danke dir! Um dein Onboarding individuell zu gestalten, stelle ich dir nun 3-4 schnelle Fragen, um deinen bevorzugten Lernstil herauszufinden.")
        print("... (Simulation von 34 Fragen) ...")
        self.user_data['lernpfad'] = self._simulate_claude_analysis(self.user_data)
        print(f"ONBOARDING MANAGER: Analyse abgeschlossen. Dein persönlicher Lernpfad ist: '{self.user_data['lernpfad']}'.")

        # 3. Code generieren und speichern
        user_code = self._generate_user_code()
        self.user_data['code'] = user_code
        print(f"\nONBOARDING MANAGER: Hier ist dein persönlicher Code: {user_code}")
        print("ONBOARDING MANAGER: Bitte notiere ihn dir gut. Wenn du eine Pause machst, kannst du damit genau hier weitermachen.")
        
        self._save_progress(user_code)

        # 4. Lernpfad starten
        self.run_learning_nugget(self.current_nugget)

    def resume_session(self, user_code):
        """Setzt eine bestehende Sitzung fort."""
        print("ONBOARDING MANAGER: Hallo zurück!")
        print(f"ONBOARDING MANAGER: Bitte gib deinen persönlichen Code ein. \nDU: {user_code}")

        if self._load_progress(user_code):
            vorname = self.user_data.get('vorname', 'Mitarbeiter')
            print(f"ONBOARDING MANAGER: Willkommen zurück, {vorname}! Du hast zuletzt bei Nugget {self.current_nugget} aufgehört. Lass uns weitermachen.")
            self.run_learning_nugget(self.current_nugget)
        else:
            print("ONBOARDING MANAGER: Dieser Code ist leider ungültig. Bitte starte eine neue Sitzung.")

    def run_learning_nugget(self, nugget_id):
        """Führt ein spezifisches Lern-Nugget aus."""
        if nugget_id not in LERN_NUGGETS:
            print("ONBOARDING MANAGER: Herzlichen Glückwunsch! Du hast alle Lern-Nuggets abgeschlossen!")
            self._send_completion_email()
            return

        nugget = LERN_NUGGETS[nugget_id]
        print(f"\n--- NUGGET {nugget_id}: {nugget['titel']} ---")
        
        # Zeige den Inhalt je nach Typ
        if nugget['typ'] == 'video':
            print(f"ONBOARDING MANAGER: Schau dir bitte dieses Video an. Klicke auf den Link und komm danach hierher zurück.")
            print(f"--> LINK: {nugget['link']}")
            print("ONBOARDING MANAGER: Schreib 'fertig', wenn du das Video angesehen hast.")
            print("DU: fertig") # Simulierter Input
        
        elif nugget['typ'] == 'text':
            print(f"ONBOARDING MANAGER: Lies dir bitte folgenden Text durch:")
            print(f"'''\n{nugget['inhalt']}\n'''")
            print("ONBOARDING MANAGER: Schreib 'fertig', wenn du es gelesen hast.")
            print("DU: fertig") # Simulierter Input

        # Kurzes Quiz nach dem Nugget
        print("ONBOARDING MANAGER: Super. Eine kurze Frage, um sicherzugehen, dass alles klar war:")
        print("ONBOARDING MANAGER: Welche Unternehmenswerte sind uns besonders wichtig? (Simulierte Quizfrage)")
        print("DU: Ehrlichkeit und Kundenfokus") # Simulierter Input
        print("ONBOARDING MANAGER: Korrekt! Sehr gut.")

        # Fortschritt aktualisieren und speichern
        self.current_nugget += 1
        self._save_progress(self.user_data['code'])

        # Nächstes Nugget starten (oder beenden, wenn es das letzte war)
        # In einer echten Chat-App würde man hier auf die nächste Nutzereingabe warten.
        # Wir simulieren den direkten Übergang.
        if self.current_nugget <= 2: # Wir stoppen in der Demo nach 2 Nuggets
            self.run_learning_nugget(self.current_nugget)


# --- Hauptprogramm: Simulation des gesamten Ablaufs ---
if __name__ == "__main__":
    
    # --- TAG 1: Ein neuer Mitarbeiter startet das Onboarding ---
    print("===== SIMULATION: TAG 1 =====")
    manager = OnboardingManager()
    manager.start_new_session()
    
    # Der Mitarbeiter hat die ersten beiden Nuggets gemacht und macht für heute Schluss.
    # Sein Fortschritt (current_nugget = 3) ist gespeichert.
    # Sein Code ist (z.B.) FXXL-2847.
    user_code_from_day_1 = manager.user_data['code']
    print("\nONBOARDING MANAGER: Das war's für heute! Du kannst den Chat jetzt schließen. Wir sehen uns morgen!")
    print(f"(Der Mitarbeiter notiert sich seinen Code: {user_code_from_day_1})")
    print("\n" + "="*25 + "\n")

    # --- TAG 2: Der Mitarbeiter kommt zurück ---
    print("===== SIMULATION: TAG 2 =====")
    # Erneute Initialisierung, um zu zeigen, dass der Zustand nicht mehr im Speicher ist.
    manager_day_2 = OnboardingManager() 
    # Wir übergeben den Code vom Vortag
    simulated_resume_code = "FXXL-2847" # Wir tun so, als wüssten wir den Code vom Vortag nicht
    manager_day_2.resume_session(simulated_resume_code)

    # Nach dem Laden des Fortschritts ist der Stand `current_nugget = 3`.
    # Die Simulation würde nun mit Nugget 3 weitermachen.
    # Wir simulieren den Abschluss manuell.
    print("\n... (Simulation: Mitarbeiter absolviert die restlichen Nuggets bis 21) ...\n")
    manager_day_2.current_nugget = 22 # Setze den Zähler auf das Ende
    manager_day_2.run_learning_nugget(manager_day_2.current_nugget)
```
