from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import JaccardSimilarity
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.logic import BestMatch
import chatterbot as ch;
import re



#f=open('FIA.txt','r').readlines()

proy=open('fia.yaml','r').readlines()





chatb=ChatBot("EDI",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../database.db",


    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": ch.comparisons.levenshtein_distance,
            "response_selection_method": ch.response_selection.get_first_response
            #"statement_comparison_function": levenshtein_distance,
            #"response_selection_method": get_most_frequent_response
     }
    ]
    )

trainerCorpus=ChatterBotCorpusTrainer(chatb)
trainerCorpus.train(
    #"chatterbot.corpus.spanish"
    "./fia.yaml"
)

trainer=ListTrainer(chatb)


trainer.train("./fia.yaml")



print("Escribe algo aqui")
while True:
    try:
        chatbot_input=chatb.get_response(input('Q:'))
        print('A:',chatbot_input)
    except(KeyboardInterrupt,EOFError,SystemExit):
        break




