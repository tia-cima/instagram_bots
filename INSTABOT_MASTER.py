from instabot import Bot
import time
import os
import random


def login(name, pw):
    choice = int(input("\nVuoi usare l'account inserito prima (1) oppure inserirne uno nuovo? (2): "))
    if choice == 1:
        username = name
        passw = pw
    else:
        username = input("\nInserisci il nome utente a cui accedere: ")
        passw = input("\nInserisci la password: ")
    return username, passw



class User:

    def __init__(self, user, passw):
        self.user = user
        self.passw = passw


    def like(self):
        print("\nQuesta funzione ti permette di mettere like ad ogni post di un singolo user. \n")

        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        account = input("\nInserisci l'account a cui mettere like: ")

        bot = Bot(max_likes_to_like = 0, like_delay = 5)
        bot.login(username = username, password = passw)
        photo = bot.get_user_medias(bot.get_user_id_from_username(account))

        for n in range (len(photo)): 
            print(f"Like messo al post numero {n + 1}. Se cosi' non fosse, e' gia' stato messo mi piace con lo stesso account.")        
            bot.like(str(photo[n]))


    def comment(self):
        print("\nQuesta funzione ti permette di commentare ogni post di un singolo user con una frase a tua scelta.\n")
        
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        account = input("\nInserisci l'account a cui commentare: ")
        comment = input("\nInserisci la frase da commentare: ")

        bot = Bot (comment_delay = 10, max_comments_per_day= 10000)
        bot.login(username = username, password = passw)
        media = bot.get_total_user_medias(account)

        for n in range (len(media)):
            bot.comment(media[n], comment)
            print(f"\nFoto numero {n + 1} commentata. Se cosi' non fosse, la foto e' gia' stata commentata dallo stesso account.")


    def follow(self):
        print("\nQuesta funzione ti permette di seguire ogni follower di un singolo utente (quindi seguire le persone che seguono un altro utente).\n")
        
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        account = input("\nInserisci l'account da cui seguire i follower: ")

        bot = Bot(follow_delay = 5, max_follows_per_day = 10000)
        bot.login(username = username, password = passw )
        people = bot.get_user_followers(bot.get_user_id_from_username(account))

        for n in range (len(people)):    
            bot.follow(str(people[n]))
            print(f"Persone seguite: {n + 1}. Se l'ultimo account non fosse stato seguito, vuol dire che lo era gia'.")

  
    def direct(self):
        print("\nQuesta funzione ti permette di inviare un tot di messaggi a tua scelta ad un singolo utente.\n")
    
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        account = input("\nInserisci l'user a cui inviare il dm: ")
        num = int(input("\nInserisci la quantita' di messaggi da inviare: "))
        message = input("\nInserisci il messaggio da inviare: ")

        bot = Bot(message_delay = 5)
        bot.login(username = username, password = passw)
        account = bot.get_user_id_from_username(account)

        for n in range(num):     
            bot.send_message(message, account)
            print(f"\nmessage numero {n + 1} inviato.")



