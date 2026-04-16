from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# In-memory Sessions (für den Prototyp ok; später DB/Redis)
USER_SESSIONS = {}

LERN_NUGGETS = {
    1: {"titel": "Grundlagen: Unsere Unternehmenswerte", "typ": "video", "link": "https://onedrive.live.com/link_zu_video_1"},
    2: {"titel": "Fahrrad-Leasing: Die Basics", "typ": "video", "link": "https://onedrive.live.com/link_zu_video_2"},
    3: {"titel": "Unser Kassensystem: Eine Einführung", "typ": "text", "inhalt": "Das Kassensystem ist ..."},
}

def build_bot_response(session, user_message):
    state = session["state"]
    responses = []

    if state == "NEU":
        responses.append("Hallo! Ich bin dein persönlicher Onboarding Manager.")
        responses.append("Wie lautet dein Vorname?")
        session["state"] = "ERWARTE_NAME"

    elif state == "ERWARTE_NAME":
        session["user_data"]["vorname"] = (user_message or "").strip()
        responses.append(f"Danke, {session['user_data']['vorname']}! In welcher Filiale arbeitest du?")
        session["state"] = "ERWARTE_FILIALE"

    elif state == "ERWARTE_FILIALE":
        session["user_data"]["filiale"] = (user_message or "").strip()
        responses.append("Super, und in welcher Abteilung?")
        session["state"] = "ERWARTE_ABTEILUNG"

    elif state == "ERWARTE_ABTEILUNG":
        session["user_data"]["abteilung"] = (user_message or "").strip()
        responses.append("Perfekt, danke dir!")
        responses.append("Um dein Onboarding individuell zu gestalten, stelle ich dir nun 3-4 schnelle Fragen, um deinen bevorzugten Lernstil herauszufinden.")
        responses.append("Bist du bereit?")

        # Demo-Sprung: wir nehmen Lerntyp direkt an
        session["user_data"]["lernpfad"] = "Standard-Onboarding"
        session["state"] = "START_LERNTYP_ANALYSE"

    elif state == "START_LERNTYP_ANALYSE":
        responses.append(f"Alles klar, dein persönlicher Lernpfad '{session['user_data']['lernpfad']}' wird jetzt für dich zusammengestellt.")
        responses.append(f"Dein persönlicher Wiederanmelde-Code lautet: {session['user_code']}")
        responses.append("Bitte notiere ihn dir gut. Du brauchst ihn, um morgen hier weiterzumachen.")

        nugget = LERN_NUGGETS.get(session["current_nugget"])
        responses.append("Lass uns mit dem ersten Thema starten!")
        responses.append(f"Nugget {session['current_nugget']}: {nugget['titel']}")
        if nugget["typ"] == "video":
            responses.append(f"Schau dir bitte dieses Video an: {nugget['link']}")
        elif nugget["typ"] == "text":
            responses.append(nugget["inhalt"])
        responses.append("Schreibe 'fertig', wenn du das Thema bearbeitet hast.")

        session["state"] = "LERNPHASE"

    elif state == "LERNPHASE":
        if user_message and "fertig" in user_message.lower():
            session["current_nugget"] += 1
            if session["current_nugget"] not in LERN_NUGGETS:
                responses.append("Glückwunsch! Du hast alle Lern-Nuggets abgeschlossen.")
                responses.append("Die Personalabteilung wurde informiert (Demo).")
                session["state"] = "ABSCHLUSS"
            else:
                responses.append("Super! Auf zum nächsten Thema...")
                nugget = LERN_NUGGETS[session["current_nugget"]]
                responses.append(f"Nugget {session['current_nugget']}: {nugget['titel']}")
                if nugget["typ"] == "video":
                    responses.append(f"Schau dir bitte dieses Video an: {nugget['link']}")
                else:
                    responses.append(nugget["inhalt"])
                responses.append("Schreibe 'fertig', wenn du das Thema bearbeitet hast.")
        else:
            responses.append("Kein Problem. Nimm dir Zeit und schreibe dann 'fertig', wenn du bereit bist.")

    elif state == "ABSCHLUSS":
        responses.append("Das Onboarding ist abgeschlossen. Vielen Dank!")

    # Persistiere den Session-Stand
    USER_SESSIONS[session["user_code"]] = session
    return responses

@app.route("/", methods=["GET"])
def serve_frontend():
    # Minimaler Frontend-Test-Stand (passt für Render sofort).
    # (Wenn du lieber die schönere Version aus deinem Canvas willst, geben wir die gleich wieder sauber rein.)
    return """
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FXXL Akademie - Onboarding Manager</title>
</head>
<body style="font-family: Arial, sans-serif; background:#f4f4f4; display:flex; justify-content:center; align-items:center; height:100vh; margin:0;">
  <div style="width:100%; max-width:650px; background:white; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.1); overflow:hidden;">
    <div style="background:#D32D3A; color:white; padding:20px; text-align:center;">
      <h1 style="margin:0; font-size:22px;">Fahrrad XXL Akademie</h1>
      <div style="opacity:0.9; margin-top:6px;">Gemeinsam. Weiter. Bilden.</div>
    </div>

    <div id="chat" style="height:70vh; overflow-y:auto; padding:18px; display:flex; flex-direction:column; gap:10px;"></div>

    <div style="display:flex; gap:10px; padding:15px; border-top:1px solid #e0e0e0;">
      <input id="input" type="text" placeholder="Schreibe eine Antwort..." style="flex:1; padding:10px 14px; border:1px solid #e0e0e0; border-radius:20px;">
      <button id="send" style="width:48px; border:none; border-radius:50%; background:#D32D3A; color:white; cursor:pointer;">➤</button>
    </div>
  </div>

<script>
  const chat = document.getElementById('chat');
  const input = document.getElementById('input');
  const send = document.getElementById('send');
  let userCode = null;

  function add(text, type){
    const div = document.createElement('div');
    div.textContent = text;
    div.style.padding = '10px 14px';
    div.style.borderRadius = '18px';
    div.style.maxWidth = '75%';
    div.style.whiteSpace = 'pre-wrap';
    if(type==='bot'){
      div.style.background = '#eef2f6';
      div.style.alignSelf = 'flex-start';
    }else{
      div.style.background = '#D32D3A';
      div.style.color = 'white';
      div.style.alignSelf = 'flex-end';
    }
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
  }

  async function sendMessage(msg){
    input.disabled = true;
    send.disabled = true;

    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ user_code: userCode, message: msg })
    });

    const data = await res.json();
    if(data.user_code) userCode = data.user_code;

    for(const m of data.responses){
      add(m, 'bot');
    }

    input.disabled = false;
    send.disabled = false;
    input.focus();
  }

  async function init(){
    await sendMessage(null);
  }

  send.onclick = () => {
    const v = input.value.trim();
    if(!v) return;
    add(v, 'user');
    input.value = '';
    sendMessage(v);
  };

  input.addEventListener('keydown', (e) => {
    if(e.key === 'Enter'){
      send.onclick();
    }
  });

  window.onload = init;
</script>
</body>
</html>
"""

@app.route("/api/chat", methods=["POST"])
def api_chat():
    request_data = request.get_json(silent=True) or {}
    user_code = request_data.get("user_code")
    user_message = request_data.get("message")

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

    responses = build_bot_response(session, user_message)
    return jsonify({"user_code": session["user_code"], "responses": responses})

# gunicorn nutzt app:app, daher kein app.run nötig; aber für lokale Tests ok:
if __name__ == "__main__":
    app.run(debug=True)
