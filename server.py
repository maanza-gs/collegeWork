from socket import *
import json
import threading

#Open server socket for connections
serverPort=14000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))

#Initializations
login_count = 0
lock = threading.Lock()
separator = '=================================\n'
received_message = None
print(separator)
player_count_str = input('Number of players: ')
player_count = int(player_count_str)
serverSocket.listen(player_count-1)
player_identifiers = []



def askPlayerPlayAgain(index,player_info):
    try:
        if player_info != None:
            player_info[0].send('dywpa'.encode())
            waitUntilClientReadsTheMessage(player_info)
            received_message = player_info[0].recv(1024)
            if received_message.decode() == 'n':
                with lock:
                    player_info[0].close()
                    player_identifiers[index] = None
            else:
                print('PLAYER',index+1,'wants to play again.')
                message = 'Please wait for the next game . . .'
                sendMessageToTheSpecifiedPlayer(player_identifiers,message,index)
    except:
        print('Error: Connection Lost. ' + ' (' + player_info[2] + ')')
        with lock:
            player_identifiers[index] = None

def collectDYWPAinfo(player_identifiers):
    message = separator
    sendSameMessageToAllPlayers(player_identifiers,message)
    t_dywpas = []
    for index,player_info in enumerate(player_identifiers):
        if player_info != None:
            t_dywpa = threading.Thread(target=askPlayerPlayAgain, args=(index,player_info))
            t_dywpas.append(t_dywpa)
            t_dywpa.start()
    for t_dywpa in t_dywpas:
        t_dywpa.join()

def acceptConnections():
    while True:
        connectionSocket,addr=serverSocket.accept()
        thread = threading.Thread(target = showMenuToTheGuest,args = (connectionSocket,addr))
        thread.start()

def registerTheGuest(connectionSocket,addr):
    try:
        message = 'Register!'
        connectionSocket.send(message.encode())
        waitUntilClientReadsTheMessage((connectionSocket,addr))
        username = connectionSocket.recv(1024).decode()
        connectionSocket.send(str(700).encode())
        password = connectionSocket.recv(1024).decode()
        if username in players:
            message = separator + 'Error: Username taken.\n' + separator
            connectionSocket.send(message.encode())
            waitUntilClientReadsTheMessage((connectionSocket,addr))
            return False
        else:
            players[username] = password
            return True
    except:
        print('Error: Guest Connection Lost During Registeration.')
        pass
    return False


def loginTheGuest(guest_info):
    try:
        message = 'Login!'
        guest_info[0].send(message.encode())
        waitUntilClientReadsTheMessage((guest_info[0],guest_info[1]))
        username = guest_info[0].recv(1024).decode()
        guest_info[0].send(str(700).encode())
        password = guest_info[0].recv(1024).decode()
        if username not in players:
            message = separator + 'Error: User not found.\n' + separator
            guest_info[0].send(message.encode())
            waitUntilClientReadsTheMessage((guest_info[0],guest_info[1]))
            return False, None
        elif players[username] == password:
            message = separator + 'Success: Login Successful.\n' + separator
            guest_info[0].send(message.encode())
            waitUntilClientReadsTheMessage((guest_info[0],guest_info[1]))
            guest_info = (guest_info[0],guest_info[1],username)
            return True, guest_info
        else:
            message = separator + 'Error: Incorrect password.\n' + separator
            guest_info[0].send(message.encode())
            waitUntilClientReadsTheMessage((guest_info[0],guest_info[1]))
            return False, None
        return False, None
    except:
        print('Error: Guest Connection Lost During Login.')