class Hashtag:
        
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw


    def like(self):
        print("\nQuesta funzione ti permette di mettere like ad ogni post sotto ad un hashtag a tua scelta (ad esempio, inserendo l'hashtag #like4like, si andra' a mettere like ad ogni post contenente l'hashtag #like4like).\n")
    
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        hshtg = input("\nInserisci l'hashtag da prendere in considerazione: ")

        bot = Bot(max_likes_to_like = 0, like_delay = 5)
        bot.login(username = username, password = passw)

        bot.like_hashtag(hshtg)
        print("Like messo a tutte le foto")


    def comment(self): 
        print("\nQuesta funzione ti permette di commentare ogni post sotto ad un hashtag a tua scelta (ad esempio, inserendo l'hashtag #dog, si andra' a commentare ogni post contenente l'hashtag #dog). \n")
    
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        hshtg = input("\nInserisci l'hashtag da prendere in considerazione: ")
        comment = input("\nInserisci la frase da commentare: ")

        bot = Bot (comment_delay = 10, max_comments_per_day= 10000)
        bot.login(username = username, password = passw)
        media = bot.get_total_hashtag_medias(hshtg)     

        for n in range (len(media)):
            bot.comment(media[n], comment)
            print(f"\nFoto numero {n + 1} commentata. Se cosi' non fosse, la foto e' gia' stata commentata dallo stesso account.")


    def follow(self):
        print("\nQuesta funzione ti permette di seguire ogni user sotto ad un hashtag a tua scelta (ad esempio, inserendo l'hashtag #follow4follow, si andra' a seguire ogni user sotto l'hashtag #follow4follow. \n")
      
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        hshtg = input("\nInserisci l'hashtag da prendere in considerazione: ")

        bot = Bot(follow_delay = 5, max_follows_per_day = 10000)
        bot.login(username = username, password = passw )
        person = bot.get_hashtag_users(hshtg)
        
        for n in range (len(person)):    
            bot.follow(str(person[n]))
            print(f"Persone seguite: {n + 1}. Se l'ultimo account non fosse stato seguito, vuol dire che lo era gia'.")


    def direct(self):
        print("\nQuesta funzione ti permette di inviare un direct (ogni 20 secondi per evitare di essere bloccato da instagram) ad ogni utente sotto un certo hashtag.\n")
    
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        hshtg = input("\nInserisci l'hashtag da cui prendere gli utenti a cui inviare il dm: ")
        message = input("\nInserisci il messaggio da inviare: ")

        bot = Bot(message_delay = 5)
        bot.login(username = username, password = passw)
        accounts = bot.get_hashtag_users(hshtg)

        for n in range(len(accounts)):     
            bot.send_message(message, accounts[n])
            print(f"\nmessage numero {n + 1} inviato.")
            time.sleep(20)



class Post:

    def __init__(self, user, passw):
        self.user = user
        self.passw = passw


    def post(self):
        print("\nQuesta funzione ti permette di postare piu' post differenti in un tot di tempo a tua scelta. \n")
    
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        delay = int(input("\nInserisci l'arco di tempo fra un post e l'altro (secondi): "))
        photo = input("\nInserisci il percorso della foto che vuoi caricare: ")
        description = input("\nInserisci la descrizione: ")

        bot = Bot()
        bot.login(username = username, password = passw)

        while(True):
            bot.upload_photo(photo, caption = description)
            print(f"\nFoto postata. Se cosi' non fosse, la foto non ha un aspect rateo compatibile con instagram, prova a ridimensionarla.\n\n")
            time.sleep(delay)
            os.rename(f'{photo}.REMOVE_ME', photo)


    def post_more(self):
            print("\nQuesta funzione ti permette di postare un solo post ogni tot di tempo a tua scelta. \n")
        
            username, passw = login(self.user, self.passw)
            print("\n----------------------------")
            delay = int(input("\nInserisci l'arco di tempo fra un post e l'altro (secondi): "))
            path = input("\nInserire il percorso della cartella con le foto da postare: (ad esempio foto/ oppure Desktop/instabot/foto): ")

            print("\nInserisci le descrizioni che saranno scelte in ordine casuale da mettere sotto i post, appena si ha finito premere 'gg'.\n ")
            comments = []
            while(True):
                description = input("--> ")
                if description == "gg":
                    break 
                else: 
                    comments.append(description)

            print(f"\n***QUESTE PAROLE VERRANNO INSERITE IN ORDINE CASUALE SOTTO LE FOTO: {comments}***\n")

            bot = Bot()
            bot.login(username = username, password = passw)

            os.chdir(path)
            video = os.listdir()

            for n in range(len(video)):
                bot.upload_photo(str(video[n]), caption = random.choice(comments))
                print("Foto postata. Se cosi' non fosse, la foto non ha un aspect rateo compatibile con instagram, prova a ridimensionarla.\n\n")
                time.sleep(delay) 



print('''   \n\nPROGRAMMA REALIZZATO UTILIZZANDO LA LIBRERIA PYTHON INSTABOT, TUTTI I DIRITTI RISERVATI. 
TUTTE LE ATTIVITA' RICONDUCIBILI A BOT SUL PROPRIO ACCOUNT INSTAGRAM POTREBBERO PORTARE AL BAN SE UTILIZZATE IN MANIERA EVIDENTE, NON MI ASSUMO ALCUNA RESPONSABILITA' SE CIO' DOVESSE ACCADERE.''')

user = input("\n\nPer prima cosa, inserisci il nome utente dell'account a cui vuoi accedere (vai tranquillo, i tuoi dati non mi interessano. Servono solo al programma per avviarsi): ")
password = input("\nInserisci la password: ")

