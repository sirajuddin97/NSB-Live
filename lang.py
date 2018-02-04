def translate(text, lang):
    if lang == 'en':
        if text == "settings": return "Settings";
        if text == "open": return "GitHub";
        if text == "quit": return "Quit";

    elif lang == 'no':
        if text == "settings": return "Innstillinger";
        if text == "open": return "GitHub";
        if text == "quit": return "Avslutt";

    else:
        return "Invalid language!";