def showMenuToTheGuest(connectionSocket,addr):
    global login_count
    try:
        message = separator + 'WELCOME TO HANGMAN'
        connectionSocket.send(message.encode())
        waitUntilClientReadsTheMessage((connectionSocket,addr))
        while True:
            message = 'Menu:\n1. Register\n2. Login\n3. Exit'
            connectionSocket.send(message.encode())
            waitUntilClientReadsTheMessage((connectionSocket,addr))
            received_message = connectionSocket.recv(1024).decode()
            if received_message != str(1) and received_message != str(2) and received_message != str(3):
                message = separator + 'Error: Undefined response. Only (1/2/3) allowed.\n' + separator
                connectionSocket.send(message.encode())
                waitUntilClientReadsTheMessage((connectionSocket,addr))
                continue
            else:
                if received_message == str(1):
                    if registerTheGuest(connectionSocket,addr):
                        message = separator + 'Success: Registeration Successful.\n' + separator
                        connectionSocket.send(message.encode())
                        waitUntilClientReadsTheMessage((connectionSocket,addr))
                elif received_message == str(2):
                    with lock:
                        if login_count == player_count:
                            message = separator + 'Error Maximum player count reached. Cannot Login.\n' + separator
                            connectionSocket.send(message.encode())
                            waitUntilClientReadsTheMessage((connectionSocket,addr))
                            message = 'Exit!'
                            connectionSocket.send(message.encode())
                            waitUntilClientReadsTheMessage((connectionSocket,addr))
                            connectionSocket.close()
                            return
                    login_result, guest_info = loginTheGuest((connectionSocket,addr))
                    if login_result:
                        with lock: 
                            player_identifiers.append(guest_info)
                            message = str(len(player_identifiers)) + '/' + player_count_str + ' Players Connected . . .\nPlease Wait . . .'
                            sendSameMessageToAllPlayers(player_identifiers,message)
                            login_count += 1
                        return
                else:
                    connectionSocket.close()
                    return
    except:
        # print('Error: Guest Connection Lost.')
        pass  


def loadPlayerInfo():
    with open('players.json', 'r') as inf:
        players = json.load(inf)
    return players

def savePlayerInfo(players):
    with open('players.json', 'w') as outf:
        json.dump(players,outf)

def waitUntilClientReadsTheMessage(player_info):
    try:
        if player_info != None:
            reveived_message = player_info[0].recv(1024)
            if reveived_message.decode() == str(700):
                return
    except:
        if player_info in player_identifiers:
            [None if x==player_info else x for x in player_identifiers]
            message = 'Error: Connection Lost.' + ' (' + player_info[2] + ')'
            sendSameMessageToAllPlayers(player_identifiers,message)
        else:
            print('Error: Guest Connection Lost.')

def initializePlaceholder(word,placeholder):
    placeholder.clear()
    for c in word:
        placeholder.append('-')

def updatePlaceholder(word,placeholder,guess=None):
    if guess:
        if len(guess) > 1:
            if word == guess:
                for index,c in enumerate(word):
                    placeholder[index] = c
                return True, True
            return False,False
        for index,c in enumerate(word):
            if c == guess:
                placeholder[index] = c
        if wordIsFullyPredicted(placeholder):
            return True,True
        if guess in word:
            return False,True
        return False,False
    return False,False

def wordIsFullyPredicted(placeholder):
    if '-' in placeholder:
        return False
    return True

def sendSameMessageToAllPlayers(player_identifiers, message, skip_player_index=(-1), inform_also_server = True):
    
    if inform_also_server:
        print(message)
    for index,player_info in enumerate(player_identifiers):
        if player_info != None:
            if index == skip_player_index:
                continue
            try:
                player_info[0].send(message.encode())
                waitUntilClientReadsTheMessage(player_info)
            except:
                # player_identifiers.remove(player_info)
                player_identifiers[index] = None
                message = 'Error: Connection Lost.' + ' (' + player_info[2] + ')'
                sendSameMessageToAllPlayers(player_identifiers,message,inform_also_server=False)
            # time.sleep(0.2)

