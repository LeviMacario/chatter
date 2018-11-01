from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


TALK = [
    'Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?',
    'Sim, eu programo em Python', 'Não quero mais falar com você',
    'Se não quiser mais falar comigo, escreva: até logo',
    'Qual seu nome?', 'Meu nome é João',
]

class Chat:
    '''
    Classe responsável por iniciar o bot,
    realizar a aprendizagem do bot e
    responder as perguntas do usuário.
    '''
    def __init__(self, main_name='TW Chat Bot'):
        self.bot = ChatBot(main_name)
        self.bot.set_trainer(ListTrainer)
        self.bot.train(TALK)

    def reply(self, question):
        if question == 'até logo':
            return 'TW Bot: Tchau! Beijos! ;'
        reply = self.bot.get_response(question)
        if float(reply.confidence) > 0.5:
            return 'TW Bot: %s' % reply
        else:
            return 'TW Bot: Ainda não sei responder esta pergunta'