print("\n\nBenvenuto! Il bot si sta avviando...")
time.sleep(5) # solo per fare scena dio che cringe


while(True):
    action = int(input('''



██╗██╗         ████████╗██╗   ██╗ ██████╗     ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗   
██║██║         ╚══██╔══╝██║   ██║██╔═══██╗    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║   
██║██║            ██║   ██║   ██║██║   ██║    ██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║   
██║██║            ██║   ██║   ██║██║   ██║    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║   
██║███████╗       ██║   ╚██████╔╝╚██████╔╝    ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║▄█╗
╚═╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝     ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝
                                                                                                                                                                                                                                                   
    
██╗██╗         ████████╗██╗   ██╗ ██████╗     ██████╗  ██████╗ ████████╗
██║██║         ╚══██╔══╝██║   ██║██╔═══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
██║██║            ██║   ██║   ██║██║   ██║    ██████╔╝██║   ██║   ██║   
██║██║            ██║   ██║   ██║██║   ██║    ██╔══██╗██║   ██║   ██║   
██║███████╗       ██║   ╚██████╔╝╚██████╔╝    ██████╔╝╚██████╔╝   ██║   
╚═╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                                    
                    SCEGLI IL TIPO DI CONTENUTO DA CONSIDERARE:
                    1 = USER: METTI LIKE, COMMENTA, SEGUI O MESSAGGIA UN UTENTE SPECIFICO
                    2 = HASHTAG: METTI LIKE, COMMENTA, SEGUI, MESSAGGIA TUTTI GLI UTENTI/POST SOTTO UN RELATIVO HASHTAG
                    3 = POST: POSTA IN UN ARCO DI TEMPO DEFINITO DA TE LA STESSA FOTO CONTINUAMENTE O PIU' POST DIFFERENTI
                    4 = ESCI DAL PROGRAMMA

                    ---> '''))
    
    if action == 1:
        userData = User(user, password)           
        while(True):        
            action_user = int(input('''
                    
                    USER: 
                    1) METTI LIKE A TUTTI I POST RELATIVI AD UN USER
                    2) COMMENTA SOTTO TUTTI I POST RELATIVI AD UN USER
                    3) SEGUI TUTTE I FOLLOWER DI UN USER
                    4) INVIA DM SPAM AD UN USER
                    5) TORNA AL MENU PRINCIPALE
                    
                    --> '''))
            if action_user == 1:
                userData.like()
            elif action_user == 2:
                userData.comment()
            elif action_user == 3:
                userData.follow()
            elif action_user == 4:
                userData.direct()
            else:
                print("\nUscita...\n")
                break


    elif action == 2:
        hashData = Hashtag(user, password)
        while(True):
            action_hashtag = int(input('''
                    
                    HASHTAG:
                    1) METTI LIKE A TUTTI I POST RELATIVI AD UN HASHTAG
                    2) COMMENTA SOTTO TUTTI I POST RELATIVI AD UN HASHTAG
                    3) SEGUI TUTTE LE PERSONE CHE HANNO POST SOTTO UN HASHTAG
                    4) INVIA DM SPAM A TUTTI GLI UTENTI CHE HANNO POST SOTTO UN HASHTAG
                    5) TORNA AL MENU PRINCIPALE            
                    
                    --> '''))
            if action_hashtag == 1:
                hashData.like()
            elif action_hashtag == 2:
                hashData.comment()
            elif action_hashtag == 3:
                hashData.follow()
            elif action_hashtag == 4:
                hashData.direct()
            else:
                print("\nUscita...\n")
                break


    elif action == 3:
        postData = Post(user, password)
        while(True):        
            action_post = int(input('''
                
                POST:
                1) POSTA LO STESSO POST OGNI TOT DI TEMPO
                2) POSTA FOTO DIFFERENTI OGNI TOT DI TEMPO
                3) TORNA AL MENU PRINCIPALE
                
                --> '''))
            if action_post == 1:
                postData.post()
            elif action_post == 2:
                postData.post_more()
            else:
                print("\nUscita...\n")
                break


    elif action == 4:
        print("\nUscita...\n")
        time.sleep(5)
        break
   

    else:
        print("Carattere errato, fai il serio")
        continue


# version 1.0, published on 10/10/2020
    