def sendMessageOnlyIndexDifferToAllPlayers(player_identifiers, message):
    for index,player_info in enumerate(player_identifiers):
        if player_info != None:
            try:
                player_info[0].send((message + str(index+1) + ' (' + player_info[2] + ')').encode())
                waitUntilClientReadsTheMessage(player_info)
            except:
                # print('Error: Connection Lost. ' + ' (' + player_info[2] + ')')
                player_identifiers[index] = None
                message = 'Error: Connection Lost. ' + ' (' + player_info[2] + ')'
                sendSameMessageToAllPlayers(player_identifiers,message)
            # time.sleep(0.2)

def sendMessageToTheSpecifiedPlayer(player_identifiers,message,index):
    try:
        if player_identifiers[index] != None:
            player_identifiers[index][0].send(message.encode())
            waitUntilClientReadsTheMessage(player_identifiers[index])
    except:
        # print('Error: Connection Lost. ' + ' (' + player_identifiers[index][2] + ')')
        player_identifiers[index] = None
        message = 'Error: Connection Lost. ' + ' (' + player_identifiers[index][2] + ')'
        sendSameMessageToAllPlayers(player_identifiers,message)
    
    # time.sleep(0.2)


#Load players from file 
players = loadPlayerInfo()

#Accept all client connections continuously (Seconder Thread)
t_acceptor = threading.Thread(target = acceptConnections)
t_acceptor.start()


