import os


class Lang:
    about_me = ""
    social_text = ""
    welcome_message = ""
    text_projects = ""
    title_about_me = ""
    title_social = ""
    about_me_message = ""
    home = ""

allowed_langs = []

langs = []


def InitLangs():
    files = os.listdir("langs/")
    for file in files:
        if os.path.isfile("langs/" + file):
            allowed_langs.append(file.replace(".txt",""))
            lang_class = Lang()
            lang = open("langs/" + file,"r")
            lang_lines = lang.readlines()
            for line in lang_lines:
                line = line.split("=")
                if line[0] == "about_me":
                   lang_class.about_me = line[1]
                elif line[0] == "social_text":
                   lang_class.social_text = line[1]
                elif line[0] == "welcome_message":
                   lang_class.welcome_message = line[1]
                elif line[0] == "text_projects":
                   lang_class.text_projects = line[1]
                elif line[0] == "title_about_me":
                   lang_class.title_about_me = line[1]
                elif line[0] == "title_social":
                   lang_class.title_social = line[1]
                elif line[0] == "about_me_message":
                   lang_class.about_me_message = line[1]
                elif line[0] == "home":
                   lang_class.home = line[1]
            lang.close()
            langs.append(lang_class)