while True:
    #Greet Players
    player_count = int(player_count_str)
    login_count = len(player_identifiers)
    message = separator + 'WELCOME TO HANGMAN'
    sendSameMessageToAllPlayers(player_identifiers,message)
    message = 'Waiting for ' + str(player_count - len(player_identifiers)) + ' players to connect . . .'
    sendSameMessageToAllPlayers(player_identifiers,message)

    #Wait for player connections
    message = str(len(player_identifiers)) + '/' + player_count_str + ' players connected . . .'
    sendSameMessageToAllPlayers(player_identifiers,message)
    while True:
        if login_count == player_count:
            with lock:
                message = 'Last Connection Check . . .'
                sendSameMessageToAllPlayers(player_identifiers,message)
                player_identifiers = list(filter(lambda a: a != None, player_identifiers))
                login_count = len(player_identifiers)
            if login_count == player_count:
                break
            else:
                message = 'Error: Some Connections Lost.\n' + str(login_count) + '/' + str(player_count) + ' Players Connected . . .'
                sendSameMessageToAllPlayers(player_identifiers,message)

    #Tell all the players that all connections are established.
    message = 'All connections established.'
    sendSameMessageToAllPlayers(player_identifiers,message)

    #Tell players their player numbers
    message = separator + 'You are: PLAYER '
    sendMessageOnlyIndexDifferToAllPlayers(player_identifiers,message)

    #Tell players to get ready
    message = 'Game Is About To Start . . . GET READY!'
    sendSameMessageToAllPlayers(player_identifiers,message)
    
    #Initializations
    turn_index = 0
    make_a_guess = 'mag'
    winner_index = None
    word_found = False
    word = input(separator + 'Enter secret word: ')
    hint = input('Enter a hint: ')
    print(separator)
    placeholder = list()
    initializePlaceholder(word,placeholder)
    round_count = 1
    wrong_guesses_remaining = 7
    wrong_guesses = set()
    guess = None
    message = None

    #Tell players that the game is started
    message = 'Game Is Started. GOOD LUCK!'
    sendSameMessageToAllPlayers(player_identifiers,message)

    #GAMEPLAY
    while (not word_found) and wrong_guesses_remaining:
        #Tell players which round they are playing
        message = separator + 'ROUND ' + str(round_count)
        sendSameMessageToAllPlayers(player_identifiers,message)
        message = 'REMAINING GUESSES: ' + str(wrong_guesses_remaining)
        sendSameMessageToAllPlayers(player_identifiers,message)
        message = 'HINT: ' + hint
        sendSameMessageToAllPlayers(player_identifiers,message)
        message = 'WORD: ' + (''.join([str(elem) for elem in placeholder]))
        sendSameMessageToAllPlayers(player_identifiers,message)
        message = 'WRONG GUESSES: ' + (''.join([str(elem) + ', ' for elem in wrong_guesses]))
        sendSameMessageToAllPlayers(player_identifiers,message)

        #Tell players whose turn it is.
        if player_identifiers[turn_index] != None:
            message = 'PLAYER ' + str(turn_index+1) + ' (' + player_identifiers[turn_index][2] + ')' '\'s TURN.\nWait For The Guess . . .'
            sendSameMessageToAllPlayers(player_identifiers,message,turn_index)
            message = 'YOUR TURN!'
            sendMessageToTheSpecifiedPlayer(player_identifiers,message,turn_index)
    
        #Receive the guess
        try:
            guess = None
            if player_identifiers[turn_index] != None:
                player_identifiers[turn_index][0].send(make_a_guess.encode())
                waitUntilClientReadsTheMessage(player_identifiers[turn_index])
                guess = player_identifiers[turn_index][0].recv(1024)
        except:
            # print('Error: Connection Lost. ' + ' (' + player_identifiers[turn_index][2] + ')')
            player_identifiers[turn_index] = None
            message = 'Error: Connection Lost. ' + ' (' + player_identifiers[turn_index][2] + ')'
            sendSameMessageToAllPlayers(player_identifiers,message)
            

        #Tell players what guess is made
        if guess != None and guess.decode() != '':
            message = 'PLAYER ' + str(turn_index+1) + ' (' + player_identifiers[turn_index][2] + ')' ' GUESSED: ' + guess.decode()
            sendSameMessageToAllPlayers(player_identifiers,message,turn_index)
            message = 'YOU GUESSED: ' + guess.decode()
            sendMessageToTheSpecifiedPlayer(player_identifiers,message,turn_index)
        
            #check the guess
            word_found,letter_found = updatePlaceholder(word,placeholder,guess.decode())
            message = separator + 'ROUND ' + str(round_count) + ' RESULTS:'
            sendSameMessageToAllPlayers(player_identifiers,message)
            if not word_found and not letter_found:
                message = 'WRONG GUESS!: ' + guess.decode()
                wrong_guesses.add(guess.decode())
            else:
                message = 'CORRECT GUESS!: ' + guess.decode()
            sendSameMessageToAllPlayers(player_identifiers,message)
            message = 'WORD(After Guess): ' + (''.join([str(elem) for elem in placeholder]))
            sendSameMessageToAllPlayers(player_identifiers,message)

            if not letter_found:
                wrong_guesses_remaining -= 1
            
            if word_found:
                winner_index = turn_index

        #Update turn index for the next round
        # player_count = len(player_identifiers) - player_identifiers.count(None) 
        turn_index += 1
        turn_index = turn_index % player_count
        round_count += 1


        #Check if there are any players left
        if player_identifiers.count(None) == len(player_identifiers):
            break

    #Report the results to all players
    message = separator + 'GAME OVER'
    sendSameMessageToAllPlayers(player_identifiers,message)
    if winner_index != None:
        message = 'PLAYER ' + str(winner_index+1) + ' WINS!'
        sendSameMessageToAllPlayers(player_identifiers,message,winner_index)
        message = 'YOU WIN! CONGRATULATIONS.'
        sendMessageToTheSpecifiedPlayer(player_identifiers,message,winner_index)
    else:
        message = 'NO WINNER.'
        sendSameMessageToAllPlayers(player_identifiers,message,winner_index)

    #Ask players if they want to play again
    collectDYWPAinfo(player_identifiers)

    #Remove players who does not want to play again AND whose connection is lost
    player_identifiers = list(filter(lambda a: a != None, player_identifiers))
    # for player_to_remove in players_to_remove:
    #     player_identifiers.remove(player_to_remove)
    #     try:
    #         player_to_remove[0].close()
    #     except:
    #         print('Connection Already Lost.')
    
    
    #Save newly registred players to file
    savePlayerInfo(players)